import pickle
import triples
T  = pickle.load( open( 'T.p','r' ) )
word_pairs = pickle.load( open( 'word_pairs.p','r' ) )
print triples.getScores( word_pairs, T )

