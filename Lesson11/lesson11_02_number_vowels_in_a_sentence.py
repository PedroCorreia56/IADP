"""
Created on 2022

@author: António Brito / Carlos Bragança

Count the number of vowels in a sentence.
"""
#%% option 1
vowels = ('a','e','i','o','u')
sentence = input("sentence:")
nvowels = 0
for letter in sentence.lower():
  for vowel in vowels:
    if letter == vowel:
        nvowels = nvowels + 1
print("N. of vowels =" , nvowels)

#%% option 2

vowels = ('a','e','i','o','u')
sentence = input("sentence:")
nvowels = 0
for letter in sentence.lower():
  for vowel in vowels:
    if letter == vowel:
        nvowels = nvowels + 1
print("N. of vowels =" , nvowels)

#%% option 3

vowels = ('a','e','i','o','u')
sentence = input("sentence:")
nvowels = 0
for letter in sentence.lower():
    if letter in vowels:
        nvowels = nvowels + 1
print("N. of vowels =" , nvowels)

#%% option 4 

sentence = input("sentence:")
num_char = len(sentence)
characters =[None]*num_char

for i in range(num_char):
  characters[i] = sentence[i].upper()

num_vowels = 0
for i in range(num_char):
  if characters[i] == "A" or characters[i] == "E" or characters[i] == "I" or characters[i] == "O" or characters[i] == "U":
    num_vowels = num_vowels + 1

print ("Number of vowels =" , num_vowels)
