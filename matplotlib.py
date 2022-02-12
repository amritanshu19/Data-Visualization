#normal graphs
a = []
b = []
for i in range(11):
  a.append(i)
  a.append(-i)
a.sort()
for i in a:
  b.append(i*i)
from matplotlib import pyplot as plt

plt.plot(a,b)
plt.title('Parabola')
plt.ylabel('Range')
plt.xlabel('Domain')

plt.show()
