class Electrics:
    def __init__(self):
        pass

    def calculate_current(self, voltage, resistance):
        if resistance == 0:
            raise ValueError("Resistance cannot be zero.")
        return voltage / resistance

    def calculate_voltage(self, current, resistance):
        return current * resistance

    def calculate_resistance(self, voltage, current):
        if current == 0:
            raise ValueError("Current cannot be zero.")
        return voltage / current