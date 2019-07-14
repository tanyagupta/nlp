import sys
import nltk

from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import wordnet as wn





def main ():

    file_content_as_string = " "

    try:
        file_handle = open("dict/para.txt", "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return (file_content_as_string)
    except IndexError:
        print ("No file name to read")



def make_positive(item):

    pos_word = item
    content = str(item)+".a.01"



    if wn.synsets(item):
        if wn.synsets(item)[0].lemmas():
            if len(wn.synsets(item)[0].lemmas()[0].antonyms()) != 0:

                pos_word = wn.synsets(item)[0].lemmas()[0].antonyms()[0].name()
                #negative_count = negative_count + 1
    #print(pos_word)

    return pos_word

def analyze (string):
    count = 0
    #print(opinion_lexicon.words()[:4])
    result = {}
    negative_words = []
    positive_words = []
    postive_result = []
    text_set = (string.split())
    num_words = len (text_set)
    clean_words = text_set
    #clean_words = remove_stopwords(text_set)
    opinion_words = opinion_lexicon.negative()
    #print(clean_words)
    #clean_words = ["stupid","afraid"]
    for item in clean_words:
        if item in opinion_words:
            pos_word = make_positive(item)
            if pos_word == item:
                count = count + 1
            postive_result.append(pos_word)
            positive_words.append(pos_word)
            #negative_words.append(item)


        else:
            postive_result.append(item)
    result['negative_score'] = (count / num_words )*100
    positive_text = " ".join(postive_result)
    result['original_text'] = string
    result['positive_text'] = positive_text
    #print(full_sentence)
    #print(set(positive_words))
    print(result)
    #print(count)



def remove_stopwords(text_set):
    result = []
    stopwords = nltk.corpus.stopwords.words('english')
    #content = [w for w in text if w.lower() not in stopwords]
    for word in text_set:
        if word.lower() not in stopwords:
            result.append(word)

    return result


if __name__ == '__main__':

    string = main()
    analyze(string)
