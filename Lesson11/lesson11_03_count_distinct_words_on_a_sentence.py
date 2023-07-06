"""
Created on 2020

@author: António Brito / Carlos Bragança

#objective: Count the number of times each distinct word appears on a sentence.
"""
# %% solution without python functions
sentence = input("Sentence:")
sentence = sentence.strip() + " "  # adds a space to the end of the sentence
length_sentence = len(sentence)
start_word = 0  # first word starts at index zero of the sentence
words = []  # creates an empty list to store words
nwords = 0
for index in range(0, length_sentence):
    if sentence[index] == " ":  # check for a space
        nwords = nwords + 1  # another word was found
        word = sentence[start_word: index]  # get the word
        words.append(word)  # add the word to the words list
        start_word = index + 1  # next word starts after the space

print(f"Sentence has {nwords} words")
print(words)

for index1 in range(nwords):
    word = words[index1]
    count_words = 0
    for index2 in range(index1):
        if word == words[index2]:
            count_words = count_words + 1
    if count_words == 0:  # it is the first time this word appears
        for index2 in range(index1, nwords):
            if word == words[index2]:
                count_words = count_words + 1
        print(f"The word: {word} appears {count_words} times")

# %% Another version using split and dictionaries
sentence = input("Sentence:")
words = sentence.split(" ")  # returns the list of words
nwords = len(words)
print(f"Sentence has {nwords} words")
print(words)
words_dict = dict.fromkeys(words, 0)  # creates a dict with the words as keys and values 0
for word in words_dict:
    words_dict[word] = words.count(word)  # counts the number of times each word appears
print(words_dict)
