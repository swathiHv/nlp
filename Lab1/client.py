from gensim.models.word2vec import *

if __name__ == '__main__':
    file_name = raw_input("Enter model file name:")
    model = Word2Vec.load(file_name)
    try:
        w1 = raw_input("Enter word1 : ").lower()
   
        w2 = raw_input("Enter word2 : ").lower()

        print "Similarity : "
        print model.similarity( w1, w2 )

        print "Get most similar words for a given set of words"
        pos = [i.lower() for i in eval(raw_input("Enter positive similaities : "))]
        neg = [i.lower() for i in eval(raw_input("Enter negative similarities : "))]
        print "Most similar word : "
        print model.most_similar( pos, neg )
    except:
        print "Key not found"
