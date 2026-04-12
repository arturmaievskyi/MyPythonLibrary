from JSPTH import Console
from JSPTH import Physics

# creating variables for physics calculations
mass = 10  
velocity = 5
height = 20
time = 4
work = 1000
force = 200
distance = 50
power = 250

# Initializing the EnergyCalculator with the given parameters
physics_energy = Physics.EnergyCalculator(mass, height, velocity)
# initializing console for output
console = Console.console.Console()
# Initializing the WorkPowerCalculator with the given parameters
physics_workpowercalculator = Physics.WorkPowerCalculator(time, work, force, distance, power)

# exaples of using the EnergyCalculator to calculate kinetic and potential energy
kinetic_energy = physics_energy.calculate_kinetic_energy(mass, velocity)
console.print(f"The kinetic energy of an object with mass {mass} kg and velocity {velocity} m/s is: {kinetic_energy} J")
potential_energy = physics_energy.calculate_potential_energy(mass, height)
console.print(f"The potential energy of an object with mass {mass} kg at a height of {height} m is: {potential_energy} J")

# calculating power using the WorkPowerCalculator
energy_from_power = physics_workpowercalculator.energy_from_power(power, time)
console.print(f"The energy calculated from power {power} W and time {time} s is: {energy_from_power} J")
energy_power = physics_workpowercalculator.calculate_power(work, time)
console.print(f"The power calculated from work {work} J and time {time} s is: {energy_power} W")

