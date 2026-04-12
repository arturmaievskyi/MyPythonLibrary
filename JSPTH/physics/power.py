

class WorkPowerCalculator:
    def __init__(self, time, work=None, power=None, force=None, distance=None):
        self.time = time
        self.work = work
        self.power = power
        self.force = force
        self.distance = distance

    def calculate_power(self, work, time):
        if time == 0:
            raise ValueError("Time cannot be zero.")
        return work / time

    def energy_from_power(self, power, time):
        return power * time
