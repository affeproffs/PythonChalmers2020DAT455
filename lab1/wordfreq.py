import re

def tokenize(lines):
    if not lines: return lines
    digits = re.compile('(\d+|[^a-zA-Z\s])').sub(r' \1 ', lines[0].strip().lower())
    spaces = re.compile('(\s+)').sub(' ', digits)
    return list(filter(lambda w: w != '', spaces.split(" ")))

def countWords(words, stopWords): return {w : words.count(w) for w in words if w not in stopWords}

def printTopMost(frequencies,n):
    for wf in list(sorted(frequencies.items(), key = lambda i: -i[1]))[:n]:
        print(wf[0].ljust(20) + str(wf[1]).rjust(5))
