import matplotlib.pyplot as plt
import matplotlib as mpl

# set font style and size
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 12

# set color palette
colors = ['#36b3d7', '#e6af4b', '#8b72a6', '#d1635f', '#5cb85c', '#f0ad4e']

slices = [46850.18,4924.65,41895.28,10205.61,61966.36,520.23]
activities = ['Hydro','SHP','Wind','Biomass','Solar','Waste to Energy']

# set figure size and background color
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#f7f7f7')

# plot pie chart
patches, texts, autotexts = ax.pie(slices, labels=activities, startangle=65, shadow=True,
                                   explode=(0,0.125,0,0.15,0,0.1), autopct='%.1f%%', 
                                   colors=colors, wedgeprops={"edgecolor": "k", "linewidth": 1}, 
                                   textprops={"color": "k"})

# set title and legend
plt.title('Renewable Energy Splitup', fontsize=16)
plt.legend(patches, activities, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)

# add text to figure
plt.figtext(0.5, -0.1, "SHP:Small Hydro Project (≤ 25 MW)", ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.75, "pad": 5})

# show plot
plt.show()
