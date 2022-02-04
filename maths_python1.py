import numpy
def f(x):
    return x * x
x = numpy.arange(0, 4, 0.01)
y = f(x)
from scipy.misc import derievative
d = derivative(f, 1.0, dx=1e-3)
print(d)
