import re

def to_let(num):
    a = ""
    for i in num:  
        if i == "1":
            a = a + "ONE"
        if i == "2":
            a = a + "TWO"
        if i == "3":
            a = a + "THR"
        if i == "4":
            a = a + "FOU"
        if i == "5":
            a = a + "FIV"
        if i == "6":
            a = a + "SIX"
        if i == "7":
            a = a + "SEV"
        if i == "8":
            a = a + "EIG"
        if i == "9":
            a = a + "NIN"
        if i == "0":
            a = a + "ZER"
    return a

def to_triplet(chr):
    if chr == "ONE":
        return "1"
    if chr == "TWO":
        return "2"
    if chr == "THR":
        return "3"
    if chr == "FOU":
        return "4"
    if chr == "FIV":
        return "5"
    if chr == "SIX":
        return "6"
    if chr == "SEV":
        return "7"
    if chr == "EIG":
        return "8"
    if chr == "NIN":
        return "9"
    if chr == "ZER":
        return "0"
def to_dig(s):
    a = ""
    cifr = ""
    for i in range(0,len(s),3):
        cifr = cifr +  s[i] + s[i+1] + s[i+2]
        a = a + to_triplet(cifr)
        cifr = ""
    return(a)
s = input()
a = ""
b = ""
znak = s.find("+")
for i in range(znak):
    a = a + s[i]
for i in range(znak+1, len(s)):
    b = b + s[i]
print(to_let (str (int(to_dig(a)) + int(to_dig(b)))))