import numpy

a = numpy.array([[ 2, -1, 3],
                 [4, 2, 0],
                 [-1, 1, 1]])
b = numpy.array([[1]
                 [2][]
                 [-1]])
c11 = a[0, 0] * b[0, 0] + a[0, 1] * b[1, 0] + a[0 ,2] * b[2, 0]
print(c11)