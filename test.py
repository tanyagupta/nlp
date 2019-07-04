import nltk
from nltk.corpus import genesis
from nltk.corpus import stopwords

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

def stop():
    return stopwords.words('english')

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

def main ():
    #print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
    print(stop())
    #print (plural('fairy'))
    #print(cfd['living'])
    #generate_model(cfd, 'living')

if __name__ == '__main__':
    main()
