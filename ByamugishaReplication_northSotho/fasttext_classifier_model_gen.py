import fasttext

'''
Train fasttext classifer using labelled corpus
'''

model = fasttext.train_supervised(input="./DataFiles/nSotho_labelled_corpus.txt",pretrainedVectors='./ModelsAndVectors/nSotho_noun_vectors.vec', minn=2)
model.save_model("nSotho_fasttext_classifer.bin")

    