from aide_design.play import*
def v_t(D_particle,density_particle,Temperature):
  return (D_particle**2*pc.gravity *(density_particle - pc.density_water(Temperature))/(18*pc.viscosity_kinematic(Temperature)*pc.density_water(Temperature))).to(u.m/u.s)
clay = 2650 * u.kg/u.m**3
organic = 1040 * u.kg/u.m**3
Temperature = 20 * u.degC
D_particle = np.logspace(-6,-3)*u.m
fig, ax = plt.subplots()
ax.loglog(D_particle.to(u.m),v_t(D_particle,clay,Temperature).to(u.m/u.s))
ax.loglog(D_particle.to(u.m),v_t(D_particle,organic,Temperature).to(u.m/u.s))
ax.set(xlabel='Particle diameter (m)', ylabel='Terminal velocity (m/s)')
ax.legend(["clay or sand","organic particle"])
plt.show()