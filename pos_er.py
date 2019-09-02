from stanfordnlp.server import CoreNLPClient
import nltk
import os
os.environ["CORENLP_HOME"] = r'/Users/abirqasem/stanford-corenlp-full-2018-10-05'


def readText ():

    file_content_as_string = " "

    try:
        file_handle = open("dict/sentence.txt", "r")
        file_content_as_string = file_content_as_string.join(file_handle.readlines())
        file_handle.close ()
        return (file_content_as_string)
    except IndexError:
        print ("No file name to read")

def getAnalysis(props):
    result={}
    for item in props:
        #print(item)
        if len(item["ner"]) > 1:
            print("There is a reference to {} in the word {}".format(item["ner"],item["word"]))
            if item["ner"] == "PERSON":
                result["replace"] = True
                result["type"] = "PERSON"
                result["wordToReplace"] = item["word"]
            if item["ner"] == "LOCATION":
                result["replace"] = True
                result["type"] = "LOCATION"
                result["wordToReplace"] = item["word"]
    return result


def runClient(text):
    print('---')
    print('starting up Java Stanford CoreNLP Server...')
    # set up the client
    #with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','natlog','openie'], properties={"outputFormat": "json","openie.triple.strict":"true","splitter.disable" : "true","openie.max_entailments_per_clause":"1"}, be_quiet=False, timeout=30000, memory='16G') as client:
    with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','natlog','openie'], be_quiet=True, timeout=30000, memory='16G') as client:
        # submit the request to the server
        # Iterate over all tokens in all sentences, and print out the word, lemma, pos and ner tags
        text = "Trump is the President of America"
        document = client.annotate(text)
        output = client.annotate(text, properties={"outputFormat": "json",
                                 "openie.triple.strict":"true",
                                 "splitter.disable" : "true",
                                 "openie.max_entailments_per_clause":"1"})
        #print(output)
        result = [output["sentences"][0]["openie"] for item in output]
        print(result)
        print(result[0][0]["subject"])
        # [[{'subject': 'John', 'subjectSpan': [0, 1], 'relation': 'jumps over', 'relationSpan': [1, 3], 'object': 'fox', 'objectSpan': [4, 5]}]]
        for i in result:
            for rel in i:
                relationSent=rel['relation'],rel['subject'],rel['object']
                print(relationSent)
        # print("{:12s}\t{:12s}\t{:6s}\t{}".format("Word", "Lemma", "POS", "NER"))
        tags = getTags()
        # #print(document.sentence)
        props = []
        for key,value in enumerate(document.sentence):
            for t in value.token:
                props.append({"word":t.word,"lemma":t.lemma,"pos":t.pos,"pos_full":tags[t.pos],"ner":t.ner})
                #print("Word: {}, Lemma: {}, POS: {}, NER: {}".format(t.word,t.lemma,tags[t.pos],t.ner))

        replaceWord = getAnalysis(props)
        if replaceWord["replace"] and replaceWord["type"] == "PERSON":
            text = text.replace(replaceWord["wordToReplace"],"who")+" ?"
            print(text)
        if replaceWord["replace"] and replaceWord["type"] == "LOCATION":
            #text = ''.join("Where is ",relationSent["subject"]," ?")
            print("Where is {} ?".format(replaceWord["wordToReplace"]))
        # for i, sent in enumerate(document.sentence):
            # print("[Sentence {}]".format(i+1))
            # for t in sent.token:
            #     print("{:12s}\t{:12s}\t{:6s}\t{}".format(t.word, t.lemma, t.pos, t.ner))
            # print("")
        # Iterate over all detected entity mentions
        # print("{:30s}\t{}".format("Mention", "Type"))

        # for sent in document.sentence:
        #     for m in sent.mentions:
                # print("{:30s}\t{}".format(m.entityMentionText, m.entityType))

        # Print annotations of a token
        # print(document.sentence[0].token[0])

        # Print annotations of a mention
        # print(document.sentence[0].mentions[0])



def getTags():
    tags = nltk.data.load('help/tagsets/upenn_tagset.pickle')
    #print("{:30s}\t{}{}".format("Abbrev.", "POS", "Example"))
    result = {}
        #print("{:30s}\t{}".format(item, tags[item][0]))
    for item in tags:
        result[item] = tags[item][0]
    return result


if __name__ == '__main__':
    #text = "Chris Manning is a nice person."
    text = readText()
    #print(text)
    runClient(text)
    #print(getTags())



#reference: https://stackoverflow.com/questions/37375137/stanford-corenlp-openie-annotator
