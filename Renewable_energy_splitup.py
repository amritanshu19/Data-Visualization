#Renewable energy splitup
import matplotlib.pyplot as plt

slices = [46850.18,4924.65,41895.28,10205.61,61966.36,520.23]
activities = ['Hydro','SHP','Wind','Biomass','Solar','Waste to Energy']
#cols = ['c','m','r','b']

plt.pie(slices,labels=activities,startangle=65,shadow=True,explode=(0,0.125,0,0.15,0,0.1),autopct='%.1f%%')

plt.title('Renewable Energy Splitup')

plt.figtext(0.5, -0.1, "SHP:Small Hydro Project (≤ 25 MW)", ha="center", fontsize=8, bbox={"facecolor": "white", "alpha": 0.75, "pad": 5})
plt.show()
