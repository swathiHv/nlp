from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize,sent_tokenize
import pickle

def getTriples(corpus):
    f = open(corpus,"r")

