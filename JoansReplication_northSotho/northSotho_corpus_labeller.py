import openpyxl

'''
Labelling for northern sotho, corpus will be prelabelled with noun information
'''

prefixingInformation = {
    '1a':['o','a'],
    '1':['o','a'],
    '2':['ba','ba'],
    '2b':['ba','ba'],
    '3':['o','wa'],
    '4':['e','ya'],
    '5':['le','la'],
    '6':['a','a'],
    '7':['se','sa'],
    '8':['di','tsa'],
    '9':['e','ya'],
    '10':['di','tsa'],
    '14':['bo','bja'],
    '15':['go','gwa'],
    '16':['go','gwa'],
    '17':['go','gwa'],
    '18':['go','gwa'],
    'n':['go','gwa'],
    '24':['go','gwa'],
}



# Load the Excel file
workbook = openpyxl.load_workbook(f'./DataFiles/NorthernSothoSingle.xlsx')
worksheet = workbook.active

# Get all the class labels from the second column
nouns = [(row[0].lower(),row[1]) for row in worksheet.iter_rows(min_row=1, values_only=True)]

# clean each sentence and apply rules to create labelled corpus
def clean_and_save_text_for_fasttext(input_file_path, output_file_path):
    
    # Open and read the input file
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    # Define a function to clean each line
    def clean_line(line):
        global number_of_lines
        global progress 
        words = line.split(" ")
        words = [s.strip() for s in words]
        label_str = ""

        last_noun=None

        for word in words:
            noun_match = [(w,s) for w,s in nouns if w==word]
            if noun_match:
                label_str += "__label__"+str(noun_match[0][1])+" "
                last_noun = str(noun_match[0][1])
            else:
                if(last_noun):
                    if(word in prefixingInformation[last_noun]):

                        label_str += "__label__SC"+last_noun+" "


                        last_noun=None
        progress+=1
        print(str(progress) +' out of ' + str(number_of_lines), end='\r')
        return label_str + " ".join(words)

    global number_of_lines
    number_of_lines =lines.__len__()
    global progress
    progress=0

    # Apply the cleaning function to each line
    cleaned_lines = [clean_line(line) for line in lines]

    # Write the cleaned lines to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for cleaned_line in cleaned_lines:
            output_file.write(cleaned_line + '\n')


clean_and_save_text_for_fasttext("./DataFiles/nSotho_clean_corpus.txt","nSotho_labelled_corpus.txt")