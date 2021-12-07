def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def replaceEscapeCode(word):
    if word == r'\b':
        return '\b'
    elif word == r'\t':
        return '\t'
    elif word == r'\n':
        return '\n'
    elif word == r'\a':
        return '\a'
    elif word == r'\r':
        return '\b'
    else:
        return word

def validDelimiter(word):
    # If len is just 1
    if len(word) == 1:        
        if not is_ascii(word):
            exit('Wrong delimiter!')
        else:
            return word
    # If len is 2, first character is \ and second isalpha()
    elif len(word) == 2 and word[0] == '\\' and word[1].isalpha():
        return replaceEscapeCode(word)
    else:
        exit('Wrong delimiter!')