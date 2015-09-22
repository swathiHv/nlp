'''tokens = getTokens()
word_pairs = getWordPairs()
vocab = getVocab()

uni_count = dict()
common_words = [ 'the', 'is', 'and', 'in', 'to', 'from', 'of','it','for','that','this','as', 'will', 'has', 'had', 'was' ]
for word in vocab:
    if( word in common_words ):
        continue
    for tok in tokens:
        if( word == tokens ):
            if( word in uni_count ):
                uni_count[word] += 1
            else:
                uni_count[word] = 1

subset_uni_count = (sorted(uni_count, key=uni_count.get )[1000]).keys()'''

def padSentences( corpus ):
    for sent in corpus:
        sent.insert( 0, '<s>' )
        sent.append( '<s>' )

def generateTriples( corpus ):
    T = dict()
    for sent in corpus:
        for it in range( 1, len(sent)-1 ):
            t = ( sent[it-1], sent[it], sent[it+1] )
            if( t in T.keys() ):
                T[t] += 1
            else:
                T[t] = 1
    return T

def getScores( word_pairs, T ):
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
        if( D is 0 and Z is 0 ):
            continue
        else:
            print D, Z
        scores[pairs] = float(1-(float(D)/float(Z)))
    return scores

