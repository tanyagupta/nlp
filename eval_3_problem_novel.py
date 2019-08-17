import sys
import nltk
import re
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import gutenberg as gutenberg
from nltk.corpus import wordnet as wn

def read_file(file_path):

    file_content_as_string = " "

    try:
        file_handle = open(file_path, "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return (file_content_as_string)
    except IndexError:
        print ("No file name to read")

##########################################################################################################
# NEXT STEPS: Find the concordance of the word, that is what words it is used next to
# then find the synsets of those neigboring words
#then see how similar the two sets of synsets are
##########################################################################################################
#Write a program that processes a text and discovers cases where a word has been used with a novel sense.
#For each word, compute the WordNet similarity between all synsets of the word and all synsets of the words
#in its context. (Note that this is a crude approach; doing it well is a difficult, open research problem.)
##########################################################################################################

def get_novel(text):

    tokens = word_tokenize(text)
    tokens = set(remove_stopwords(tokens))

    textList = Text(tokens)

    cc_words = {}
    result = []

    #textList.concordance('is')
    # for token in tokens:
    #     c = nltk.ConcordanceIndex(textList.tokens, key = lambda s: s.lower())
    #     print([textList.tokens[offset+1] for offset in c.offsets(token)])

    #for token in tokens:
    #    result.append(textList.concordance(token))


    res=[]
    for word in textList:
        con_list = textList.concordance_list(word)
        #print(con_list)
        for item in con_list:
            temp = {}
            #print(item)
            # Removing the numbers and space and punctuation
            # Creating a new dictionary that has the word, one word on the right and one word on the left
            if len(word) >1:
                #print(word)
                word = re.sub(r'[^\w\s]','',word)
                word = re.sub(r'[0-9]','',word)
                print(word)
                temp["word"] = word
            else:
                temp["word"] =""
            if len(item.left) >1:

                left = str(item.left[0])
                left = re.sub(r'[^\w\s]','',left)
                left = re.sub(r'[0-9]','',left)
                temp["left"] = left
            else:
                temp["left"] =""
            if len(item.right) >1:
                right = str(item.right[0])
                right = re.sub(r'[^\w\s]','',right)
                right = re.sub(r'[0-9]','',right)
                temp["right"] = right
            else:
                temp["right"] =""
            res.append(temp)

    all_synsets = []
    items =res

    #print(items)

    for item in items:
        #print(wn.wup_similarity(all_synsets[0], all_synsets[1]))
        #print(item)
        word_synsets = [wn.synsets(item["word"])]
        if len(word_synsets) >0:
            word_synsets = word_synsets[0]
            #print(wn.wup_similarity(word_synsets[0][0],word_synsets[0][1]))
            for synset in word_synsets:
                #print('The word is {} and the words on the right are {} and the similarity is {}'.format(synset.lemmas()[0].name(),wn.synsets(item["right"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["right"][0])[0])))
                #print(item["word"])
                if len(item["left"]) >0 and len(wn.synsets(item["left"])) > 0 and len(wn.synsets(item["word"])) > 0 :
                    #all_synsets.append([synset.lemmas()[0].name(),wn.synsets(item["left"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["left"][0])[0])])
                    all_synsets.append([item["word"],item["left"],wn.wup_similarity(synset,wn.synsets(item["left"][0])[0])])
                if len(item["right"]) >0 and len(wn.synsets(item["right"])) > 0 and len(wn.synsets(item["word"])) > 0 :
                    #all_synsets.append([synset.lemmas()[0].name(),wn.synsets(item["right"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["right"][0])[0])])
                    all_synsets.append([item["word"],item["right"],wn.wup_similarity(synset,wn.synsets(item["right"][0])[0])])
    vals=[]
    result= []
    for item in all_synsets:
        if item[2] != None:
            vals.append([item[0],item[1]])
        else:
            result.append([item[0],item[1]])
    result = [list(v) for v in dict(result).items()]
    print(result)
    return result


def is_unusual_word(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

def remove_stopwords(text_set):
    result = []
    stopwords = nltk.corpus.stopwords.words('english')
    #content = [w for w in text if w.lower() not in stopwords]
    for word in text_set:
        if word.lower() not in stopwords:
            result.append(word)

    return result


if __name__ == '__main__':
    file_path = '/Users/abirqasem/nlp/dict'
    file_name = 'text_compl_hard.txt'
    #text = read_file("dict/para2.txt")
    text = read_file("dict/text_compl_hard.txt")
    #text = read_file("dict/bicycle_thief.txt")
    get_novel(text)
    #print(text)


#http://www.nltk.org/howto/wordnet.html
#http://www.nltk.org/howto/corpus.html#common-corpus-reader-methods
#http://www.nltk.org/nltk_data/
