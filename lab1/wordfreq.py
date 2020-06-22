def tokenize(lines):
    if not lines:
        return []

    tokens = []
    word = ""
    for c in lines[0].lower():
        if not(c.isspace()):
            cType = "a" if c.isalpha() else "d" if c.isdigit() else "s"
            wType = "a" if word.isalpha() else "d" if word.isdigit() else cType if word == "" else "s"
            if(cType == wType):
                word += c
            else:
                tokens.append(word)
                word = c
        elif(word):
            tokens.append(word)
            word = ""
        
    return tokens + [word] if word else tokens

#print(tokenize(['10  S2we.et  Apple  Tarts.']))
