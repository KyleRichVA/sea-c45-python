import random
# get the file used to create the trigram
file = open("sherlock_small.txt", "r")
# take the text and store in memory line by line
lines = []
for line in file:
    lines.append(file.readline())
words = []
trigrams = {}

for line in lines:
    words += line.replace('--', ' ').replace('\n', ' ').split()
for i, word in enumerate(words):
    # if are able to get 3 words without a index out of range.
    if(i + 1 in range(len(words)) and i + 2 in range(len(words))):
        # if a two word sequence already appeared.
        if((word, words[i + 1]) in trigrams.keys()):
            trigrams[(word, words[i + 1])].append(words[i + 2])
        # otherwise create a new trigram for that sequence
        else:
            trigrams[(word, words[i + 1])] = [words[i + 2]]

start = ('as', 'I')
print(start[0], start[1], trigrams[start][1])
next = (start[1], trigrams[start][0])
print(trigrams[next][0])

