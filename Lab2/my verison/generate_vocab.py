from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize,sent_tokenize
import pickle

def unigram_count(tokens):
	unigram = {}
	print "Calculating unigram counts"
	for j in tokens:
		for i in j:
			if i in unigram.keys():
				unigram[i]+=1
			else:
				unigram[i]=1
	return unigram

def getTokens(corpus):
	f = open(corpus,'r')
	tokens = []
	tokenizer = RegexpTokenizer(r'[\w\d]+')
	print "Tokenizing"
	for i in sent_tokenize(f.read()):
		tokens.append(['<s>']+tokenizer.tokenize(i)+['</s>'])
	return tokens

def getVocab(tokens,threshold):
	vocab = []
	replace = []
	unigram = unigram_count(tokens)
	'''
	print "Comparing unigram counts with threshold"
	for word,count in unigram.items():
		if count < threshold:
			#replace all words in tokens with special symbol
			replace.append(word)
	print "Replacing tokens with special symbol"
	for i in range(len(tokens)):
		for j in range(len(tokens[i])):
			if tokens[i][j] in replace:
				tokens[i][j] = '__UNK__'
	print "Creating vocab after applying threshold"
	for i in range():
		vocab.extend(tokens)
	'''
	
	return list(set(vocab))

if __name__ == '__main__':
	corpus = raw_input("Enter corpus to create vocab:")
	threshold = raw_input("Enter unigram threshold:")
	vocab = getVocab(getTokens(corpus),threshold)
	cpickle.dump(vocab,open('vocab.p','w'))