digit = ['1','2', '3', '4', '5', '6', '7', '8', '9', '10']
#color = ['blue', 'yellow', 'pink', 'red', 'black', 'white', 'green']
with open('input.txt',"w") as file:
    for  i in digit:
        file.write("%s\n" % i)
content = open("input.txt")
print(content.read())