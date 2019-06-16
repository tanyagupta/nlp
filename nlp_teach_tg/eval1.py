import nltk
import matplotlib
from nltk.probability import FreqDist

def get_books():
    return nltk.corpus.gutenberg.fileids()

def get_fds():
    fds={}
    file_ids=nltk.corpus.gutenberg.fileids()
    for id in file_ids:
        fds[id] = FreqDist(nltk.corpus.gutenberg.words(id))
    return fds

def call_me (p1,p2):
    s = p1 * p2
    return s

def sent_fd():
    result = []
    sents = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
    for item in sents:
        result.append(len(item))

    fd = FreqDist(result)
    return fd


def assignment3():
    drop_words=[]

    word_list = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
    #print(word_list)
    fd = FreqDist(word_list)

    most_common = sorted(fd.most_common(100))
    # the need for this extra step is because one would like to have dropwords that have a high frequency. If you have a dropword that only occurs once, then it is not worth it to drop it
    # Without this however you could simply create the dropwords from word_list instead of creating an fd of the most_common
    for word in most_common:
        if len(word[0])<=3:
            drop_words.append(word[0])
    clean = [word for word in word_list if word not in drop_words]

    new_fd = FreqDist(clean)

    return new_fd


def main ():
    print(sent_fd().most_common(10))
    #print(assignment3().most_common(10))
    # fds = get_fds()
    # for fd in fds:
    #     print(fd+" \n: "+str(fds[fd].most_common(20)))

if __name__ == '__main__':
    main()
