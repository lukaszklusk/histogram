import matplotlib.pyplot as plt
import numpy as np
import pylab


x = np.random.normal(0,1,1000)
d = int(round(np.sqrt(1000)))
plt.hist(x,4)
pylab.show()