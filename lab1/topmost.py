from wordfreq import *
from sys import argv
import urllib.request

def main():
    if("http://" in argv[2][:7] or "https://" in argv[2][:8]):
        lines = urllib.request.urlopen(argv[2]).read().decode("utf8").splitlines()
    else:
        lines = open(argv[2]).readlines() # Scopes in python? OMEGALUL

    tokens = tokenize(["".join(w.strip() + " " for w in lines)])        
    stopWords = [w.strip() for w in open(argv[1]).readlines()]
    printTopMost(countWords(tokens, stopWords), int(argv[3]))

main()
