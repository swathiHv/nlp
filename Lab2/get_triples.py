from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize,sent_tokenize
import pickle

unigram = {}
T = {}

def get_vocab(tokens):
    unigram = unigram_count(tokens)
    sorted_unigram = sorted(unigram, key=unigram.get ).keys()[::-1]
    pickle.dump(sorted_unigram,open('sorted_unigram.p','w'))
    vocab = sorted_unigram

def get_triples_tokens(corpus):

    stop_words = [ 'a', 'an','are','be','at', 'by','he', 'its', 'on','were','with','the', 'is', 'and', 'in', 'to', 'from', 'of','it','for','that','this','as', 'will', 'has', 'had', 'was' ]
    f = open(corpus,"r")
    tokens = []
    tokenizer = RegexpTokenizer(r'[\w\d]+')
    print "Tokenizing"
    for sentence in sent_tokenize(f.read()):
    	tok = ['<s>']+tokenizer.tokenize(sentence)+['</s>']
        for it in range(1,len(tok)-1):
            if tok[it] not in stop_words:

                if tok[it] in unigram.keys():
	            unigram[tok[it]]+=1
                else:
		    unigram[tok[it]]=1

            t = ( tok[it-1], tok[it], tok[it+1] )
            if( t in T.keys() ):
                T[t] += 1
            else:
                T[t] = 1
        tokens.append(tok)
    return tokens

if __name__ == '__main__':
    corpus = raw_input("Enter corpus to create vocab:")
    threshold = raw_input("Enter unigram threshold:")
    tokens = get_triples_tokens(corpus)
    pickle.dump(tokens, open('tokens.p','w'))
    vocab = get_vocab(tokens)
    pickle.dump(vocab,open('vocab.p','w'))
