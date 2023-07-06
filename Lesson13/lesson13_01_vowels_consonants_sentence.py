"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
    a) Write a function that, given a letter, determines if it is a vowel. 
	b) Write a function that, given a letter, determines if it is a consonant.
    c) Using the previous functions, build a program that, given a sentence, determines
        the number of vowels that are found between two consonants of the same word.
Ex: Today I will go to the movies  A: 4 (Tod, day, wil, mov)
"""

#%%

def isvogal(char):
    vowels = ('a','e','i','o','u')
    return char.lower() in vowels
    
def isCons(char):
    char = char.lower()
    if char >= 'a' and char <= 'z':
        if isvogal(char) == False:
            return True
        else:
            return False
    

frase = 'Today I will go to the movies'
palavras = frase.split(' ')

resultado = []
for palavra in palavras:
    for i in range(1,len(palavra)-1):
        if isCons(palavra[i-1]) and isvogal(palavra[i]) and isCons(palavra[i+1]):
            resultado.append(palavra[i-1:i+2])

print (resultado)        
    

