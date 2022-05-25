install pip
from matplotlib import pyplot as plt

names=['Seth','Isaac','Okonko','Prince','Watty']
ages=[22,21,19,23,25]

plt.plot(names,ages,color='red',linestyle='solid',marker='*')
plt.title('Graph of Names against Ages')
plt.ylabel('Ages')
plt.xlabel('Names of Students')

plt.show()
