#Renewable energy splitup
import matplotlib.pyplot as plt
plt.bar(['Hydro','SHP','Wind','Biomass','Solar','W to E'],[46850.18,4924.65,41895.28,10205.61,61966.36,520.23], label='Mega watts')
#plt.legend()
plt.xlabel('Mode wise breakup')
plt.ylabel('Megawatt')
plt.title('Renewable energy splitup')
plt.figtext(0.5, -0.1, "SHP:Small Hydro Project (≤ 25 MW)\n W to E: Waste to Energy", ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.75, "pad": 5})
#plt.grid(True)
plt.show()
