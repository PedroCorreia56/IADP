""" 

file = input('Filename:')
column=input('Column name:')
func=input('Function name:')

lis=['id','nome','altura','peso','idade','horas','estado','filhos']

location=lis.index(column)
f1 = open(file,"r")
help=[]
for line in f1:
    healp=line.split(";")
    if healp[location] not in lis:
        help.append(float(healp[location]))


if func=="max":
    resultado=max(help)
    print("{}({})={:.2f}".format(func,column,resultado))
if func=="min":
    resultado=min(help)
    print("{}({})={:.2f}".format(func,column,resultado))
if func=="sum":
    resultado=sum(help)
    print("{}({})={:.2f}".format(func,column,resultado))
 """

""" file1 = input('Filename 1:')
file2 = input('Filename 2:')

f1=open(file1,"r")

for line in f1:
    f2=open(file2,"r")
    for ll in f2:
        word=line.strip()+" "+ll.strip()
        print(word)
    f2.close """

file1 = input('Filename 1:')
file2 = input('Filename 2:')    
f1 = open(file1,"r")
f2 = open(file2,"r")
line1 = f1.readline()
line2 = f2.readline()
while line1 != '' and line2 != '':
    media = (float(line1) + float(line2)) / 2
    print(media)
    line1 = f1.readline()
    line2 = f2.readline()

while line1 != '':
    print((float(line1) / 2))
    line1 = f1.readline()

while line2 != '':
    print((float(line2) / 2))
    line2 = f2.readline()