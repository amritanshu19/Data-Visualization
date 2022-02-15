#fibonacci vs 2^x curves upto 1st 10 terms
def Fibonacci(n):

    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fiba=[]
fibb=[]
by=[]
for i in range(10):
  fiba.append(i)
  fibb.append(Fibonacci(i))
  by.append(2**i)

plt.scatter(fiba,fibb,color='r',s=30,marker='o')

plt.plot(fiba,fibb, color='b',label='Fibonacci curve')

plt.scatter(fiba,by,color='indigo',s=30,marker='o')

plt.plot(fiba,by, color='m',label='2^x')
plt.title('Curve')
plt.ylabel('Range')
plt.xlabel('Domain')
plt.legend()
plt.grid(True, color='k')

plt.show()
