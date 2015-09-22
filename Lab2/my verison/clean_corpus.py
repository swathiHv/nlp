from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize,word_tokenize
from gensim.models.word2vec import *
import re
from stemming.porter2 import stem
import pickle

def clean_corpus(in_corpus,out_corpus): 	
	tokens = []
	vocab = []
	f = open(in_corpus,'r')
	out = open(out_corpus,'w')
	hashtag = r'#\w[\w\d]*'
	#url = r'(\w+)://(([\w\d]*)\.)?([\w\d]+)\.([\w\d]+)(:\d+)?(\/[\w\d]+)+(\?(\w[\w\d]*=[\w\d]+&?)+)?(#[\w\d]+)?'
	#stupid_url = r'(https?)?://[\S+]?'
	stupid_url = r'(https?)?://([^\s+]+)?'
	screen_name = r'@\S+'
	html = r'&\S+;'
	emoticon = r'[:;B8][-][DP\)\(]' 
	for j in sent_tokenize(f.read()):
		for i in j.split():
			if re.search(hashtag,i)  or re.search(stupid_url,i) or re.search(screen_name,i) or re.search(r'RT',i) or re.search(emoticon,i) or re.search(html,i):
				out.write("")	
			else:
				#write out stem of
				out.write(stem(i.lower())+" ")
	out.close()
	f.close()
	

if __name__ == '__main__':
	clean = raw_input("Clean corpus?(y/n):")
	in_corpus = raw_input('Enter input corpus filename:')
	clean_corpus(in_corpus,'clean_tweets.txt')
