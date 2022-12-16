#all data from here: https://cea.nic.in/wp-content/uploads/installed/2022/11/IC_Nov_2022.pdf
#ALL INDIA  INSTALLED CAPACITY Pie Chart

import matplotlib.pyplot as plt

capacity = [236018.90,6780.00,166362.31]
modes = ['Thermal','Nuclear','Renewable']
cols = ['c','m','r']

plt.pie(capacity ,labels=modes,startangle=60,shadow=True,explode=(0,0.2,0),autopct='%.1f%%')

plt.title('ALL INDIA  INSTALLED CAPACITY(IN MW) OF POWER STATIONS ')

plt.show()
