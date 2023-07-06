"""
Created on 2021

@author: António Brito / Carlos Bragança

"""
# Lesson11_01
#%% Accessing characters as elements of a list
s1 = "Hello World"
for i in range(len(s1)):
    print(s1[i])
    
#%% Accessing characters as elements of a list
s1 = "Hello World"
for char in s1:
    print(char)
    
#%% Accessing characters of a string in reverse order
s1 = "Hello World"
for i in range(-1,-(len(s1)+1), -1):
    print(s1[i])
    
#%% Printing characters of a string in reverse order
s1 = "Hello World"
print(s1[::-1])

# Lesson11_02
#%% Separate the words in a sentence
s1 = "I am going to the movies"
ncar = len(s1)
words = []              # List to store the words
pos = 0                 # Position of the first character in a word
for i in range(ncar):
    if s1[i] == " ":
        # If the character is a space a word ended
        words.append(s1[pos:i])
        pos = i + 1     # Position of the first character of the next word
words.append(s1[pos:])  # Get the last word that don't have a space in the end
print(words)

#%% Separate the words in a sentence using the split function
s1 = "I am going to the movies"
words = s1.split()      # Same as use split(" ")
print(words)