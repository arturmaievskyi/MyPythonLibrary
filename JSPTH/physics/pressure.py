class FluidMaterial:
    def __init__(self, name, density, dynamic_viscosity):
        self.name = name
        self.density = density
        self.mu = dynamic_viscosity

    def get_kinematic_viscosity(self):
        return self.mu / self.density
    


class Preasure:
    def __init__(self, height, gravity=9.81, ro=1000, force=None, area=None, volume=None):
        self.height = height
        self.gravity = gravity
        self.ro = ro
        self.force = force
        self.area = area
        self.volume = volume

class Mechanic(Preasure): 
    def calculate_mechanic(force, area):
        return force / area if area != 0 else 0
    

class Fluids(Preasure):
    def hydrostatic_pressure(ro, gravity, height):
        return ro * gravity * height
    
    def archimedes_principle(ro, gravity, volume):
        return ro * gravity * volume
    
    def bernoulli_equation(ro, velocity1, velocity2, height1, height2):
        return 0.5 * ro * (velocity1**2 - velocity2**2) + ro * 9.81 * (height1 - height2)

    @staticmethod
    def volumetric_flow_rate_by_velocity(area, velocity):
        if area < 0 or velocity < 0:
            raise ValueError("Area and Velocity must be non-negative.")
        return area * velocity

    @staticmethod
    def volumetric_flow_rate_by_time(volume, time):
        if time <= 0:
            raise ZeroDivisionError("Time must be greater than zero.")
        return volume / time

    @staticmethod
    def velocity_from_flow(flow_rate, area):
        return flow_rate / area
    
    def calculate_reynolds(fluid, velocity, diameter):
        return (fluid.density * velocity * diameter) / fluid.mu
    
    