a = []
b = []

from matplotlib import pyplot as plt
import numpy as np
for i in range(81):
  a.append(4*np.sin(3.75*i))
  b.append(3*np.cos(3.75*i))


plt.scatter(a,b,label='Elipse',color='r',s=30,marker='o')

plt.plot(a,b, color='b')
plt.title('Curve')
plt.ylabel('Range')
plt.xlabel('Domain')
plt.grid(True, color='k')

plt.show()
