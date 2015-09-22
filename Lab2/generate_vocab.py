from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize,sent_tokenize
import pickle

def unigram_count(tokens):
	stop_words = [ 'a', 'an','are','be','at', 'by','he', 'its', 'on','were','with','the', 'is', 'and', 'in', 'to', 'from', 'of','it','for','that','this','as', 'will', 'has', 'had', 'was' ]
	unigram = {}
	print "Calculating unigram counts"
	for sent in tokens:
		for word in sent:
			if( word in stop_words ):
				continue
			if word in unigram.keys():
				unigram[word]+=1
			else:
				unigram[word]=1
	return unigram

def getTokens(corpus):
	f = open(corpus,'r')
	tokens = []
	tokenizer = RegexpTokenizer(r'[\w\d]+')
	print "Tokenizing"
	for i in sent_tokenize(f.read()):
		tokens.append(tokenizer.tokenize(i))
	return tokens

def getVocab(tokens):
	unigram = unigram_count(tokens)
	sorted_unigram = sorted(unigram, key=unigram.get ).keys()[::-1]
	pickle.dump(sorted_unigram,open('sorted_unigram.p','w'))
	vocab = sorted_unigram

if __name__ == '__main__':
	corpus = raw_input("Enter corpus to create vocab:")
	threshold = raw_input("Enter unigram threshold:")
	tokens = getTokens(corpus)
	pickle.dump(tokens, open('tokens.p','w'))
	exit()
	vocab = getVocab( tokens )
	pickle.dump(vocab,open('vocab.p','w'))
