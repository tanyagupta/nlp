import nltk
from nltk.corpus import nps_chat as nps_chat
from nltk import word_tokenize
from nltk.data import load
tagdict = load('help/tagsets/upenn_tagset.pickle')
from nltk.corpus import names
import random
from nltk.corpus import movie_reviews
from nltk.stem.wordnet import WordNetLemmatizer
import spacy


short_tagdict = {}
for item in tagdict:
        short_tagdict[item] = tagdict[item][0]

#print (short_tagdict)
sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the','sounds', 'will', 'take', 'care', 'of', 'themselves', '.']


def extract_property(prop):
    return [prop(word) for word in sent]

def last_letter(word):
    return word[-1]

def permutations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + seq[0:1] + perm[i:]

def gender_features(word):
    vcount =0
    ccount=0
    vowels = ['a','e','i','o','u']
    for letter in word:
        if letter.lower() in vowels:
            vcount=vcount+1
        else:
            ccount = ccount+1
    result = {'last_letter': word[-1].lower(),'scndlstlttr': word[-2],'first_letter' : word[0].lower(), 'consonant_count':ccount/len(word)}
    return result

def class_name():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(labeled_names)
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(classifier.classify(gender_features('Neo')))
    print(nltk.classify.accuracy(classifier, test_set))
    print(classifier.show_most_informative_features(10))

def modify(inputStr):

    tokens =  word_tokenize(inputStr)
    tagged = nltk.pos_tag(tokens)
    #print(tagdict)

    #print(tagdict[tagged[0][1]][0])

    # auxiliary_verbs = [i for i, w in enumerate(tagged) if w[1] == 'VBP']
    # if auxiliary_verbs:
    #     tagged.insert(0, tagged.pop(auxiliary_verbs[0]))
    # else:
    #     tagged.insert(0, ('did', 'VBD'))
    # tagged.insert(0, ('When', 'WRB'))
    #
    # return ' '.join([t[0] for t in tagged])


def use():
    #question_one = 'The Knights Templar are founded to protect Christian pilgrims in Jerusalem.'
    #question_two = 'Alfonso VI of Castile captures the Moorish Muslim city of Toledo, Spain.'

    question_one = 'I went home to collect my keys.'
    question_two = 'George won the race.'

    question_one = modify(question_one)
    #question_two = modify(question_two)

    #print(question_one)
    #print(question_two)


def document_features(document):
    document_words = set(document)
    movie_features = {}
    for word in movie_word_features:
        movie_features['contains({})'.format(word)] = (word in document_words)
        #features[word] = word in document_words

    return movie_features

def get_movie_words():
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    movie_words = list(all_words)[:2000]
    return movie_words

def movies():
    documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)

    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    print(classifier.show_most_informative_features(50))

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
        #features[word.lower()] = True



def classify_text():
    posts = nps_chat.xml_posts()[:10000]
    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    #print(nltk.classify.accuracy(classifier, test_set))
    print(classifier.classify(dialogue_act_features("how are you, my sweet cat?")))
    print(classifier.classify(dialogue_act_features("Shut up and get out")))
    print(classifier.classify(dialogue_act_features("You are the most wonderful thing in my life")))
    print(classifier.classify(dialogue_act_features("I loved the movie")))
    print(classifier.classify(dialogue_act_features("How many suns does Jupitor have")))
    print(classifier.classify(dialogue_act_features("Do you love me?")))
    # https://stackoverflow.com/questions/49100615/nltk-detecting-whether-a-sentence-is-interogative-or-not
    # The dialogue-act tags are Accept, Bye, Clarify, Continuer, Emotion, Emphasis, Greet, No Answer, Other, Reject, Statement, System, Wh-Question, Yes Answer, Yes/No Question.
    # http://faculty.nps.edu/cmartell/NPSChat.htm
    #



def spacy_basic_test():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)

if __name__ == '__main__':
    #print(extract_property(last_letter))
    #print(list(permutations(['police', 'fish', 'buffalo'])))
    #classify_text()
    #use()
    #class_name()
    #print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

    movie_word_features = get_movie_words()
    movies()
    #spacy_basic_test()




# good definition of generator function
# https://mail.google.com/mail/u/0/#search/hopsy/FMfcgxwChmJWMWgSqDLrMQTNqLpXnPDw
