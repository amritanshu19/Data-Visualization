def Fibonacci(n):

    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fiba=[]
fibb=[]
for i in range(31):
  fiba.append(i)
  fibb.append(Fibonacci(i))

plt.scatter(fiba,fibb,color='r',s=30,marker='o')

plt.plot(fiba,fibb, color='b',label='Fibonacci curve')
plt.title('Curve')
plt.ylabel('Range')
plt.xlabel('Domain')
plt.legend()
plt.grid(True, color='k')

plt.show()
