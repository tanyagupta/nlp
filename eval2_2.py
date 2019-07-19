import sys
import nltk

from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

from nltk.corpus import stopwords as sw



def main ():
        corpus_root = '/Users/abirqasem/nlp/dict'
        words = PlaintextCorpusReader(corpus_root, 'sentence.txt').words()
        return words



def analyze (words):
    #words = ["jump","dog"]
    positions = {}
    clean_words = words
    result = {}

    #stopwords = sw.words('english')
    #stopwords.append("the")


    for word in words:
        positions[word] = words.index(word)

        #if (not word.lower() in stopwords):
        #clean_words.append(word)



    for word in clean_words:
        content = wn.synsets(word,pos="n") #n stands for noun, and a for adjective
        if len(content) > 0:

            hypos = content[0].hyponyms()
            # if len(content) > 0:
            #     hypos = content[0].hyponyms()
            #     if len(hypos) != 0:
            #
            temp = []
            for hypo in hypos:
                temp.append(hypo.lemmas()[0].name())
            result[word] = temp

                # else:
                #     content = wn.synset(word+".a.01")
                #     hypos = content.hyponyms()
                #     if len(hypos) != 0:
                #         for word in hypos:
                #             print(word.lemmas()[0].name())
                #             print("adjective")
        else:
            result[word] = []
    #print(positions)
    #print(clean_words)
    print(result)

    #return len(content.hyponyms())




if __name__ == '__main__':

    words = main()
    analyze(words)
