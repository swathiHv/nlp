import cPickle as pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
import os 

def get_data(directory):
    data = []
    tokenizer = RegexpTokenizer(r'[\w\d\']+')
    print "Tokenizing"
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root,file),"r") as f:
                lines = f.read().split(".")
                for line in lines:
                    data.append(['*',"*"]+tokenizer.tokenize(line.decode('ascii', "ignore")))
    pickle.dump(data, open("data_new1.p","wb"))

if __name__ == "__main__":
    directory = "/home/benaka/nlp_class/Lab3/NDTV_mobile_reviews_Classified"
    get_data(directory)
