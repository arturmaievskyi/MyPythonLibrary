from .energy_importer import *


class OtherAnalyzing():
    @staticmethod
    def compare_kinetic_energies(objects: List[KineticObject]) -> Dict[str, float]:
        """
        Compare kinetic energies of multiple objects.
        
        :param objects: List of KineticObject instances
        :return: Dictionary of object names and their kinetic energies
        """
        results = {}
        for obj in objects:
            results[obj.name] = KineticEnergyCalculator.kinetic_energy(obj.mass, obj.velocity)
        return results
        
    @staticmethod
    def kinetic_energy_distribution(objects: List[KineticObject]) -> Dict[str, float]:
        """
        Calculate distribution of kinetic energy among objects.
        
        :param objects: List of KineticObject instances
        :return: Dictionary of object names and their percentage of total KE
        """
        ke_values = KineticEnergyCalculator.compare_kinetic_energies(objects)
        total_ke = sum(ke_values.values())
        
        if total_ke == 0:
            return {name: 0 for name in ke_values}
        
        return {name: (ke / total_ke) * 100 for name, ke in ke_values.items()}
    
    @staticmethod
    def kinetic_energy_timeline(initial_mass: float, initial_velocity: float, 
                                acceleration: float, time_steps: List[float]) -> Dict[float, float]:
        """
        Calculate kinetic energy over time with constant acceleration.
        
        :param initial_mass: Mass in kg
        :param initial_velocity: Initial velocity in m/s
        :param acceleration: Acceleration in m/s²
        :param time_steps: List of times in seconds
        :return: Dictionary mapping time to kinetic energy
        """
        timeline = {}
        for t in time_steps:
            velocity = initial_velocity + acceleration * t
            ke = KineticEnergyCalculator.kinetic_energy(initial_mass, abs(velocity))
            timeline[t] = ke
        return timeline
    
    @staticmethod
    def kinetic_energy_decay(initial_ke: float, decay_constant: float, 
                            time_steps: List[float]) -> Dict[float, float]:
        """
        Calculate kinetic energy decay over time.
        KE(t) = KE₀ * e^(-t/τ)
        
        :param initial_ke: Initial kinetic energy in Joules
        :param decay_constant: Time constant τ in seconds
        :param time_steps: List of times in seconds
        :return: Dictionary mapping time to kinetic energy
        """
        timeline = {}
        for t in time_steps:
            ke = initial_ke * math.exp(-t / decay_constant)
            timeline[t] = ke
        return timeline
    
    @staticmethod
    def kinetic_energy_statistics(objects: List[KineticObject]) -> Dict[str, float]:
        """
        Calculate statistical measures of kinetic energies.
        
        :param objects: List of KineticObject instances
        :return: Dictionary with statistics
        """
        ke_values = list(KineticEnergyCalculator.compare_kinetic_energies(objects).values())
        
        if not ke_values:
            return {}
        
        mean = sum(ke_values) / len(ke_values)
        variance = sum((x - mean) ** 2 for x in ke_values) / len(ke_values)
        std_dev = math.sqrt(variance)
        
        return {
            'total': sum(ke_values),
            'mean': mean,
            'median': sorted(ke_values)[len(ke_values) // 2],
            'min': min(ke_values),
            'max': max(ke_values),
            'variance': variance,
            'std_dev': std_dev,
            'count': len(ke_values),
        }
