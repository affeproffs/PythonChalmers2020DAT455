import re

def tokenize(lines):
    if not lines: return lines
    digits = re.compile('(\d+|[^\w\s])').sub(r' \1 ', lines[0].strip().lower())
    spaces = re.compile('(\s+)').sub(' ', digits)
    return list(filter(lambda w: w != '', spaces.split(" ")))
