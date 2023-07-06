"""
Created on 2022

@author: António Brito / Carlos Bragança

#objective:
    Consider that you have grades (integer values from 0 to 20) of N students.
    Write a function that computes the frequency (in percentage) of each of the
    grades.
"""
#%%

def grades_frequency(grades):
    ngrades = len(grades)
    freq = dict()
    for grade in range(21):
        freqgrade = grades.count(grade)
        if freqgrade > 0:
            freq[grade] = round(100 * freqgrade / ngrades , 1)
    return freq

n = int(input("Number of grades="))
grades = [0] * n
for i in range(n):
    grades[i] = float(input("Grade ="))
freq = grades_frequency(grades)
print(freq)
for grade, frequency in freq.items():
    print(f"{grade}\t{frequency:.1f}%")
