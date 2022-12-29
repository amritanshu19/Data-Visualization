#Thermal energy splitup barchart
import matplotlib.pyplot as plt
import matplotlib as mpl

# set font style and size
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 12

# set color palette
colors = ['#36b3d7', '#e6af4b', '#8b72a6', '#d1635f'] #, '#5cb85c', '#f0ad4e']

# set figure size and background color
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#f7f7f7')

# plot bar chart
x_pos = [0, 1, 2, 3]
plt.bar(x_pos, [24824.21,589.20,203985.49,6620.00], label='Mega watts', color=colors)

# set tick labels
ax.set_xticks(x_pos)
ax.set_xticklabels(['Gas','Diesel','Coal','Lignite'])

# set axis labels and title
plt.xlabel('Mode wise breakup')
plt.ylabel('Megawatt')
plt.title('Thermal energy splitup', fontsize=16)


plt.show()
