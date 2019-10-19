import sys
import nltk

from nltk.corpus import opinion_lexicon
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

from nltk.corpus import stopwords as sw

def main():
    word_data = get_sent()
    sent_obj = analyze(word_data)
    sentence = sent_obj["sentence"]
    translator = sent_obj["tree"]
    result = hypo_explode (sentence,translator)

    return result


def get_sent ():
        corpus_root = 'dict'
        # corpus_root = '/Users/abirqasem/nlp/dict'
        sentence = PlaintextCorpusReader(corpus_root, 'test3.txt')
        words = sentence.words()
        result = {"sentence": sentence, "words": words}
        return result

def create_keys(translator):
    result = {}
    for item in translator:
        result[item] = len(translator[item])
    return result

def hypo_explode (sent,translator):
    sents = ""
    result = []
    sent_result = sent

    trans_key = create_keys(translator)
    sent = sent.split(" ")
    result.append(sent_result)

    for item in sent:
        if len(translator[item]) != 0:
            count = 0
            while count < len(translator[item]):

                new_val = sent_result.replace(item,str(translator[item][count]))
                result.append(new_val)

                for key in trans_key.keys():

                    if key != item and trans_key[key] > 0:
                        for i in range(0,len(translator[key])):
                            result.append(new_val.replace(key,translator[key][i]))

                if len(translator[sent[(sent.index(item))]]) > 0:
                    result.append(new_val.replace(sent[(sent.index(item))],translator[sent[(sent.index(item))]][0]))

                count = count+1

    result = set(result)
    return result


def analyze (sentence_object):
    final_obj = {}
    words = sentence_object["words"]
    sentence = " ".join(sentence_object["sentence"].sents()[0])

    positions = {}
    #lean_words = words
    result = {}

    for word in words:
        positions[word] = words.index(word)

    for word in words:
        content = wn.synsets(word,pos="n") #n stands for noun, and a for adjective
        if len(content) > 0:

            hypos = content[0].hyponyms()

            temp = []
            for hypo in hypos:
                temp.append(hypo.lemmas()[0].name())
            result[word] = temp

        else:
            result[word] = []
    final_obj["tree"] = result
    final_obj["sentence"] = sentence

    return final_obj




if __name__ == '__main__':
    print(main())

    #sent1 = "Assign the Variable to a constant"
    #translator1 = {"Assign": ["Set value"], "the":[], "to":[], "a":[], "Variable":["memory location", "letter"], "constant": ["number", "fixed number"]}
