from aguaclara.play import*
import sys


Q_fi = 3.07*u.L/u.s
ID_twoft = (pipe.ID_SDR(2*u.ft, 26))
Pi_Branch = (10*u.cm * ID_twoft/2)/pc.area_circle(ID_twoft)

Q = Pi_Branch * Q_fi
PI = 0.62*u.dimensionless
epsilon = 1*u.dimensionless
HL = 5*u.cm
g = 9.80665 * u.m / u.s ** 2
A = 1/((np.sqrt(2*g*HL)*PI*epsilon)/ Q)
A = A.to(u.cm ** 2)

diam = 0.25*u.inch

A_orifice = (np.pi*(diam**2)/4).to(u.cm**2)
N_orifice = A/A_orifice
N_orifice
12*u.inch/N_orifice

## for regualr branches




Q_ff = Pi_Branch * Q_fi/3
HL_ff = 5*u.cm
g = 9.80665 * u.m / u.s ** 2
A = 1/((np.sqrt(2*g*HL_ff)*PI*epsilon)/ Q_ff)
A = A.to(u.cm ** 2)
diam_ff = 0.25*u.inch
A_orifice_ff = (np.pi*(diam_ff**2)/4).to(u.cm**2)
N_orifice_ff = A/A_orifice_ff
N_orifice_ff
12*u.inch/N_orifice_ff
