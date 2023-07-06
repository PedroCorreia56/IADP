""" sentence = input()

l=sentence.split(" ")

l.reverse()


new_sentence = ""

for i in range(len(l)):
    if(i>0):
        new_sentence=new_sentence+" "
    new_sentence =  new_sentence + l[i]
    

print(new_sentence) """

""" word=input()
number=int(input())

alphaber="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newword=""

for wr in word:
    print(wr)
    pos=alphaber.find(wr)
    newword=newword+alphaber[pos+number]

print(newword) """
bannedwords=["da","das","de","do","dos"]
sentence = input()
newsentence=""
l=sentence.split(" ")

for word in l:
    if word in bannedwords:
        l.remove(word)

for i in range(len(l)):
    if i+1==len(l):
        newsentence=newsentence+l[i]
        break
    else:
        newsentence=newsentence+l[i][0]+"."+" "
print(newsentence)    
