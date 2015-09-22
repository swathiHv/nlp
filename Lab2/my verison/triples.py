from generate_vocab import *
from word_pairs import *

tokens = getTokens('clean_tweets.txt')
word_pairs = getWordPairs()
vocab = getVocab(tokens)

for word in vocab:
    for tok in tokens:
        if( word == tokens ):
            if( word in uni_count ):
                uni_count[word] += 1
            else:
                uni_count[word] = 1
for sent in corpus:
    sent.insert( 0, '<s>' )
    sent.append( '<s>' )

T = dict()
for sent in corpus:
    for it in range( 1, len(sent)-1 ):
        t = ( sent[it-1], sent[it], sent[it+1] )
        if( t is in T.keys() ):
            T[t] += 1
        else:
            T[t] = 1

scores = dict()
for pairs in word_pairs:
    D = 0
    Z = 0
    for t1 in T:
        if( pairs[0] == t1[1] ):
            for t2 in T:
                if( pairs[1] == t2[1] and t1[0] == t2[0] and t1[2] == t2[2] ):
                    Z += T[t1] + T[t2]
                    D += abs( T[t1] - T[t2] )
    scores[pairs] = 1-(D/Z)

