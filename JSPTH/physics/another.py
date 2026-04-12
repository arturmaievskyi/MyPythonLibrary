class FluidMaterial:
    def __init__(self, name, density, dynamic_viscosity):
        self.name = name
        self.density = density
        self.mu = dynamic_viscosity

    def get_kinematic_viscosity(self):
        return self.mu / self.density
    
