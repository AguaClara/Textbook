from aide_design.play import *

# Create a list of 100 numbers between 0 and 100 and then assign the units of degC to the array.
# This array will be the x values of the graph.

x = np.arange(2) * u.degC
GraphTarray = u.Quantity(np.arange(100),u.degC)

#Note the use of the .to method below to display the results in a particular set of units.
plt.plot(GraphTarray, pc.viscosity_kinematic(GraphTarray).to(u.mm**2/u.s), '-')
#plt.xlabel('Temperature (degrees Celcius)')
#plt.ylabel('Viscosity (mm^2/s)')
#plt.show()
