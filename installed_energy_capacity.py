#all data from here: https://cea.nic.in/wp-content/uploads/installed/2022/11/IC_Nov_2022.pdf
#ALL INDIA  INSTALLED CAPACITY Pie Chart

import matplotlib.pyplot as plt
import matplotlib as mpl

# set font style and size
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 12

# set color palette
colors = ['#36b3d7', '#e6af4b', '#8b72a6']

slices = [236018.90, 6780.00, 166362.31]
activities = ['Thermal','Nuclear','Renewable']

# set figure size and background color
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#f7f7f7')

# plot pie chart
patches, texts, autotexts = ax.pie(slices, labels=activities, startangle=65, shadow=True,
                                   explode=(0,0.125,0), autopct='%.1f%%', 
                                   colors=colors, wedgeprops={"edgecolor": "k", "linewidth": 1}, 
                                   textprops={"color": "k"})

# set title and legend
plt.title('ALL INDIA  INSTALLED CAPACITY(IN MW) OF POWER STATIONS', fontsize=16)
plt.legend(patches, activities, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)


# show plot
plt.show()
