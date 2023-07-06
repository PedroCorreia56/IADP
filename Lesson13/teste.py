def iscons(a):
        vowels = ('a','e','i','o','u')
        a = a.lower()
        if a >= 'a' and a <= 'z':
            if a in vowels:
                return False
            else:
                return True

#pr=input()

def swap(h):
    l=h.split(" ")
    l.reverse()
    final=""+l[0]+" "+l[-1]
    return final

print(swap("Cristiano Ronaldo"))


def grades_frequency(grades):
    ngrades = len(grades)
    freq = dict()
    for grade in range(21):
        freqgrade = grades.count(grade)
        if freqgrade > 0:
            freq[grade] = round(100 * freqgrade / ngrades , 1)
    return freq

grades = [10, 9, 10, 12, 10, 9, 11, 10, 12, 13]
print(grades_frequency(grades))