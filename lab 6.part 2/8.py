import os
f = open('Z.txt')
line = f.readline()
while line:
    print (line),
    line = f.readline()
f.close()
path = "C:\\Users\\a_nus\\Desktop\\lab6\\Z.txt"
os.remove(path)