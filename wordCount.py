import string
"""
    Description: This program is only partially complete. To finish it, complete
                 the following exercises (in order):
                    1) Discuss the program with your neighbor. How do we process
                       the file? What are the keys and values for our dictionary?
                    2) What is the role of updateFrequency?
                    3) Complete updateFrequency to update the dictionary for each
                       word read in.
                    4) Complete the print method such that all words in the
                       dictionary with a value greater than the value n are printed.
    Author: Mr. Bloom
    Date: Spring 2020
"""

def updateFrequency(word, wordCountDict):
    """ update the word count dictionary for each word read in """
    cleanWord = word.translate(str.maketrans('', '', string.punctuation))
    if cleanWord in wordCountDict:
        wordCountDict[cleanWord] += 1
    else:
        wordCountDict[cleanWord] = 1


def readBooks(filename):
    """ process the book file """
    infile = open(filename, 'r')
    wordCounts = {}
    for line in infile:
        line = line.strip()
        wordsPerLine = line.lower().split(" ")
        for word in wordsPerLine:
            updateFrequency(word, wordCounts)
    infile.close()
    return wordCounts


def printDict(n, wordCountDict):
    """ complete the print method such that all words in the dictionary with
        a value greater than the value n are printed """
    for word in wordCountDict:
        if wordCountDict[word] > n:
            print("Word: %15s   Count: %i" % (word, wordCountDict[word]))


def main():
    filename = "../week12/lab12/book-database/alice.txt" # str(input("Enter filename: "))
    wordCounts = readBooks(filename)
    printDict(10, wordCounts)


main()
