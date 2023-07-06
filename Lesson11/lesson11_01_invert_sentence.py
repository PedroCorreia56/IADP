"""
Created on 2022

@author: António Brito / Carlos Bragança

objective:
  Invert the characters of a sentence
  
Variables:
 sentence          -> Sentence
 num_char       -> Number of characters in the sentence
 single_char    -> single character
"""
#%% Version 1
sentence = input("Sentence : ")

num_char = len(sentence)
new_sentence = ""

for i in range(num_char-1,-1,-1):
    new_sentence =  new_sentence + sentence[i]

print(f"Inverted sentence: {new_sentence}")
#%% Version 2
sentence = input("Sentence : ")

new_sentence = sentence[::-1]

print(f"Inverted sentence: {new_sentence}")