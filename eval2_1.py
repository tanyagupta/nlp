import sys
import nltk

from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import wordnet as wn





def main ():

    file_content_as_string = " "

    try:
        file_handle = open("dict/para2.txt", "r")
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
    all_negative_words = []
    postive_result = []
    text_set = (string.split())
    num_words = len (text_set)
    clean_words = text_set
    opinion_words = opinion_lexicon.negative()
    #clean_words = ["stupid","afraid"]
    for item in clean_words:
        if item in opinion_words:
            count = count + 1
            new_word = make_positive(item)
            if new_word != item: # i.e. if the word was changed successfully
                negative_words.append(item)
            postive_result.append(new_word)
            all_negative_words.append(new_word)


        else:
            postive_result.append(item)
    result['negative_score'] = (count / num_words )*100
    positive_text = " ".join(postive_result)
    result['original_text'] = string
    result['positive_text'] = positive_text
    result['all_negative_words'] = set(all_negative_words)
    result['count'] = count
    result['num_words'] = num_words
    result['replaced_negative_words'] = set(negative_words)
    print(result)





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
