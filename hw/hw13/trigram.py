"""
Short Program That Generates Over 100 Words Of A Moby Dick
Style Story Using Trigrams.
"""

import random
# get the file used to create the trigram
file = open("mobydick.txt", "r")
# take the text and store in memory line by line
lines = []
for line in file:
    lines.append(file.readline())
file.close()

# Used to store individual words and trigrams.
words = []
trigrams = {}

# Go through each line and split it up into indivdual words
for line in lines:
    words += line.replace('--', ' ').replace('\n', '').split(' ')
# Go through each word and set up a trigram (word, nextword): wordafternextword
for i, word in enumerate(words):
    # if are able to get 3 words without a index out of range.
    if(i + 1 in range(len(words)) and i + 2 in range(len(words))):
        # if a two word sequence already appeared.
        if((word, words[i + 1]) in trigrams.keys()):
            trigrams[(word, words[i + 1])].append(words[i + 2])
        # otherwise create a new trigram for that sequence
        else:
            trigrams[(word, words[i + 1])] = [words[i + 2]]

# the random starting trigram and printing for the text generation.
start = random.choice(list(trigrams.keys()))
print(start[0], start[1], trigrams[start][0], end=' ')
# set up the next trigram key
nextKey = (start[1], trigrams[start][0])
lastWord = start[1]
# generates new text while the the last two words printed exist in the trigram
wordsPrinted = 0
wordLimit = random.randint(125, 201)
# will stop generating new text after between 125 and 200 words have been made.
while(nextKey in trigrams.keys() and wordsPrinted < wordLimit):
    # used to select a random 3rd word from the trigram
    ran = random.choice(range(len(trigrams[nextKey])))
    newWord = trigrams[nextKey][ran]
    print(newWord, end=' ')
    # set up the next trigram
    lastWord = nextKey[1]
    nextKey = (lastWord, newWord)
    wordsPrinted += 1
# print a new line to look nice in the terminal
print()
