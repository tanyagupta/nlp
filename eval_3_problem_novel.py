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



    porter = nltk.PorterStemmer()



    text = re.sub(r'\d+\[.,-*''?";:"][0-9]', '', text)
    # text = ' '.join(e for e in text if e.isalnum())

    tokens = word_tokenize(text)
    tokens = set(remove_stopwords(tokens))
    #tokens = ['affluent','women','housing']

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
        for item in con_list:
            temp={}
            temp["word"] = word
            temp["left"] = item.left
            temp["right"] = item.right
            res.append(temp)
        #print(res)


    #print(cc_words)
    #print(result)

    items = [{'word': 'affluent',
    'left': ['permits', '2,000', 'person', 'endless', '90', 'insisted', 'One', 'protester', 'new', 'pains', 'following', 'D.C.', 'provide', 'concerned', '1,500', 'homes', 'said', 'petition', 'jumped'],
    'right': ['one', 'emphasize', 'another', 'less', 'set', '1950', 'unanimously']},
    {'word': 'one',
    'left': ['Council', '?', 'Washington', '2010', 'planners', 'Minneapolis', '10', 'Montgomery', 'neighboring', 'hire', 'passed', 'protesters', 'Dale','permits','2,000','person', 'endless','90','insisted'],
    'right': ['protester', 'new', 'pains', 'following', 'D.C.', 'provide', 'concerned', '1,500', 'homes', 'said', 'petition', 'jumped', 'affluent', 'one', 'emphasize', 'another', 'less', 'set']}]

    all_synsets = []

    for item in items:
        #print(wn.wup_similarity(all_synsets[0], all_synsets[1]))
        #print(item)
        word_synsets = [wn.synsets(item["word"])]
        word_synsets = word_synsets[0]
        #print(wn.wup_similarity(word_synsets[0][0],word_synsets[0][1]))
        for synset in word_synsets:
            #print(synset)
            #print(wn.synsets(item["left"][0][0]))
            #print(item["word"])
            #print('The word is {} and the words on the left are {} and the similarity is {}'.format(synset.lemmas()[0].name(),wn.synsets(item["left"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["left"][0])[0])))
            #print('The word is {} and the words on the right are {} and the similarity is {}'.format(synset.lemmas()[0].name(),wn.synsets(item["right"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["right"][0])[0])))
            # print(synset.lemmas())
            # print(synset.lemmas()[0])
            # print(synset.lemmas()[0].name())
            # print(wn.synsets(item["left"]))
            # print(wn.synsets(item["left"][0]))
            # print(wn.synsets(item["left"][0])[0])



            #if len(synset.lemmas())>0 and len(synset.lemmas())>0 and wn.synsets(item["left"]) is not None:
            #    print(wn.synsets(item["left"]))
            all_synsets.append([synset.lemmas()[0].name(),wn.synsets(item["left"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["left"][0])[0])])

            # len_syn =  len(wn.synsets(item["left"][0]))
            # count = 0
            # while count < len_syn:
            #     #print(wn.synsets(item["left"][0][count]))
            #
            #     print('set:{}..{}..{}'.format(synset.lemmas()[0].name(),wn.synsets(item["left"][0])[count].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["left"][0])[count])))
            #
            #     all_synsets.append([synset.lemmas()[0].name(),wn.synsets(item["left"][0])[count].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["left"][0])[count])])
            #
            #     count = count+1
            #print(wn.synsets(item["left"]))

            #all_synsets.append([synset.lemmas()[0].name(),wn.synsets(item["right"][0])[0].lemmas()[0].name(),wn.wup_similarity(synset,wn.synsets(item["right"][0])[0])])
            #print(wn.wup_similarity(synset, wn.synsets(item["right"])))

    #all_synsets = set(all_synsets)
    #print(all_synsets)

    vals=[]
    result= []
    for item in all_synsets:
        if item[2] != None:
            vals.append([item[0],item[1]])
        else:
            result.append([item[0],item[1]])
    result = [list(v) for v in dict(result).items()]
    print(result)

    # for synset in (wn.synsets("dog")):
    #     all_synsets.append(synset)
    #
    #
    # result = []
    # length = len(all_synsets)
    # for synset in all_synsets:
    #     count = 0
    #     while count < length-1:
    #         temp = []
    #         temp.append(all_synsets[count])
    #         temp.append(all_synsets[count+1])
    #         result.append(temp)
    #         count = count + 1
    #
    # result = [list(v) for v in dict(result).items()]
    # for item in result:
    #
    #     print('The similarity of {} and {} is: {}'.format(item[0].lemma_names()[0],item[1].lemma_names()[0],wn.wup_similarity(item[0],item[1])))



    #print(wn.wup_similarity(all_synsets[0], all_synsets[1]))
    #print(wn.wup_similarity(wn.synset('bank.n.01'), wn.synset('bank.n.04')))




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
    text = read_file("dict/text_compl_hard.txt")
    #text = read_file("dict/bicycle_thief.txt")
    get_novel(text)
    #print(text)


#http://www.nltk.org/howto/wordnet.html
#http://www.nltk.org/howto/corpus.html#common-corpus-reader-methods
#http://www.nltk.org/nltk_data/
