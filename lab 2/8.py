from math import*
result = {

}
list = []
coordinates = [int(i) for i in input().split()]
x, y = coordinates[0], coordinates[1]
for i in range(int(input())):
    t = input()
    coordinates = [int(i) for i in t.split()]
    a, b = coordinates[0], coordinates[1]
    distance = sqrt((a-x)**2+(b-y)**2)
    list.append(distance)
    result[t] = distance
list.sort()
for i in list:
    for j in result:
        if result[j] == i:
            print(j)