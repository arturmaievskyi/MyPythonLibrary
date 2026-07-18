

class Mechanic(): 
    def calculate_mechanic(force, area):
        return force / area if area != 0 else 0
    

class Fluids():
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
    
class IdealGas:
    R = 8.31446  # Universal Gas Constant

    def __init__():
        pass

    def solve_for_pressure(self, n, t, v):
        # P = nRT / V
        return (n * self.R * t) / v

    def solve_for_volume(self, n, t, p):
        # V = nRT / P
        return (n * self.R * t) / p

