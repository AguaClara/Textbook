#from aide_design.play import*

# Create a list of 100 numbers between 0 and 100 and then assign the units of degC to the array.
# This array will be the x values of the graph.

#x = np.arange(2) * u.degC
#GraphTarray = u.Quantity(np.arange(100),u.degC)

#Note the use of the .to method below to display the results in a particular set of units.
#ax.plot(GraphTarray, pc.viscosity_kinematic(GraphTarray).to(u.mm**2/u.s), '-')
#ax.set(xlabel='Temperature (degrees Celcius)')
#ax.set(ylabel='Viscosity (mm^2/s)')
#plt.show()


#import sys
#from PyQt5 import QtWidgets
#app = QtWidgets.QApplication(sys.argv)


import matplotlib.pyplot as plt
import numpy as np

xgraph = np.arange(100)
ygraph = xgraph + 1
ax.plot(xgraph, ygraph, '-')
