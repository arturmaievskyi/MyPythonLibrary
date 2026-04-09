

class EnergyCalculator:
    def calculate_kinetic_energy(self, mass, velocity):
        return 0.5 * mass * velocity ** 2

    def calculate_potential_energy(self, mass, height, gravity=9.81):
        return mass * gravity * height
    
    def calculate_total_energy(self, mass, velocity, height, gravity=9.81):
        kinetic_energy = self.calculate_kinetic_energy(mass, velocity)
        potential_energy = self.calculate_potential_energy(mass, height, gravity)
        return kinetic_energy + potential_energy
    
    def energy_conversion(self, energy, from_unit, to_unit):
        conversion_factors = {
            'joules_to_calories': 0.239006,
            'calories_to_joules': 4.184,
            'joules_to_kilowatt_hours': 2.77778e-7,
            'kilowatt_hours_to_joules': 3.6e6,
        }
        
        key = f"{from_unit}_to_{to_unit}"
        if key in conversion_factors:
            return energy * conversion_factors[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
        
    def efficiency(self, useful_energy_output, total_energy_input):
        if total_energy_input == 0:
            raise ValueError("Total energy input cannot be zero.")
        return (useful_energy_output / total_energy_input) * 100
    
    def energy_density(self, energy, volume):
        if volume == 0:
            raise ValueError("Volume cannot be zero.")
        return energy / volume
    
    
