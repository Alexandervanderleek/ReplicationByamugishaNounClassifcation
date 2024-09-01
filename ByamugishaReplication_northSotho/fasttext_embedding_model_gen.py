import fasttext

'''
train skipgram fasstext embeddings using corpus
'''

file = './DataFiles/nSotho_clean_corpus.txt'

model = fasttext.train_unsupervised(file, model='skipgram', minn=2)

model.save_model('nSotho_fasttext_embeddings.bin')