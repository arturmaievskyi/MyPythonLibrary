# JSPTH/physics/kinetic_energy.py

from .energy_importer import *

class ReferenceFrame(Enum):
    """Types of reference frames for kinetic energy calculations."""
    INERTIAL = "inertial"
    MOVING = "moving"
    ROTATING = "rotating"
    CENTER_OF_MASS = "center_of_mass"


@dataclass
class KineticObject:
    """Represents an object with kinetic energy properties."""
    mass: float
    velocity: float
    name: str = "Object"
    radius: float = 0.0  # For rotational KE
    angular_velocity: float = 0.0  # For rotational KE
    moment_of_inertia: float = 0.0  # For rotational KE


class KineticEnergyCalculator:
    """
    Comprehensive kinetic energy calculations covering all aspects of motion.
    """
    
    # Physical constants
    SPEED_OF_LIGHT = 299792458  # m/s
    BOLTZMANN_CONSTANT = 1.380649e-23  # J/K
    
    def __init__(self):
        pass
    
    # ==================== BASIC KINETIC ENERGY ====================
    
    @staticmethod
    def kinetic_energy(mass: float, velocity: float) -> float:
        """
        Calculate kinetic energy: KE = (1/2) * m * v²
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Kinetic energy in Joules
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if velocity < 0:
            raise ValueError("Velocity cannot be negative")
        return 0.5 * mass * velocity ** 2
    
    @staticmethod
    def kinetic_energy_2d(mass: float, vx: float, vy: float) -> float:
        """
        Calculate kinetic energy in 2D: KE = (1/2) * m * (vx² + vy²)
        
        :param mass: Mass in kg
        :param vx: Velocity in x-direction in m/s
        :param vy: Velocity in y-direction in m/s
        :return: Kinetic energy in Joules
        """
        velocity_magnitude = math.sqrt(vx**2 + vy**2)
        return KineticEnergyCalculator.kinetic_energy(mass, velocity_magnitude)
    
    @staticmethod
    def kinetic_energy_3d(mass: float, vx: float, vy: float, vz: float) -> float:
        """
        Calculate kinetic energy in 3D: KE = (1/2) * m * (vx² + vy² + vz²)
        
        :param mass: Mass in kg
        :param vx: Velocity in x-direction in m/s
        :param vy: Velocity in y-direction in m/s
        :param vz: Velocity in z-direction in m/s
        :return: Kinetic energy in Joules
        """
        velocity_magnitude = math.sqrt(vx**2 + vy**2 + vz**2)
        return KineticEnergyCalculator.kinetic_energy(mass, velocity_magnitude)
    
    @staticmethod
    def kinetic_energy_vector(mass: float, velocity_vector: Tuple[float, ...]) -> float:
        """
        Calculate kinetic energy from velocity vector of any dimension.
        
        :param mass: Mass in kg
        :param velocity_vector: Tuple of velocity components
        :return: Kinetic energy in Joules
        """
        velocity_magnitude = math.sqrt(sum(v**2 for v in velocity_vector))
        return KineticEnergyCalculator.kinetic_energy(mass, velocity_magnitude)
    
    # ==================== VELOCITY FROM KINETIC ENERGY ====================
    
    @staticmethod
    def velocity_from_kinetic_energy(kinetic_energy: float, mass: float) -> float:
        """
        Calculate velocity from kinetic energy: v = √(2 * KE / m)
        
        :param kinetic_energy: Kinetic energy in Joules
        :param mass: Mass in kg
        :return: Velocity in m/s
        """
        if mass == 0:
            raise ValueError("Mass cannot be zero")
        if kinetic_energy < 0:
            raise ValueError("Kinetic energy cannot be negative")
        return math.sqrt(2 * kinetic_energy / mass)
    
    @staticmethod
    def velocity_components_from_ke_2d(kinetic_energy: float, mass: float, 
                                       angle: float) -> Tuple[float, float]:
        """
        Calculate velocity components in 2D given KE and direction angle.
        
        :param kinetic_energy: Kinetic energy in Joules
        :param mass: Mass in kg
        :param angle: Direction angle in degrees
        :return: Tuple of (vx, vy)
        """
        velocity = KineticEnergyCalculator.velocity_from_kinetic_energy(kinetic_energy, mass)
        angle_rad = math.radians(angle)
        vx = velocity * math.cos(angle_rad)
        vy = velocity * math.sin(angle_rad)
        return vx, vy
    
    @staticmethod
    def velocity_components_from_ke_3d(kinetic_energy: float, mass: float, 
                                       theta: float, phi: float) -> Tuple[float, float, float]:
        """
        Calculate velocity components in 3D (spherical coordinates).
        
        :param kinetic_energy: Kinetic energy in Joules
        :param mass: Mass in kg
        :param theta: Polar angle in degrees
        :param phi: Azimuthal angle in degrees
        :return: Tuple of (vx, vy, vz)
        """
        velocity = KineticEnergyCalculator.velocity_from_kinetic_energy(kinetic_energy, mass)
        theta_rad = math.radians(theta)
        phi_rad = math.radians(phi)
        
        vx = velocity * math.sin(theta_rad) * math.cos(phi_rad)
        vy = velocity * math.sin(theta_rad) * math.sin(phi_rad)
        vz = velocity * math.cos(theta_rad)
        return vx, vy, vz
    
    # ==================== MASS FROM KINETIC ENERGY ====================
    
    @staticmethod
    def mass_from_kinetic_energy(kinetic_energy: float, velocity: float) -> float:
        """
        Calculate mass from kinetic energy: m = 2 * KE / v²
        
        :param kinetic_energy: Kinetic energy in Joules
        :param velocity: Velocity in m/s
        :return: Mass in kg
        """
        if velocity == 0:
            raise ValueError("Velocity cannot be zero")
        return 2 * kinetic_energy / (velocity ** 2)
    
    # ==================== MOMENTUM & KINETIC ENERGY ====================
    
    @staticmethod
    def kinetic_energy_from_momentum(momentum: float, mass: float) -> float:
        """
        Calculate KE from momentum: KE = p² / (2m)
        
        :param momentum: Momentum in kg⋅m/s
        :param mass: Mass in kg
        :return: Kinetic energy in Joules
        """
        if mass == 0:
            raise ValueError("Mass cannot be zero")
        return (momentum ** 2) / (2 * mass)
    
    @staticmethod
    def momentum_from_kinetic_energy(kinetic_energy: float, mass: float) -> float:
        """
        Calculate momentum from kinetic energy: p = √(2 * m * KE)
        
        :param kinetic_energy: Kinetic energy in Joules
        :param mass: Mass in kg
        :return: Momentum in kg⋅m/s
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if kinetic_energy < 0:
            raise ValueError("Kinetic energy cannot be negative")
        return math.sqrt(2 * mass * kinetic_energy)
    
    @staticmethod
    def kinetic_energy_from_momentum_velocity(momentum: float, velocity: float) -> float:
        """
        Calculate KE from momentum and velocity: KE = (1/2) * p * v
        
        :param momentum: Momentum in kg⋅m/s
        :param velocity: Velocity in m/s
        :return: Kinetic energy in Joules
        """
        return 0.5 * momentum * velocity
    
    @staticmethod
    def momentum_magnitude(mass: float, velocity: float) -> float:
        """
        Calculate momentum magnitude: p = m * v
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Momentum in kg⋅m/s
        """
        return mass * velocity
    
    # ==================== KINETIC ENERGY IN COLLISIONS ====================
    
    @staticmethod
    def elastic_collision_kinetic_energy(m1: float, v1: float, 
                                        m2: float, v2: float) -> Tuple[float, float]:
        """
        Calculate final velocities in elastic collision.
        Returns kinetic energies before and after.
        
        :param m1: Mass 1 in kg
        :param v1: Velocity 1 in m/s
        :param m2: Mass 2 in kg
        :param v2: Velocity 2 in m/s
        :return: Tuple of (initial_KE, final_KE)
        """
        ke_initial = KineticEnergyCalculator.kinetic_energy(m1, v1) + \
                     KineticEnergyCalculator.kinetic_energy(m2, v2)
        
        # Calculate final velocities using conservation of momentum and energy
        v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
        
        ke_final = KineticEnergyCalculator.kinetic_energy(m1, v1_final) + \
                   KineticEnergyCalculator.kinetic_energy(m2, v2_final)
        
        return ke_initial, ke_final
    
    @staticmethod
    def inelastic_collision_kinetic_energy(m1: float, v1: float, 
                                          m2: float, v2: float) -> Tuple[float, float, float]:
        """
        Calculate kinetic energy loss in inelastic collision.
        Objects stick together after collision.
        
        :param m1: Mass 1 in kg
        :param v1: Velocity 1 in m/s
        :param m2: Mass 2 in kg
        :param v2: Velocity 2 in m/s
        :return: Tuple of (initial_KE, final_KE, energy_lost)
        """
        ke_initial = KineticEnergyCalculator.kinetic_energy(m1, v1) + \
                     KineticEnergyCalculator.kinetic_energy(m2, v2)
        
        # Conservation of momentum
        v_final = (m1 * v1 + m2 * v2) / (m1 + m2)
        
        ke_final = KineticEnergyCalculator.kinetic_energy(m1 + m2, v_final)
        energy_lost = ke_initial - ke_final
        
        return ke_initial, ke_final, energy_lost
    
    @staticmethod
    def collision_coefficient_of_restitution(m1: float, v1_initial: float, 
                                             m2: float, v2_initial: float,
                                             v1_final: float, v2_final: float) -> float:
        """
        Calculate coefficient of restitution from velocities.
        e = (v2_final - v1_final) / (v1_initial - v2_initial)
        
        :param m1: Mass 1 in kg
        :param v1_initial: Initial velocity 1 in m/s
        :param m2: Mass 2 in kg
        :param v2_initial: Initial velocity 2 in m/s
        :param v1_final: Final velocity 1 in m/s
        :param v2_final: Final velocity 2 in m/s
        :return: Coefficient of restitution (0-1)
        """
        if v1_initial == v2_initial:
            return 0
        return (v2_final - v1_final) / (v1_initial - v2_initial)
    
    # ==================== ROTATIONAL KINETIC ENERGY ====================
    
    @staticmethod
    def rotational_kinetic_energy(moment_of_inertia: float, angular_velocity: float) -> float:
        """
        Calculate rotational kinetic energy: KE_rot = (1/2) * I * ω²
        
        :param moment_of_inertia: Moment of inertia in kg⋅m²
        :param angular_velocity: Angular velocity in rad/s
        :return: Rotational kinetic energy in Joules
        """
        return 0.5 * moment_of_inertia * (angular_velocity ** 2)
    
    @staticmethod
    def moment_of_inertia_sphere(mass: float, radius: float) -> float:
        """
        Calculate moment of inertia for solid sphere: I = (2/5) * m * r²
        
        :param mass: Mass in kg
        :param radius: Radius in meters
        :return: Moment of inertia in kg⋅m²
        """
        return (2/5) * mass * (radius ** 2)
    
    @staticmethod
    def moment_of_inertia_cylinder(mass: float, radius: float) -> float:
        """
        Calculate moment of inertia for solid cylinder: I = (1/2) * m * r²
        
        :param mass: Mass in kg
        :param radius: Radius in meters
        :return: Moment of inertia in kg⋅m²
        """
        return 0.5 * mass * (radius ** 2)
    
    @staticmethod
    def moment_of_inertia_disk(mass: float, radius: float) -> float:
        """
        Calculate moment of inertia for disk: I = (1/2) * m * r²
        
        :param mass: Mass in kg
        :param radius: Radius in meters
        :return: Moment of inertia in kg⋅m²
        """
        return 0.5 * mass * (radius ** 2)
    
    @staticmethod
    def moment_of_inertia_rod(mass: float, length: float) -> float:
        """
        Calculate moment of inertia for rod (rotating about center): I = (1/12) * m * L²
        
        :param mass: Mass in kg
        :param length: Length in meters
        :return: Moment of inertia in kg⋅m²
        """
        return (1/12) * mass * (length ** 2)
    
    @staticmethod
    def moment_of_inertia_rod_end(mass: float, length: float) -> float:
        """
        Calculate moment of inertia for rod (rotating about end): I = (1/3) * m * L²
        
        :param mass: Mass in kg
        :param length: Length in meters
        :return: Moment of inertia in kg⋅m²
        """
        return (1/3) * mass * (length ** 2)
    
    @staticmethod
    def angular_velocity_from_rotational_ke(kinetic_energy: float, moment_of_inertia: float) -> float:
        """
        Calculate angular velocity from rotational KE.
        ω = √(2 * KE_rot / I)
        
        :param kinetic_energy: Rotational kinetic energy in Joules
        :param moment_of_inertia: Moment of inertia in kg⋅m²
        :return: Angular velocity in rad/s
        """
        if moment_of_inertia == 0:
            raise ValueError("Moment of inertia cannot be zero")
        return math.sqrt(2 * kinetic_energy / moment_of_inertia)
    
    @staticmethod
    def total_kinetic_energy(mass: float, velocity: float, 
                            moment_of_inertia: float, angular_velocity: float) -> float:
        """
        Calculate total kinetic energy (translational + rotational).
        
        :param mass: Mass in kg
        :param velocity: Linear velocity in m/s
        :param moment_of_inertia: Moment of inertia in kg⋅m²
        :param angular_velocity: Angular velocity in rad/s
        :return: Total kinetic energy in Joules
        """
        ke_trans = KineticEnergyCalculator.kinetic_energy(mass, velocity)
        ke_rot = KineticEnergyCalculator.rotational_kinetic_energy(moment_of_inertia, 
                                                                   angular_velocity)
        return ke_trans + ke_rot
    
    # ==================== RELATIVISTIC KINETIC ENERGY ====================
    
    @staticmethod
    def relativistic_kinetic_energy(mass: float, velocity: float) -> float:
        """
        Calculate kinetic energy with relativistic correction.
        KE = (γ - 1) * m * c²
        where γ = 1 / √(1 - v²/c²)
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Kinetic energy in Joules
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        if velocity >= c:
            raise ValueError("Velocity cannot exceed speed of light")
        
        gamma = 1 / math.sqrt(1 - (velocity / c) ** 2)
        return (gamma - 1) * mass * (c ** 2)
    
    @staticmethod
    def lorentz_factor(velocity: float) -> float:
        """
        Calculate Lorentz factor: γ = 1 / √(1 - v²/c²)
        
        :param velocity: Velocity in m/s
        :return: Lorentz factor
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        if velocity >= c:
            raise ValueError("Velocity cannot exceed speed of light")
        return 1 / math.sqrt(1 - (velocity / c) ** 2)
    
    @staticmethod
    def relativistic_momentum(mass: float, velocity: float) -> float:
        """
        Calculate relativistic momentum: p = γ * m * v
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Momentum in kg⋅m/s
        """
        gamma = KineticEnergyCalculator.lorentz_factor(velocity)
        return gamma * mass * velocity
    
    @staticmethod
    def relativistic_total_energy(mass: float, velocity: float) -> float:
        """
        Calculate total relativistic energy: E = γ * m * c²
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Total energy in Joules
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        gamma = KineticEnergyCalculator.lorentz_factor(velocity)
        return gamma * mass * (c ** 2)
    
    @staticmethod
    def rest_energy(mass: float) -> float:
        """
        Calculate rest energy: E₀ = m * c²
        
        :param mass: Mass in kg
        :return: Rest energy in Joules
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        return mass * (c ** 2)
    
    @staticmethod
    def velocity_from_relativistic_energy(total_energy: float, mass: float) -> float:
        """
        Calculate velocity from relativistic total energy.
        
        :param total_energy: Total energy in Joules
        :param mass: Mass in kg
        :return: Velocity in m/s
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        rest_E = mass * (c ** 2)
        
        if total_energy < rest_E:
            raise ValueError("Total energy must be at least rest energy")
        
        # From E = γ * m * c², solve for v
        gamma = total_energy / rest_E
        velocity = c * math.sqrt(1 - 1/gamma**2)
        return velocity
    
    @staticmethod
    def relativistic_kinetic_energy_momentum(momentum: float, mass: float) -> float:
        """
        Calculate KE from relativistic momentum using energy-momentum relation.
        E² = (pc)² + (mc²)²
        
        :param momentum: Momentum in kg⋅m/s
        :param mass: Mass in kg
        :return: Kinetic energy in Joules
        """
        c = KineticEnergyCalculator.SPEED_OF_LIGHT
        rest_E = mass * (c ** 2)
        total_E = math.sqrt((momentum * c) ** 2 + rest_E ** 2)
        return total_E - rest_E
    
    # ==================== KINETIC ENERGY IN REFERENCE FRAMES ====================
    
    @staticmethod
    def kinetic_energy_moving_frame(mass: float, velocity_object: float, 
                                   velocity_frame: float) -> float:
        """
        Calculate kinetic energy in a moving reference frame.
        v_relative = v_object - v_frame
        
        :param mass: Mass in kg
        :param velocity_object: Velocity of object in m/s
        :param velocity_frame: Velocity of reference frame in m/s
        :return: Kinetic energy in moving frame in Joules
        """
        relative_velocity = velocity_object - velocity_frame
        return KineticEnergyCalculator.kinetic_energy(mass, abs(relative_velocity))
    
    @staticmethod
    def kinetic_energy_center_of_mass(objects: List[KineticObject]) -> float:
        """
        Calculate kinetic energy in center-of-mass frame.
        
        :param objects: List of KineticObject instances
        :return: Total kinetic energy in CM frame
        """
        # Calculate center of mass velocity
        total_mass = sum(obj.mass for obj in objects)
        if total_mass == 0:
            return 0
        
        vcm = sum(obj.mass * obj.velocity for obj in objects) / total_mass
        
        # Calculate KE in CM frame
        ke_cm = 0
        for obj in objects:
            relative_velocity = obj.velocity - vcm
            ke_cm += KineticEnergyCalculator.kinetic_energy(obj.mass, abs(relative_velocity))
        
        return ke_cm
    
    @staticmethod
    def kinetic_energy_lab_frame(objects: List[KineticObject]) -> float:
        """
        Calculate total kinetic energy in lab frame.
        
        :param objects: List of KineticObject instances
        :return: Total kinetic energy
        """
        return sum(KineticEnergyCalculator.kinetic_energy(obj.mass, obj.velocity) 
                   for obj in objects)
    
    # ==================== KINETIC ENERGY CONVERSIONS ====================
    
    ENERGY_CONVERSIONS = {
        ('joules', 'calories'): 1 / 4.184,
        ('calories', 'joules'): 4.184,
        ('joules', 'kilowatt_hours'): 1 / 3.6e6,
        ('kilowatt_hours', 'joules'): 3.6e6,
        ('joules', 'electron_volts'): 1 / 1.602176634e-19,
        ('electron_volts', 'joules'): 1.602176634e-19,
        ('joules', 'foot_pounds'): 1 / 1.355817948,
        ('foot_pounds', 'joules'): 1.355817948,
        ('joules', 'BTU'): 1 / 1055.0559,
        ('BTU', 'joules'): 1055.0559,
        ('joules', 'erg'): 1e7,
        ('erg', 'joules'): 1e-7,
    }
    
    @staticmethod
    def convert_kinetic_energy(energy: float, from_unit: str, to_unit: str) -> float:
        """
        Convert kinetic energy between different units.
        
        :param energy: Energy value
        :param from_unit: Source unit
        :param to_unit: Target unit
        :return: Converted energy value
        """
        key = (from_unit, to_unit)
        if key in KineticEnergyCalculator.ENERGY_CONVERSIONS:
            return energy * KineticEnergyCalculator.ENERGY_CONVERSIONS[key]
        else:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")
    
    # ==================== KINETIC ENERGY IN FLUIDS ====================
    
    @staticmethod
    def kinetic_energy_fluid_flow(density: float, volume_flow_rate: float, 
                                 velocity: float) -> float:
        """
        Calculate kinetic energy in fluid flow.
        KE = (1/2) * ρ * V * v²
        
        :param density: Fluid density in kg/m³
        :param volume_flow_rate: Volume flow rate in m³/s
        :param velocity: Flow velocity in m/s
        :return: Kinetic energy in Joules/second (Power)
        """
        return 0.5 * density * volume_flow_rate * (velocity ** 2)
    
    @staticmethod
    def kinetic_energy_pressure_head(velocity: float) -> float:
        """
        Calculate kinetic head (pressure equivalent of KE).
        h = v² / (2g)
        
        :param velocity: Velocity in m/s
        :return: Kinetic head in meters
        """
        g = 9.81
        return (velocity ** 2) / (2 * g)
    
    @staticmethod
    def dynamic_pressure(density: float, velocity: float) -> float:
        """
        Calculate dynamic pressure: q = (1/2) * ρ * v²
        
        :param density: Fluid density in kg/m³
        :param velocity: Velocity in m/s
        :return: Dynamic pressure in Pa
        """
        return 0.5 * density * (velocity ** 2)
    
    @staticmethod
    def velocity_from_dynamic_pressure(dynamic_pressure: float, density: float) -> float:
        """
        Calculate velocity from dynamic pressure.
        
        :param dynamic_pressure: Dynamic pressure in Pa
        :param density: Fluid density in kg/m³
        :return: Velocity in m/s
        """
        if density == 0:
            raise ValueError("Density cannot be zero")
        return math.sqrt(2 * dynamic_pressure / density)
    
    # ==================== WORK-ENERGY THEOREM ====================
    
    @staticmethod
    def work_energy_theorem(initial_ke: float, final_ke: float) -> float:
        """
        Apply work-energy theorem: W = ΔKE = KE_final - KE_initial
        
        :param initial_ke: Initial kinetic energy in Joules
        :param final_ke: Final kinetic energy in Joules
        :return: Work done in Joules
        """
        return final_ke - initial_ke
    
    @staticmethod
    def kinetic_energy_from_work(initial_ke: float, work_done: float) -> float:
        """
        Calculate final kinetic energy from work done.
        KE_final = KE_initial + W
        
        :param initial_ke: Initial kinetic energy in Joules
        :param work_done: Work done on object in Joules
        :return: Final kinetic energy in Joules
        """
        final_ke = initial_ke + work_done
        if final_ke < 0:
            raise ValueError("Final kinetic energy cannot be negative")
        return final_ke
    
    @staticmethod
    def work_from_force_distance(force: float, distance: float, angle: float = 0) -> float:
        """
        Calculate work from force and distance.
        W = F * d * cos(θ)
        
        :param force: Force in Newtons
        :param distance: Distance in meters
        :param angle: Angle between force and displacement in degrees
        :return: Work in Joules
        """
        angle_rad = math.radians(angle)
        return force * distance * math.cos(angle_rad)
    
    # ==================== KINETIC ENERGY & POWER ====================
    
    @staticmethod
    def power_from_kinetic_energy_change(delta_ke: float, time: float) -> float:
        """
        Calculate power from kinetic energy change.
        P = ΔKE / Δt
        
        :param delta_ke: Change in kinetic energy in Joules
        :param time: Time interval in seconds
        :return: Power in Watts
        """
        if time == 0:
            raise ValueError("Time cannot be zero")
        return delta_ke / time
    
    @staticmethod
    def power_from_force_velocity(force: float, velocity: float) -> float:
        """
        Calculate power from force and velocity.
        P = F * v
        
        :param force: Force in Newtons
        :param velocity: Velocity in m/s
        :return: Power in Watts
        """
        return force * velocity
    
    @staticmethod
    def acceleration_from_power_velocity(power: float, velocity: float, mass: float) -> float:
        """
        Calculate acceleration from power, velocity, and mass.
        a = P / (m * v)
        
        :param power: Power in Watts
        :param velocity: Velocity in m/s
        :param mass: Mass in kg
        :return: Acceleration in m/s²
        """
        if velocity == 0 or mass == 0:
            raise ValueError("Velocity and mass cannot be zero")
        return power / (mass * velocity)
    
    # ==================== KINETIC ENERGY IN WAVES ====================
    
    @staticmethod
    def kinetic_energy_wave(mass: float, amplitude: float, 
                           frequency: float, position: float, time: float) -> float:
        """
        Calculate instantaneous kinetic energy in a harmonic wave.
        
        :param mass: Total mass in kg
        :param amplitude: Wave amplitude in meters
        :param frequency: Frequency in Hz
        :param position: Position in wave
        :param time: Time in seconds
        :return: Instantaneous kinetic energy
        """
        omega = 2 * math.pi * frequency
        # Velocity in wave: v = -Aω * sin(kx - ωt)
        velocity_amplitude = amplitude * omega
        velocity = velocity_amplitude * math.cos(omega * time)
        return KineticEnergyCalculator.kinetic_energy(mass, abs(velocity))
    
    @staticmethod
    def average_kinetic_energy_wave(mass: float, amplitude: float, frequency: float) -> float:
        """
        Calculate average kinetic energy in a harmonic wave.
        <KE> = (1/4) * m * (Aω)²
        
        :param mass: Total mass in kg
        :param amplitude: Wave amplitude in meters
        :param frequency: Frequency in Hz
        :return: Average kinetic energy
        """
        omega = 2 * math.pi * frequency
        return 0.25 * mass * (amplitude * omega) ** 2
    
    @staticmethod
    def total_wave_energy(mass: float, amplitude: float, frequency: float) -> float:
        """
        Calculate total mechanical energy in wave.
        E_total = (1/2) * m * (Aω)²
        
        :param mass: Total mass in kg
        :param amplitude: Wave amplitude in meters
        :param frequency: Frequency in Hz
        :return: Total energy
        """
        omega = 2 * math.pi * frequency
        return 0.5 * mass * (amplitude * omega) ** 2
    
    # ==================== KINETIC ENERGY & TEMPERATURE ====================
    
    @staticmethod
    def average_kinetic_energy_particle(temperature: float, 
                                       degrees_of_freedom: int = 3) -> float:
        """
        Calculate average kinetic energy of particle from temperature.
        <KE> = (f/2) * k_B * T
        
        :param temperature: Temperature in Kelvin
        :param degrees_of_freedom: Degrees of freedom (3 for translation, +2 for rotation, etc.)
        :return: Average kinetic energy in Joules
        """
        k_B = KineticEnergyCalculator.BOLTZMANN_CONSTANT
        return (degrees_of_freedom / 2) * k_B * temperature
    
    @staticmethod
    def temperature_from_kinetic_energy(avg_kinetic_energy: float, 
                                       degrees_of_freedom: int = 3) -> float:
        """
        Calculate temperature from average kinetic energy.
        
        :param avg_kinetic_energy: Average kinetic energy in Joules
        :param degrees_of_freedom: Degrees of freedom
        :return: Temperature in Kelvin
        """
        k_B = KineticEnergyCalculator.BOLTZMANN_CONSTANT
        return (2 * avg_kinetic_energy) / (degrees_of_freedom * k_B)
    
    @staticmethod
    def rms_velocity(temperature: float, mass_particle: float) -> float:
        """
        Calculate root-mean-square velocity from temperature.
        v_rms = √(3 * k_B * T / m)
        
        :param temperature: Temperature in Kelvin
        :param mass_particle: Particle mass in kg
        :return: RMS velocity in m/s
        """
        k_B = KineticEnergyCalculator.BOLTZMANN_CONSTANT
        if mass_particle == 0:
            raise ValueError("Particle mass cannot be zero")
        return math.sqrt(3 * k_B * temperature / mass_particle)
    
    @staticmethod
    def thermal_kinetic_energy(num_particles: float, temperature: float, 
                              degrees_of_freedom: int = 3) -> float:
        """
        Calculate total thermal kinetic energy of system.
        
        :param num_particles: Number of particles
        :param temperature: Temperature in Kelvin
        :param degrees_of_freedom: Degrees of freedom per particle
        :return: Total thermal kinetic energy in Joules
        """
        return num_particles * KineticEnergyCalculator.average_kinetic_energy_particle(
            temperature, degrees_of_freedom)
    
    # ==================== KINETIC ENERGY EFFICIENCY ====================
    
    @staticmethod
    def kinetic_energy_efficiency(useful_ke: float, total_input_ke: float) -> float:
        """
        Calculate kinetic energy efficiency.
        η = (Useful KE / Input KE) * 100%
        
        :param useful_ke: Useful kinetic energy in Joules
        :param total_input_ke: Total input kinetic energy in Joules
        :return: Efficiency as percentage
        """
        if total_input_ke == 0:
            raise ValueError("Total input cannot be zero")
        return (useful_ke / total_input_ke) * 100
    
    @staticmethod
    def kinetic_energy_loss(initial_ke: float, final_ke: float) -> float:
        """
        Calculate kinetic energy loss (dissipation).
        
        :param initial_ke: Initial kinetic energy in Joules
        :param final_ke: Final kinetic energy in Joules
        :return: Energy loss in Joules
        """
        loss = initial_ke - final_ke
        if loss < 0:
            raise ValueError("Energy loss cannot be negative")
        return loss
    
    @staticmethod
    def kinetic_energy_loss_percentage(initial_ke: float, final_ke: float) -> float:
        """
        Calculate percentage of kinetic energy lost.
        
        :param initial_ke: Initial kinetic energy in Joules
        :param final_ke: Final kinetic energy in Joules
        :return: Percentage lost
        """
        if initial_ke == 0:
            return 0
        loss = KineticEnergyCalculator.kinetic_energy_loss(initial_ke, final_ke)
        return (loss / initial_ke) * 100
    
    # ==================== KINETIC ENERGY DENSITY ====================
    
    @staticmethod
    def kinetic_energy_density_volume(mass: float, velocity: float, volume: float) -> float:
        """
        Calculate kinetic energy density per unit volume.
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :param volume: Volume in m³
        :return: KE density in J/m³
        """
        if volume == 0:
            raise ValueError("Volume cannot be zero")
        ke = KineticEnergyCalculator.kinetic_energy(mass, velocity)
        return ke / volume
    
    @staticmethod
    def kinetic_energy_density_mass(velocity: float) -> float:
        """
        Calculate kinetic energy density per unit mass.
        
        :param velocity: Velocity in m/s
        :return: KE density in J/kg
        """
        return 0.5 * (velocity ** 2)
    
    # ==================== KINETIC ENERGY ANALYSIS ====================
    
    
class CollisionAnalyzer:
    """Analyze kinetic energy in collisions."""
    
    @staticmethod
    def analyze_elastic_collision(m1: float, v1: float, m2: float, v2: float) -> Dict:
        """Complete analysis of elastic collision."""
        ke_initial, ke_final = KineticEnergyCalculator.elastic_collision_kinetic_energy(
            m1, v1, m2, v2)
        
        return {
            'initial_ke': ke_initial,
            'final_ke': ke_final,
            'ke_conserved': abs(ke_final - ke_initial) < 1e-6,
            'energy_loss': ke_initial - ke_final,
            'loss_percentage': ((ke_initial - ke_final) / ke_initial * 100) if ke_initial > 0 else 0,
        }
    
    @staticmethod
    def analyze_inelastic_collision(m1: float, v1: float, m2: float, v2: float) -> Dict:
        """Complete analysis of inelastic collision."""
        ke_initial, ke_final, energy_lost = KineticEnergyCalculator.inelastic_collision_kinetic_energy(
            m1, v1, m2, v2)
        
        return {
            'initial_ke': ke_initial,
            'final_ke': ke_final,
            'energy_lost': energy_lost,
            'loss_percentage': (energy_lost / ke_initial * 100) if ke_initial > 0 else 0,
            'coefficient_restitution': 0,  # Perfectly inelastic
        }


class RotationalKineticEnergyAnalyzer:
    """Analyze rotational kinetic energy."""
    
    @staticmethod
    def analyze_rolling_object(mass: float, velocity: float, radius: float) -> Dict:
        """Analyze kinetic energy of rolling object."""
        moi = KineticEnergyCalculator.moment_of_inertia_sphere(mass, radius)
        angular_velocity = velocity / radius
        
        ke_trans = KineticEnergyCalculator.kinetic_energy(mass, velocity)
        ke_rot = KineticEnergyCalculator.rotational_kinetic_energy(moi, angular_velocity)
        ke_total = ke_trans + ke_rot
        
        return {
            'translational_ke': ke_trans,
            'rotational_ke': ke_rot,
            'total_ke': ke_total,
            'ke_ratio': ke_rot / ke_trans if ke_trans > 0 else 0,
            'moment_of_inertia': moi,
            'angular_velocity': angular_velocity,
        }


