import sys
import nltk

from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader

def read_file(file_path,file_name):
    text = PlaintextCorpusReader(file_path,file_name)
    words = text.words()
    return text

##########################################################################################################
# NEXT STEPS: Find the concordance of the word, that is what words it is used next to
# then find the synsets of those neigboring words
#then see how similar the two sets of synsets are
##########################################################################################################
#Write a program that processes a text and discovers cases where a word has been used with a novel sense.
#For each word, compute the WordNet similarity between all synsets of the word and all synsets of the words
#in its context. (Note that this is a crude approach; doing it well is a difficult, open research problem.)
##########################################################################################################

def get_novel(words):
    # item = "car"
    # content = str(item)+".n.01"
    # lemmas = wn.synset(content).lemma_names()
    # for lemma in lemmas:
    #     print(lemma)
    # for synset in wn.synsets(item):
    #     print(synset.lemma_names())

    # dog = wn.synset('dog.n.01')
    # cat = wn.synset('cat.n.01')
    # print(dog.path_similarity(cat))
    #
    # print(dog.lch_similarity(cat))
    #
    # print(dog.wup_similarity(cat))
    all_synsets = []
    item = "car"
    content = str(item)+".n.01"
    for synset in (wn.synsets("dog")):
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



    #print(wn.wup_similarity(all_synsets[0], all_synsets[1]))
    #print(wn.wup_similarity(wn.synset('bank.n.01'), wn.synset('bank.n.04')))




def is_unusual_word(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)


if __name__ == '__main__':
    file_path = '/Users/abirqasem/nlp/dict'
    file_name = 'text_compl_hard.txt'
    text = read_file(file_path,file_name)
    get_novel(text)
    #print(text)


#http://www.nltk.org/howto/wordnet.html
#http://www.nltk.org/howto/corpus.html#common-corpus-reader-methods
#http://www.nltk.org/nltk_data/
