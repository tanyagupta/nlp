import nltk
from nltk.util import bigrams
from nltk.corpus import genesis
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader


def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)


def generate_model_your_own(cfdist, word, num=20):
     for i in range(num):
         print(word, end=' ')
         word = cfdist[word].max()

corpus_root = '/Users/abirqasem/nlp/dict'
text = PlaintextCorpusReader(corpus_root, 'bicycle_thief.txt').words()


#sents = bith.sents()
#a_sent= bith.sents(fileids='bicycle_thief.txt')[19]

bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(words)
#print(sents)



    #bgram = bith.bigrams(words)
    #print(bgram)
    #print(wordlists.fileids())
    #text = wordlists.words('bicycle_thief.txt')
    #print(wordlists)

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

def puzzle(puzzle):
    puzzle_letters = nltk.FreqDist(puzzle)
    obligatory = 'r'
    wordlist = nltk.corpus.words.words()
    result = [w for w in wordlist if len(w) >= 6 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters]
    return result

def male_female_names():
    names = nltk.corpus.names
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')
    androgyn_names = [w for w in male_names if w in female_names]
    return androgyn_names

def rhyme(syllable):
    entries = nltk.corpus.cmudict.entries()
    a_list = [word for word, pron in entries if pron[-4:] == syllable]
    return a_list

def stress():
    entries = nltk.corpus.cmudict.entries()
    res = [w for w, pron in entries if [char for phone in pron for char in phone if char.isdigit()] == ['0', '1', '0', '2', '0']]
    return res

def main ():
    print(generate_model_your_own(cfd, 'bike'))
    #print(stress())
    #print(rhyme(['N', 'IH0', 'K', 'S']))
    #print(male_female_names())
    #print(puzzle('egivrvonl'))
    #print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
    #print(stop())
    #print (plural('fairy'))
    #print(cfd['living'])
    #generate_model(cfd, 'living')

if __name__ == '__main__':
    main()
