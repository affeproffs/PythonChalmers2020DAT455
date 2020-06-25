from wordfreq import *
from sys import argv

def main():
    stopWords = [w.strip() for w in open(argv[1]).readlines()]
    tokens = tokenize(["".join(w.strip() + " " for w in open(argv[2]).readlines())])
    printTopMost(countWords(tokens, stopWords), int(argv[3]))

main()
