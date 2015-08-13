import math

def term_freq(t,d):
	term_freq = {}
	for list1 in d:
		for item in list1:
			if item not in term_freq.keys():
				count +=1
				term_freq[item] = 1
			else:
				term_freq[item] += 1
	return term_freq
	
def tf(t,d):
	freq = 0
	N = 0
	for list1 in d:
		N += len(list1)
		for item in list1:
			if item == t:
				freq+ = 1
	return freq/N
	
def idf(t,D):
		N = len(D)
		count = 0
		for f in D:
			tokenized_list = [word_tokenize(i) for i in sent_tokenize(f.read())]
			for list1 in tokenized_list:
				if t in list1:
					count += 1
					break
		
		return log(N/count,10) #can change the base to 2 or natural log
