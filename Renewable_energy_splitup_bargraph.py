#Renewable energy splitup
import matplotlib.pyplot as plt
import matplotlib as mpl

# set font style and size
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 12

# set color palette
colors = ['#36b3d7', '#e6af4b', '#8b72a6', '#d1635f', '#5cb85c', '#f0ad4e']

# set figure size and background color
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#f7f7f7')

# plot bar chart
x_pos = [0, 1, 2, 3, 4, 5]
plt.bar(x_pos, [46850.18,4924.65,41895.28,10205.61,61966.36,520.23], label='Mega watts', color=colors)

# set tick labels
ax.set_xticks(x_pos)
ax.set_xticklabels(['Hydro','SHP','Wind','Biomass','Solar','W to E'])

# set axis labels and title
plt.xlabel('Mode wise breakup')
plt.ylabel('Megawatt')
plt.title('Renewable energy splitup', fontsize=16)

# add text to figure
plt.figtext(0.5, -0.1, "SHP:Small Hydro Project (≤ 25 MW)\n W to E: Waste to Energy", ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.75, "pad": 5})

# show plot
plt.show()
