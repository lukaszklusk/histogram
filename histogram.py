import matplotlib.pyplot as plt
import numpy as np
import pylab


i = 4
n = 1000
x = np.random.normal(0,1,n)
d = int(round(np.sqrt(n)))
plt.hist(x,i)
pylab.show()