from gensim.models.word2vec import *

if __name__ == '__main__':
    #file_name = raw_input("Enter model file name:")
    file_name = "word_rep128"
    model = Word2Vec.load(file_name)
    for i in range(10):
        try:
            w1 = raw_input("Enter word1 : ").lower()
   
            w2 = raw_input("Enter word2 : ").lower()

            print "Similarity : "
            print model.similarity( w1, w2 )
        except:
            print "Key not found"
