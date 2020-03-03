import re

def abbreviate(palabras):
    regex = "[A-Z]+['a-z]*|['a-z]+"
    return ''.join(word[0].upper() for word in re.findall(regex, palabras))
