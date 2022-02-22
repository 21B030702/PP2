import numpy
def solve(numheads, numlegs):
    M1 = numpy.array([[1, 1], [2, 4]]) 
    v1 = numpy.array([numheads, numlegs])
    print(numpy.linalg.solve(M1, v1))
numheads, numlegs = map(int, input().split())
solve(numheads, numlegs)
