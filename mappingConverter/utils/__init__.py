"""Library with generic tools to me used in taxam project.

Constants
---------
ROOT_PATH : str
    Root's absolute path.

Functions
---------
isAscii(s) : bool
    Check if all characters of this words are an ascii character.
replaceEscapeCode(word)
    Replace a str escape code for a real escape code.
validDelimiter(word)
    Check if word is a valid delimiter, like \\t, for instance.
"""
ROOT_PATH = __path__[0] + '/..'

def isAscii(word):
    """Check if all characters of this words are an ascii character.

    Parameters
    ----------
    word : str
        Word to be verified.

    Returns
    -------
    bool
        True if all characters are ascii characters,or false, if not..
    """
    return all(ord(character) < 128 for character in word)


def replaceEscapeCode(word):
    """Replace a str escape code for a real escape code.

    Parameters
    ----------
    word : str
        Escape code to be verified.

    Returns
    -------
    str
        It return escape code or a simple str.
    """    
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
    """Check if word is a valid delimiter, like \\t, for instance.

    Parameters
    ----------
    word : str
        Word to check if is a valida delimiter.

    Returns
    -------
    bool
        The right delimiter.
    """    
    if len(word) == 1:        
        if not isAscii(word):
            exit('Wronge delimiter: ' + word)
        else:
            return word
    # If len is 2, first character is \ and second isalpha()
    elif len(word) == 2 and word[0] == '\\' and word[1].isalpha():
        return replaceEscapeCode(word)
    else:
        exit('Wronge delimiter: ' + word)