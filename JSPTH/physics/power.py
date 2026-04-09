

class PowerCalculator:
    def calculate_power(self, work, time):
        if time == 0:
            raise ValueError("Time cannot be zero.")
        return work / time
    
    def energy_from_power(self, power, time):
        return power * time

    
    