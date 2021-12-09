"""
    Description: This program reads natural text and classify its sentiment
    (e.g., negative vs. positive; 5-star vs. 3-star product). We analyze movie
    review data extracted from Rotten Tomatoes and use sorting to determine which
    words are most associated with positive reviews and which words are most
    associated with negative reviews. Now with dictionaries!
    Author: Matthew Erdman
    Date: 10/25/21
"""


def parallelInsertionSort(sentScore, sentWords):
    """
    Purpose: Use a modified insertion sort algorithm to sort two linked lists simultaneously,
    keeping them linked.
    Parameters: sentScore - the list of integer word sentiment scores, and
    sentWords - the list of movie review words. These lists are linked.
    Return Value: sentScore - the sorted list of integer scores for the review words,
    and sentWords - the sorted list of review words. These lists are linked.
    """
    for i in range(1, len(sentScore)):
        key = sentScore[i]
        keyWords = sentWords[i] # track a second key for sentWords
        j = i-1
        while j >=0 and key < sentScore[j]: # go through items to the left of key
            sentScore[j+1] = sentScore[j]
            sentWords[j+1] = sentWords[j]   # swap sentWords when we swap sentScore
            j -= 1
        sentScore[j+1] = key
        sentWords[j+1] = keyWords           # swap sentWords when we swap sentScore

    return sentScore, sentWords             # linked lists are now both sorted


def sortScores(sentiments):
    """
    Purpose: Turn a dictionary into two parallel lists and sort them with parallelInsertionSort().
    Parameters: The dictionary containing the string word keys and integer scores.
    Return Value: sentScore - the sorted list of integer scores for the review words,
    and sentWords - the sorted list of review words. These lists are linked.
    """
    sentWords = []
    sentScore = []
    for word in sentiments:
        sentWords.append(word)
        sentScore.append(sentiments[word])

    sentScore, sentWords = parallelInsertionSort(sentScore, sentWords)
    return sentScore, sentWords


def binarySearch(x, L):
    """
    Purpose: Perform a binary search to find a specified value in a list.
    Parameters: x - the value to look for, and L - the list to look in.
    Return Value: Boolean indicating if x is in L and the integer index of x.
    """
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high)//2

        if x == L[mid]:       # found x in L
            return True, mid

        elif x > L[mid]:      # too low, adjust low bound
            low = mid + 1

        elif x < L[mid]:      # too high, adjust high bound
            high = mid - 1

    return False              # x is not in L


def sentiment(reviewFilename):
    """
    Purpose: Open a .txt file containing a 0-4 score and written movie review,
    and build a dictionary with integer scores assigned to each word.
    Parameters: The string filename of the reviews file.
    Return Value: A dictionary containing the string review word keys and integer scores.
    """
    stopWords = getStopWords()
    sentiments = {}
    rawReviews = open(reviewFilename, 'r')
    for line in rawReviews:
        # review text is second char onward, remove whitespace/caps when grabbing words
        for word in line[2:].strip().lower().split(" "):
            if word in sentiments:
                # word has already been found, update the existing score
                sentiments[word] += int(line[:1]) - 2 # score is first char of line
            elif word.isalpha() and not binarySearch(word, stopWords):
                # new entry for new word, ensure it's alphabetical and not a stop word
                sentiments[word] = int(line[:1]) - 2 # score is first char of line
    rawReviews.close()

    return sentiments


def getStopWords():
    """
    Purpose: Open a .txt file containing stop words, reads each word in as a string
    and stores it in a list.
    Parameters: None.
    Return Value: A list of stop words as strings.
    """
    stopWords = []
    wordsFile = open("stopwords.txt", 'r')
    for line in wordsFile:
        stopWords.append(line.strip())
    wordsFile.close()

    return stopWords


def printScores(sentScore, sentWords):
    """
    Purpose: Print the top 20 scored and bottom 20 scored words.
    Parameters: sentScore - the list of integer word sentiment scores, and
    sentWords - the list of movie review words. These lists are linked.
    Return Value: None.
    """
    # print top 20 words
    print("-----------------------------")
    print("top 20 words:")
    for i in range(len(sentWords)-1, len(sentWords)-21, -1):
        print(sentScore[i], sentWords[i])

    # print bottom 20 words
    print("\nbottom 20 words:")
    for i in range(19, -1, -1):
         print(sentScore[i], sentWords[i])


def main():
    # from time import time
    # startTime = time()

    # read in scores and reviews, assigning scores
    sentiments = sentiment("movieReviews.txt")
    # sentimentTime = time()
    # print("Sentiment analysis time: %.2f sec" % (sentimentTime - startTime))

    # sort sentiment scores
    print("Sorting...")
    sentScore, sentWords = sortScores(sentiments)
    # sortTime = time()
    # print("Sorting time: %.2f sec" % (sortTime - sentimentTime))

    printScores(sentScore, sentWords)

    # print("Total time: %.2f sec" % (time() - startTime))


main()
