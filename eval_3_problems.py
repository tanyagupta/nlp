import sys
import nltk

from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import wordnet as wn
from nltk import word_tokenize
from nltk.corpus import abc as abc
from nltk.corpus import gutenberg as gutenberg
from nltk.corpus import brown as brown
from nltk.corpus import PlaintextCorpusReader

dicts = {}
dicts["abc"] = abc
dicts["brown"] = brown
dicts["gutenberg"] = gutenberg
dicts["wn"] = wn

def read_file(file_path,file_name):


    text = PlaintextCorpusReader(file_path,file_name)
    sents = text.sents()
    words = text.words()
    text_complexity_score(words,sents,file_name)


def words_sents_maker(corpus,source):
    sents_source = corpus.sents(source);
    words_source = corpus.words(source)
    text_complexity_score(words_source,sents_source,source)


def text_complexity_score(words,sents,source):
    len_letters= []
    for word in words:
        len_letters.append(len(list(word)))

    sum_letters = sum(len_letters)
    len_letters = len(len_letters)
    avg_letters = sum_letters/len_letters


    len_sentences = []
    for sentence in sents:
        len_sentences.append(len(sentence))
    sum_sentences = sum(len_sentences)
    len_sentences = len(len_sentences)
    avg_sentences = sum_sentences/len_sentences

    # print ('the sum of sentence lengths is: {}'.format(sum_sentences))
    # print('the length of sentences is: {}'.format(len_sentences))
    # print('the average number of words per sentence is: {}'.format(avg_sentences))

    text_complexity_score = 4.71 * avg_letters + .5 * avg_sentences - 21.43
    print('the Automated Readability Index of {} is: {}'.format(source,text_complexity_score))

    # Obtain raw texts from two or more genres and compute their respective reading
    #difficulty scores as in the earlier exercise on reading difficulty.
    #E.g. compare ABC Rural News and ABC Science News (nltk.corpus.abc).
    # Use Punkt to perform sentence segmentation
    #Let us define μw to be the average number of letters per word, and μs to be the average number of
    #words per sentence, in a given text. The Automated Readability Index (ARI) of the text is
    #defined to be: 4.71 μw + 0.5 μs - 21.43.
    return text_complexity_score



if __name__ == '__main__':

# This area is for testing out corpora
    corpus = dicts["abc"]
    source='rural.txt'
    words_sents_maker(corpus,source)

    source='science.txt'
    words_sents_maker(corpus,source)

    corpus = dicts["gutenberg"]
    source = 'austen-persuasion.txt'
    words_sents_maker(corpus,source)

    source = 'whitman-leaves.txt'
    words_sents_maker(corpus,source)

# This area is for testing out files
    file_path = '/Users/abirqasem/nlp/dict'
    file_name = 'text_compl_easy.txt'
    read_file(file_path,file_name)

    file_name = 'text_compl_medium.txt'
    read_file(file_path,file_name)

    file_name = 'text_compl_hard.txt'
    read_file(file_path,file_name)



    # samples http://www.impact-information.com/scales.pdf
