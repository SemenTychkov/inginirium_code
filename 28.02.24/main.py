import numpy

a = numpy.array([[1,2,3,4], [5,6,7,8]])
b = numpy.repeat(a, 2). reshape(a.shape[0], a.shape[1], -1)
c = numpy.stack((a, a))
print(a.shape[0])
print(b)
print(c)