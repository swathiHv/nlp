from gensim.models.word2vec import *

if __name__ == '__main__':
    file_name = raw_input("Enter model file name:")
    model = Word2Vec.load(file_name)
    word_pairs = [ ('india', 'narendra'), ('indian', 'uae'), ('pm', 'dubai'), ('modi', 'namo'), ('temple', 'mosque'), ('congress','dubai'), ('dhabi','bhakt'), ('sardesai','dubai'), ('modi','pm') ]
    for i in word_pairs:
        try:
            print i,':',model.similarity( w1, w2 )
        except:
            print "Key not found"
