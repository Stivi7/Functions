import string

def process_file(filename):                 #loops through the lines of the file, passing them one at a time to
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):               #The histogram hist is being used as an accumulator.
    line = line.replace('-', ' ')           #Replaces - with spaces to easily split words

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)       #Strips the words from punctuations and spaces.
        word = word.lower()                                             #Lowercase the words.
        hist[word] = hist.get(word, 0) + 1     #updates the histogram by creating a new item or incrementing an existing one.


hist = process_file('words.txt')

def total_words(hist):                      #counts the words of the document
    return sum(hist.values())

def different_words(hist):                  #The number of different words is just the number of items in the dictionary
    return len(hist)

print("total n of words", total_words(hist))

print("total of dif words", different_words(hist))
