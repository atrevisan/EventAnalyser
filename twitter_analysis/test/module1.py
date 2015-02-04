import matplotlib.pyplot as plt
import numpy as np

x_ticks = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

y_values = [33, 55, 88, 22, 5, 9, 1]
x_values = [0, 1, 2, 3, 4, 5, 6]

max_frequency = sorted (y_values, key=lambda x : -x)[0]
                
#print("Max frequency: %d" %max_frequency)

plt.plot(x_values, y_values, linewidth=1.5, label="haha")
plt.legend()
          
plt.xticks(np.arange(0, 7), x_ticks)
plt.ylim(0, max_frequency)
                
plt.xlabel("Day of week")
plt.ylabel("N-gram frequency")
plt.title("N-gram frequency distribution")

plt.show()