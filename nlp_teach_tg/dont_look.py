import nltk
import sys
from bs4 import BeautifulSoup
from urllib import request
from nltk import word_tokenize
from nltk.probability import FreqDist


nltk.corpus.gutenberg.words




>>> fdist1 = FreqDist(t)



def main ():
    url = sys.argv[1]
    html = request.urlopen(url).read()
    raw = BeautifulSoup(html, 'html.parser').get_text()

    print (html)

    #tokens = word_tokenize(raw)
    #text = nltk.Text (tokens)



    #words = [w.lower() for w in text]
    #print (sorted(set(words)))


if __name__ == '__main__':
    main()
