import string


def lowecase(f):
    f = open('words.txt')
    for word in f.read().split():
        word = word.strip()
    
        print(word.lower())
    
    

lowecase('words.txt')