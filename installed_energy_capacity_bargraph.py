#ALL INDIA  INSTALLED CAPACITY(IN MW) OF POWER STATIONS
import matplotlib.pyplot as plt
import matplotlib as mpl

# set font style and size
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 12

# set color palette
colors = ['#36b3d7', '#e6af4b', '#8b72a6']

# set figure size and background color
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#f7f7f7')

# plot bar chart
x_pos = [0, 1, 2]
plt.bar(x_pos, [236018.90, 166362.31, 6780.00], label='Mega watts', color=colors)

# set tick labels
ax.set_xticks(x_pos)
ax.set_xticklabels(['Thermal','Renewable','Nuclear'])

# set axis labels and title
plt.xlabel('Mode wise breakup')
plt.ylabel('Megawatt')
plt.title('ALL INDIA  INSTALLED CAPACITY(IN MW) OF POWER STATIONS', fontsize=16)


plt.show()
