#Thermal energy splitup
import matplotlib.pyplot as plt

slices = [24824.21,589.20,203985.49,6620.00]
activities = ['Gas','Diesel','Coal','Lignite']
#cols = ['c','m','r','b']

plt.pie(slices,labels=activities,startangle=65,shadow=True,explode=(0,0.125,0,0.15),autopct='%.1f%%')

plt.title('Thermal energy Splitup')

plt.show()
