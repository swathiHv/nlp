from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize,word_tokenize
from gensim.models.word2vec import *

def corpus_tokenize():
    f = open('Unified_corpus','r')
    tokenizer = RegexpTokenizer(r'[\w\d]+')
    tokenized_list = [word_tokenize(i.lower()) for i in sent_tokenize(f.read())]
    return tokenized_list

def word_rep(sentences,size):
    model = Word2Vec(size=size, sentences=sentences, window=10, sg=1)
    model.save('word_rep'+str(size))

if __name__ == '__main__':
    sentences = corpus_tokenize()
    size  = int(raw_input("Enter size"))
    word_rep(sentences,size)
