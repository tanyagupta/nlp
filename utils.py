import nltk
from nltk.corpus import wordnet as wn
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

def sim_syns(text):
    all_synsets = []
    for synset in (wn.synsets(text)):
        all_synsets.append(synset)


    result = []
    length = len(all_synsets)
    for synset in all_synsets:
        count = 0
        while count < length-1:
            temp = []
            temp.append(all_synsets[count])
            temp.append(all_synsets[count+1])
            result.append(temp)
            count = count + 1

    result = [list(v) for v in dict(result).items()]
    for item in result:

        print('The similarity of {} and {} is: {}'.format(item[0].lemma_names()[0],item[1].lemma_names()[0],wn.wup_similarity(item[0],item[1])))



def lemma_names(item):
    lems = {}
    lems["word"] = item
    content = str(item)+".n.01"
    lemmas = wn.synset(content).lemma_names()
    lems["lemmas"] = lemmas
    temp=[]
    for synset in wn.synsets(item):
        temp.append(synset.lemma_names()[0])
    lems["lemma_names"] = temp
    return lems

def comp_sims(word1,word2):
    sims = {}
    sims["noun1"] = word1
    sims["noun2"] = word2
    noun1 = wn.synset(word1+'.n.01')
    noun2 = wn.synset(word2+'.n.01')
    sims["path_similarity"] = noun1.path_similarity(noun2)
    sims["lch_similarity"] = noun1.lch_similarity(noun2)
    sims["wup_similarity"] = noun1.wup_similarity(noun2)
    #porter = nltk.PorterStemmer()
    return sims

    #textList.concordance('is')
    # for token in tokens:
    #     c = nltk.ConcordanceIndex(textList.tokens, key = lambda s: s.lower())
    #     print([textList.tokens[offset+1] for offset in c.offsets(token)])

    #for token in tokens:
    #    result.append(textList.concordance(token))


def main ():
    print(comp_sims("dog","cat"))
    #print(lemma_names("dog"))
    #sim2()
    #sim_syns("dog")
    #print(generate_model_your_own(cfd, 'bike'))
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
