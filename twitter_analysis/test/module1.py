import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random

x = [random() * 10 for i in range(10)]
y = [random() * 10 for i in range(10)]

plt.plot(x, y, label='label1', color='r')
plt.legend()
plt.fill_between(x, y, color='r')

x = [random() * 10 for i in range(10)]
y = [random() * 10 for i in range(10)]

plt.plot(x, y, label='label2', color='b')
plt.legend()
plt.fill_between(x, y, color='b')


plt.show()