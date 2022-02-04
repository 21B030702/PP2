n  = int(input())
list = []
for i in range(0,n):
    a = int(input())
    list.append(a)
for i in range(0,len(list)):
    if list[i] <= 10:
       print("Go to work!")
    elif list[i] > 10 and list[i] <= 25:
       print("You are weak")
    elif list[i] > 25 and list[i] <= 45:
       print("Okay, fine")
    elif list[i] > 45:
       print("Burn! Burn! Burn Young!")
