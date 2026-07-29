from .energy_importer import *

class MechanicalEnergy:
    """
    Comprehensive class for calculating and analyzing mechanical energy.
    Covers kinetic energy, potential energy, work, power, and energy conservation.
    """
    
    # Physical Constants
    GRAVITY = 9.81  # m/s² (standard Earth gravity)
    GRAVITY_MOON = 1.62  # m/s² (Moon gravity)
    GRAVITY_MARS = 3.71  # m/s² (Mars gravity)
    
    def __init__(self, gravity=GRAVITY):
        """Initialize with custom gravity value if needed."""
        self.gravity = gravity
    
    # ==================== KINETIC ENERGY ====================
    
    @staticmethod
    def kinetic_energy(mass, velocity):
        """
        Calculate kinetic energy: KE = 1/2 * m * v²
        
        :param mass: Mass in kg
        :param velocity: Velocity in m/s
        :return: Kinetic energy in Joules
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if velocity < 0:
            raise ValueError("Velocity magnitude cannot be negative")
        
        return 0.5 * mass * velocity ** 2
    
    @staticmethod
    def kinetic_energy_from_momentum(momentum, mass):
        """
        Calculate kinetic energy from momentum.
        KE = p² / (2m), where p is momentum
        
        :param momentum: Momentum (kg·m/s)
        :param mass: Mass (kg)
        :return: Kinetic energy (Joules)
        """
        if mass <= 0:
            raise ValueError("Mass must be positive")
        
        return (momentum ** 2) / (2 * mass)
    
    @staticmethod
    def velocity_from_kinetic_energy(kinetic_energy, mass):
        """
        Find velocity given kinetic energy.
        v = √(2·KE / m)
        
        :param kinetic_energy: Kinetic energy (Joules)
        :param mass: Mass (kg)
        :return: Velocity (m/s)
        """
        if kinetic_energy < 0:
            raise ValueError("Kinetic energy cannot be negative")
        if mass <= 0:
            raise ValueError("Mass must be positive")
        
        return math.sqrt((2 * kinetic_energy) / mass)
    
    @staticmethod
    def mass_from_kinetic_energy(kinetic_energy, velocity):
        """
        Find mass given kinetic energy and velocity.
        m = 2·KE / v²
        
        :param kinetic_energy: Kinetic energy (Joules)
        :param velocity: Velocity (m/s)
        :return: Mass (kg)
        """
        if velocity == 0:
            raise ValueError("Velocity cannot be zero")
        if kinetic_energy < 0:
            raise ValueError("Kinetic energy cannot be negative")
        
        return (2 * kinetic_energy) / (velocity ** 2)
    
    # ==================== ROTATIONAL KINETIC ENERGY ====================
    
    @staticmethod
    def rotational_kinetic_energy(moment_of_inertia, angular_velocity):
        """
        Calculate rotational kinetic energy: KE_rot = 1/2 * I * ω²
        
        :param moment_of_inertia: Moment of inertia (kg·m²)
        :param angular_velocity: Angular velocity (rad/s)
        :return: Rotational kinetic energy (Joules)
        """
        if moment_of_inertia < 0:
            raise ValueError("Moment of inertia cannot be negative")
        
        return 0.5 * moment_of_inertia * angular_velocity ** 2
    
    @staticmethod
    def angular_velocity_from_rotational_ke(rotational_ke, moment_of_inertia):
        """
        Find angular velocity from rotational KE.
        ω = √(2·KE_rot / I)
        
        :param rotational_ke: Rotational kinetic energy (Joules)
        :param moment_of_inertia: Moment of inertia (kg·m²)
        :return: Angular velocity (rad/s)
        """
        if moment_of_inertia <= 0:
            raise ValueError("Moment of inertia must be positive")
        
        return math.sqrt((2 * rotational_ke) / moment_of_inertia)
    
    # Moment of Inertia for common shapes
    @staticmethod
    def moment_of_inertia_solid_sphere(mass, radius):
        """I = 2/5 * m * r²"""
        return (2/5) * mass * radius ** 2
    
    @staticmethod
    def moment_of_inertia_hollow_sphere(mass, radius):
        """I = 2/3 * m * r²"""
        return (2/3) * mass * radius ** 2
    
    @staticmethod
    def moment_of_inertia_solid_cylinder(mass, radius):
        """I = 1/2 * m * r²"""
        return 0.5 * mass * radius ** 2
    
    @staticmethod
    def moment_of_inertia_hollow_cylinder(mass, radius):
        """I = m * r²"""
        return mass * radius ** 2
    
    @staticmethod
    def moment_of_inertia_rod_center(mass, length):
        """I = 1/12 * m * L²"""
        return (1/12) * mass * length ** 2
    
    @staticmethod
    def moment_of_inertia_rod_end(mass, length):
        """I = 1/3 * m * L²"""
        return (1/3) * mass * length ** 2
    
    @staticmethod
    def moment_of_inertia_disk(mass, radius):
        """I = 1/2 * m * r²"""
        return 0.5 * mass * radius ** 2
    
    @staticmethod
    def moment_of_inertia_ring(mass, radius):
        """I = m * r²"""
        return mass * radius ** 2
    
    @staticmethod
    def total_kinetic_energy_rolling(mass, velocity, moment_of_inertia, radius):
        """
        Total KE for rolling object: KE_total = 1/2*m*v² + 1/2*I*ω²
        For rolling without slipping: v = ω*r, so ω = v/r
        
        :param mass: Mass (kg)
        :param velocity: Linear velocity (m/s)
        :param moment_of_inertia: Moment of inertia (kg·m²)
        :param radius: Radius (m)
        :return: Total kinetic energy (Joules)
        """
        if radius == 0:
            raise ValueError("Radius cannot be zero")
        
        translational_ke = 0.5 * mass * velocity ** 2
        angular_velocity = velocity / radius
        rotational_ke = 0.5 * moment_of_inertia * angular_velocity ** 2
        
        return translational_ke + rotational_ke
    
    # ==================== GRAVITATIONAL POTENTIAL ENERGY ====================
    
    def gravitational_potential_energy(self, mass, height):
        """
        Calculate gravitational potential energy: PE = m * g * h
        
        :param mass: Mass in kg
        :param height: Height in m
        :return: Potential energy in Joules
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if height < 0:
            raise ValueError("Height cannot be negative")
        
        return mass * self.gravity * height
    
    @staticmethod
    def gravitational_potential_energy_exact(mass, earth_mass, radius):
        """
        Exact gravitational PE: PE = -G*M*m/r
        
        :param mass: Object mass (kg)
        :param earth_mass: Planet mass (kg)
        :param radius: Distance from center (m)
        :return: Potential energy (Joules)
        """
        G = 6.674e-11  # Gravitational constant
        return -(G * earth_mass * mass) / radius
    
    def height_from_potential_energy(self, potential_energy, mass):
        """
        Find height from potential energy: h = PE / (m * g)
        
        :param potential_energy: Potential energy (Joules)
        :param mass: Mass (kg)
        :return: Height (m)
        """
        if mass <= 0:
            raise ValueError("Mass must be positive")
        
        return potential_energy / (mass * self.gravity)
    
    def mass_from_potential_energy(self, potential_energy, height):
        """
        Find mass from potential energy: m = PE / (g * h)
        
        :param potential_energy: Potential energy (Joules)
        :param height: Height (m)
        :return: Mass (kg)
        """
        if height <= 0:
            raise ValueError("Height must be positive")
        
        return potential_energy / (self.gravity * height)
    
    # ==================== ELASTIC POTENTIAL ENERGY ====================
    
    @staticmethod
    def elastic_potential_energy(spring_constant, displacement):
        """
        Calculate elastic potential energy: PE = 1/2 * k * x²
        
        :param spring_constant: Spring constant (N/m)
        :param displacement: Displacement from equilibrium (m)
        :return: Elastic potential energy (Joules)
        """
        if spring_constant < 0:
            raise ValueError("Spring constant cannot be negative")
        
        return 0.5 * spring_constant * displacement ** 2
    
    @staticmethod
    def spring_constant_from_elastic_pe(elastic_pe, displacement):
        """
        Find spring constant: k = 2*PE / x²
        
        :param elastic_pe: Elastic potential energy (Joules)
        :param displacement: Displacement (m)
        :return: Spring constant (N/m)
        """
        if displacement == 0:
            raise ValueError("Displacement cannot be zero")
        
        return (2 * elastic_pe) / (displacement ** 2)
    
    @staticmethod
    def displacement_from_elastic_pe(elastic_pe, spring_constant):
        """
        Find displacement: x = √(2*PE / k)
        
        :param elastic_pe: Elastic potential energy (Joules)
        :param spring_constant: Spring constant (N/m)
        :return: Displacement (m)
        """
        if spring_constant <= 0:
            raise ValueError("Spring constant must be positive")
        
        return math.sqrt((2 * elastic_pe) / spring_constant)
    
    # ==================== TOTAL MECHANICAL ENERGY ====================
    
    def total_mechanical_energy(self, mass, velocity, height, 
                               spring_constant=0, displacement=0):
        """
        Calculate total mechanical energy: E = KE + PE_grav + PE_elastic
        
        :param mass: Mass (kg)
        :param velocity: Velocity (m/s)
        :param height: Height (m)
        :param spring_constant: Spring constant (N/m) - optional
        :param displacement: Displacement (m) - optional
        :return: Total mechanical energy (Joules)
        """
        ke = self.kinetic_energy(mass, velocity)
        pe_grav = self.gravitational_potential_energy(mass, height)
        pe_elastic = self.elastic_potential_energy(spring_constant, displacement)
        
        return ke + pe_grav + pe_elastic
    
    def total_mechanical_energy_with_rotation(self, mass, velocity, height,
                                             moment_of_inertia=0, angular_velocity=0):
        """
        Total mechanical energy including rotation.
        
        :param mass: Mass (kg)
        :param velocity: Linear velocity (m/s)
        :param height: Height (m)
        :param moment_of_inertia: Moment of inertia (kg·m²)
        :param angular_velocity: Angular velocity (rad/s)
        :return: Total mechanical energy (Joules)
        """
        ke_trans = self.kinetic_energy(mass, velocity)
        ke_rot = self.rotational_kinetic_energy(moment_of_inertia, angular_velocity)
        pe = self.gravitational_potential_energy(mass, height)
        
        return ke_trans + ke_rot + pe
    
    # ==================== ENERGY CONSERVATION ====================
    
    def check_energy_conservation(self, initial_energy, final_energy, tolerance=1e-6):
        """
        Check if mechanical energy is conserved (initial ≈ final).
        
        :param initial_energy: Initial total energy (Joules)
        :param final_energy: Final total energy (Joules)
        :param tolerance: Allowed difference (Joules)
        :return: True if energy conserved, False otherwise
        """
        difference = abs(initial_energy - final_energy)
        return difference <= tolerance
    
    def energy_conservation_analysis(self, initial_ke, initial_pe, 
                                     final_ke, final_pe):
        """
        Analyze energy conservation with detailed breakdown.
        
        :return: Dictionary with conservation info
        """
        initial_total = initial_ke + initial_pe
        final_total = final_ke + final_pe
        difference = abs(initial_total - final_total)
        percent_loss = (difference / initial_total) * 100 if initial_total > 0 else 0
        
        return {
            'initial_ke': initial_ke,
            'initial_pe': initial_pe,
            'initial_total': initial_total,
            'final_ke': final_ke,
            'final_pe': final_pe,
            'final_total': final_total,
            'energy_loss': difference,
            'percent_loss': percent_loss,
            'is_conserved': abs(difference) < 1e-6
        }
    
    # ==================== WORK & POWER ====================
    
    @staticmethod
    def work_by_force(force, displacement, angle=0):
        """
        Calculate work done by force: W = F * d * cos(θ)
        
        :param force: Force magnitude (N)
        :param displacement: Displacement magnitude (m)
        :param angle: Angle between force and displacement (degrees)
        :return: Work done (Joules)
        """
        angle_rad = math.radians(angle)
        return force * displacement * math.cos(angle_rad)
    
    @staticmethod
    def work_energy_theorem(initial_ke, final_ke):
        """
        Work-energy theorem: W_net = ΔKE = KE_final - KE_initial
        
        :param initial_ke: Initial kinetic energy (Joules)
        :param final_ke: Final kinetic energy (Joules)
        :return: Net work done (Joules)
        """
        return final_ke - initial_ke
    
    @staticmethod
    def power_average(work, time):
        """
        Calculate average power: P = W / t
        
        :param work: Work done (Joules)
        :param time: Time interval (seconds)
        :return: Average power (Watts)
        """
        if time <= 0:
            raise ValueError("Time must be positive")
        
        return work / time
    
    @staticmethod
    def power_instantaneous(force, velocity, angle=0):
        """
        Calculate instantaneous power: P = F·v = F*v*cos(θ)
        
        :param force: Force magnitude (N)
        :param velocity: Velocity magnitude (m/s)
        :param angle: Angle between force and velocity (degrees)
        :return: Instantaneous power (Watts)
        """
        angle_rad = math.radians(angle)
        return force * velocity * math.cos(angle_rad)
    
    @staticmethod
    def power_rotational(torque, angular_velocity):
        """
        Calculate rotational power: P = τ * ω
        
        :param torque: Torque (N·m)
        :param angular_velocity: Angular velocity (rad/s)
        :return: Power (Watts)
        """
        return torque * angular_velocity
    
    @staticmethod
    def energy_from_power(power, time):
        """
        Calculate energy from power: E = P * t
        
        :param power: Power (Watts)
        :param time: Time (seconds)
        :return: Energy (Joules)
        """
        return power * time
    
    # ==================== COLLISION ENERGY ====================
    
    @staticmethod
    def kinetic_energy_before_collision(mass1, velocity1, mass2, velocity2):
        """
        Total kinetic energy before collision.
        
        :param mass1: Mass of object 1 (kg)
        :param velocity1: Velocity of object 1 (m/s)
        :param mass2: Mass of object 2 (kg)
        :param velocity2: Velocity of object 2 (m/s)
        :return: Total KE before (Joules)
        """
        ke1 = 0.5 * mass1 * velocity1 ** 2
        ke2 = 0.5 * mass2 * velocity2 ** 2
        return ke1 + ke2
    
    @staticmethod
    def kinetic_energy_after_collision(mass1, velocity1_final, mass2, velocity2_final):
        """
        Total kinetic energy after collision.
        
        :param mass1: Mass of object 1 (kg)
        :param velocity1_final: Final velocity of object 1 (m/s)
        :param mass2: Mass of object 2 (kg)
        :param velocity2_final: Final velocity of object 2 (m/s)
        :return: Total KE after (Joules)
        """
        ke1 = 0.5 * mass1 * velocity1_final ** 2
        ke2 = 0.5 * mass2 * velocity2_final ** 2
        return ke1 + ke2
    
    @staticmethod
    def energy_lost_in_collision(ke_before, ke_after):
        """
        Calculate energy lost in collision.
        
        :param ke_before: KE before collision (Joules)
        :param ke_after: KE after collision (Joules)
        :return: Energy lost (Joules)
        """
        return ke_before - ke_after
    
    @staticmethod
    def coefficient_of_restitution_energy(ke_after, ke_before):
        """
        Estimate coefficient of restitution from energy ratio.
        
        :param ke_after: KE after collision
        :param ke_before: KE before collision
        :return: Approximate COR (0-1)
        """
        if ke_before == 0:
            return 0
        
        energy_ratio = ke_after / ke_before
        return math.sqrt(energy_ratio)
    
    # ==================== PROJECTILE MOTION ENERGY ====================
    
    def projectile_total_energy_at_launch(self, mass, velocity, angle_degrees, height=0):
        """
        Total mechanical energy at launch of projectile.
        
        :param mass: Mass (kg)
        :param velocity: Launch velocity (m/s)
        :param angle_degrees: Launch angle (degrees)
        :param height: Initial height (m)
        :return: Total energy (Joules)
        """
        ke = self.kinetic_energy(mass, velocity)
        pe = self.gravitational_potential_energy(mass, height)
        return ke + pe
    
    def projectile_velocity_at_height(self, initial_velocity, initial_height, final_height):
        """
        Find velocity at different height using energy conservation.
        
        :param initial_velocity: Initial velocity (m/s)
        :param initial_height: Initial height (m)
        :param final_height: Final height (m)
        :return: Velocity at final height (m/s)
        """
        # Energy conservation: v² = v₀² - 2g(h - h₀)
        # But we don't know mass, so work with energy per unit mass
        height_diff = final_height - initial_height
        
        velocity_squared = initial_velocity ** 2 - 2 * self.gravity * height_diff
        
        if velocity_squared < 0:
            raise ValueError("Object cannot reach this height")
        
        return math.sqrt(velocity_squared)
    
    def projectile_max_height_from_energy(self, mass, velocity, angle_degrees):
        """
        Find maximum height using energy conservation.
        
        :param mass: Mass (kg)
        :param velocity: Launch velocity (m/s)
        :param angle_degrees: Launch angle (degrees)
        :return: Maximum height (m)
        """
        angle_rad = math.radians(angle_degrees)
        vertical_velocity = velocity * math.sin(angle_rad)
        
        # At max height, all vertical KE becomes PE
        max_height = (vertical_velocity ** 2) / (2 * self.gravity)
        return max_height
    
    def projectile_range_energy_method(self, mass, velocity, angle_degrees):
        """
        Calculate range using energy (validates projectile motion).
        
        :param mass: Mass (kg)
        :param velocity: Velocity (m/s)
        :param angle_degrees: Launch angle (degrees)
        :return: Range (m)
        """
        angle_rad = math.radians(angle_degrees)
        
        # Range formula from kinematics
        range_x = (velocity ** 2 * math.sin(2 * angle_rad)) / self.gravity
        return range_x
    
    # ==================== SIMPLE HARMONIC MOTION ====================
    
    @staticmethod
    def shm_total_energy(mass, velocity, spring_constant, displacement):
        """
        Total energy in SHM: E = 1/2*m*v² + 1/2*k*x²
        
        :param mass: Mass (kg)
        :param velocity: Velocity (m/s)
        :param spring_constant: Spring constant (N/m)
        :param displacement: Displacement (m)
        :return: Total energy (Joules)
        """
        ke = 0.5 * mass * velocity ** 2
        pe = 0.5 * spring_constant * displacement ** 2
        return ke + pe
    
    @staticmethod
    def shm_amplitude_from_energy(total_energy, spring_constant):
        """
        Find amplitude in SHM: A = √(2*E / k)
        
        :param total_energy: Total energy (Joules)
        :param spring_constant: Spring constant (N/m)
        :return: Amplitude (m)
        """
        if spring_constant <= 0:
            raise ValueError("Spring constant must be positive")
        
        return math.sqrt((2 * total_energy) / spring_constant)
    
    @staticmethod
    def shm_max_velocity(amplitude, angular_frequency):
        """
        Maximum velocity in SHM: v_max = A * ω
        
        :param amplitude: Amplitude (m)
        :param angular_frequency: Angular frequency (rad/s)
        :return: Maximum velocity (m/s)
        """
        return amplitude * angular_frequency
    
    @staticmethod
    def shm_period_from_mass_spring(mass, spring_constant):
        """
        Period of mass-spring system: T = 2π√(m/k)
        
        :param mass: Mass (kg)
        :param spring_constant: Spring constant (N/m)
        :return: Period (seconds)
        """
        if spring_constant <= 0:
            raise ValueError("Spring constant must be positive")
        
        return 2 * math.pi * math.sqrt(mass / spring_constant)
    
    @staticmethod
    def shm_frequency_from_period(period):
        """
        Frequency: f = 1/T
        
        :param period: Period (seconds)
        :return: Frequency (Hz)
        """
        if period <= 0:
            raise ValueError("Period must be positive")
        
        return 1 / period
    
    # ==================== GRAVITATIONAL ORBITAL ENERGY ====================
    
    @staticmethod
    def orbital_kinetic_energy(mass, orbital_velocity):
        """
        KE of orbiting object: KE = 1/2 * m * v_orbit²
        
        :param mass: Orbiting object mass (kg)
        :param orbital_velocity: Orbital velocity (m/s)
        :return: Orbital KE (Joules)
        """
        return 0.5 * mass * orbital_velocity ** 2
    
    @staticmethod
    def orbital_velocity(central_mass, radius):
        """
        Orbital velocity: v = √(G*M/r)
        
        :param central_mass: Central body mass (kg)
        :param radius: Orbital radius (m)
        :return: Orbital velocity (m/s)
        """
        G = 6.674e-11
        return math.sqrt((G * central_mass) / radius)
    
    @staticmethod
    def orbital_period(central_mass, radius):
        """
        Orbital period (Kepler's 3rd law): T = 2π√(r³/GM)
        
        :param central_mass: Central body mass (kg)
        :param radius: Orbital radius (m)
        :return: Period (seconds)
        """
        G = 6.674e-11
        return 2 * math.pi * math.sqrt((radius ** 3) / (G * central_mass))
    
    @staticmethod
    def total_orbital_energy(mass, central_mass, radius):
        """
        Total orbital energy: E = -G*M*m/(2*r)
        (Negative indicates bound orbit)
        
        :param mass: Orbiting mass (kg)
        :param central_mass: Central mass (kg)
        :param radius: Orbital radius (m)
        :return: Total energy (Joules)
        """
        G = 6.674e-11
        return -(G * central_mass * mass) / (2 * radius)
    
    @staticmethod
    def escape_velocity(central_mass, radius):
        """
        Escape velocity: v_esc = √(2*G*M/r)
        
        :param central_mass: Central mass (kg)
        :param radius: Surface radius (m)
        :return: Escape velocity (m/s)
        """
        G = 6.674e-11
        return math.sqrt((2 * G * central_mass) / radius)
    
    @staticmethod
    def escape_energy(mass, central_mass, radius):
        """
        Energy needed to escape: E = G*M*m/r
        
        :param mass: Object mass (kg)
        :param central_mass: Central mass (kg)
        :param radius: Initial distance (m)
        :return: Escape energy (Joules)
        """
        G = 6.674e-11
        return (G * central_mass * mass) / radius
    
    # ==================== FLUID DYNAMICS ENERGY ====================
    
    @staticmethod
    def dynamic_pressure(density, velocity):
        """
        Dynamic pressure: q = 1/2 * ρ * v²
        
        :param density: Fluid density (kg/m³)
        :param velocity: Velocity (m/s)
        :return: Dynamic pressure (Pa)
        """
        return 0.5 * density * velocity ** 2
    
    @staticmethod
    def bernoulli_equation(pressure1, density, velocity1, height1, 
                          pressure2, velocity2, height2, gravity=9.81):
        """
        Bernoulli's equation (energy per unit volume):
        P + ρgh + 1/2ρv² = constant
        
        :param pressure1: Pressure at point 1 (Pa)
        :param density: Fluid density (kg/m³)
        :param velocity1: Velocity at point 1 (m/s)
        :param height1: Height at point 1 (m)
        :param pressure2: Pressure at point 2 (Pa)
        :param velocity2: Velocity at point 2 (m/s)
        :param height2: Height at point 2 (m)
        :param gravity: Gravity (m/s²)
        :return: True if Bernoulli satisfied, False otherwise
        """
        side1 = pressure1 + density * gravity * height1 + 0.5 * density * velocity1 ** 2
        side2 = pressure2 + density * gravity * height2 + 0.5 * density * velocity2 ** 2
        
        return abs(side1 - side2) < 1  # Small tolerance for rounding
    
    # ==================== ENERGY TRANSFORMATIONS ====================
    
    @staticmethod
    def efficiency(energy_output, energy_input):
        """
        Calculate efficiency: η = (E_out / E_in) * 100%
        
        :param energy_output: Useful energy output (Joules)
        :param energy_input: Total energy input (Joules)
        :return: Efficiency (percentage)
        """
        if energy_input == 0:
            raise ValueError("Energy input cannot be zero")
        
        return (energy_output / energy_input) * 100
    
    @staticmethod
    def energy_loss(energy_input, energy_output):
        """
        Calculate energy loss.
        
        :param energy_input: Input energy (Joules)
        :param energy_output: Output energy (Joules)
        :return: Energy loss (Joules)
        """
        return energy_input - energy_output
    
    @staticmethod
    def energy_loss_percentage(energy_input, energy_output):
        """
        Calculate energy loss as percentage.
        
        :param energy_input: Input energy (Joules)
        :param energy_output: Output energy (Joules)
        :return: Energy loss (percentage)
        """
        if energy_input == 0:
            return 0
        
        return ((energy_input - energy_output) / energy_input) * 100
    
    # ==================== FREE FALL & VERTICAL MOTION ====================
    
    def free_fall_velocity(self, height):
        """
        Velocity reached in free fall from height: v = √(2*g*h)
        
        :param height: Height (m)
        :return: Velocity (m/s)
        """
        return math.sqrt(2 * self.gravity * height)
    
    def free_fall_time(self, height):
        """
        Time to fall: t = √(2*h/g)
        
        :param height: Height (m)
        :return: Time (seconds)
        """
        if height < 0:
            raise ValueError("Height cannot be negative")
        
        return math.sqrt((2 * height) / self.gravity)
    
    def free_fall_energy_at_height(self, mass, initial_height, current_height):
        """
        Total energy at any height during free fall (energy conservation).
        
        :param mass: Mass (kg)
        :param initial_height: Initial height (m)
        :param current_height: Current height (m)
        :return: Total energy (Joules)
        """
        # Energy is constant: E = mgh_initial
        return mass * self.gravity * initial_height
    
    def velocity_at_height_free_fall(self, initial_height, current_height):
        """
        Velocity at specific height during free fall.
        
        :param initial_height: Initial height (m)
        :param current_height: Current height (m)
        :return: Velocity (m/s)
        """
        height_fallen = initial_height - current_height
        return math.sqrt(2 * self.gravity * height_fallen)
    
    # ==================== INCLINED PLANE MOTION ====================
    
    def potential_energy_on_incline(self, mass, incline_angle_degrees, distance_along_incline):
        """
        Potential energy for object on incline.
        Height = distance * sin(θ)
        
        :param mass: Mass (kg)
        :param incline_angle_degrees: Angle (degrees)
        :param distance_along_incline: Distance along incline (m)
        :return: Potential energy (Joules)
        """
        angle_rad = math.radians(incline_angle_degrees)
        height = distance_along_incline * math.sin(angle_rad)
        return mass * self.gravity * height
    
    def velocity_at_bottom_frictionless_incline(self, initial_height):
        """
        Velocity at bottom of frictionless incline using energy conservation.
        
        :param initial_height: Initial height (m)
        :return: Velocity at bottom (m/s)
        """
        return math.sqrt(2 * self.gravity * initial_height)
    
    def velocity_at_bottom_with_friction(self, initial_height, friction_coefficient, angle_degrees):
        """
        Velocity at bottom with friction considered.
        
        :param initial_height: Initial height (m)
        :param friction_coefficient: Coefficient of friction
        :param angle_degrees: Incline angle (degrees)
        :return: Velocity at bottom (m/s)
        """
        angle_rad = math.radians(angle_degrees)
        distance_along_incline = initial_height / math.sin(angle_rad)
        
        # Energy lost to friction: W_friction = μ * m * g * cos(θ) * d
        # Net energy: mgh - W_friction = 1/2*m*v²
        # We need mass, but it cancels: gh - μ*g*cos(θ)*d = 1/2*v²
        
        friction_work_per_mass = friction_coefficient * self.gravity * math.cos(angle_rad) * distance_along_incline
        velocity_squared = 2 * (self.gravity * initial_height - friction_work_per_mass)
        
        if velocity_squared < 0:
            raise ValueError("Friction too high - object won't reach bottom")
        
        return math.sqrt(velocity_squared)
    
    # ==================== PENDULUM ENERGY ====================
    
    def simple_pendulum_period(self, length):
        """
        Period of simple pendulum: T = 2π√(L/g)
        
        :param length: Length (m)
        :return: Period (seconds)
        """
        if length < 0:
            raise ValueError("Length cannot be negative")
        
        return 2 * math.pi * math.sqrt(length / self.gravity)
    
    def simple_pendulum_max_velocity(self, length, angle_degrees):
        """
        Max velocity at bottom for pendulum released from angle.
        Using energy conservation: mgh = 1/2*m*v_max²
        where h = L(1 - cos(θ))
        
        :param length: Pendulum length (m)
        :param angle_degrees: Release angle (degrees)
        :return: Max velocity (m/s)
        """
        angle_rad = math.radians(angle_degrees)
        height_drop = length * (1 - math.cos(angle_rad))
        return math.sqrt(2 * self.gravity * height_drop)
    
    def pendulum_total_energy(self, mass, length, angle_degrees):
        """
        Total energy of simple pendulum (using lowest point as reference).
        
        :param mass: Mass (kg)
        :param length: Length (m)
        :param angle_degrees: Current angle (degrees)
        :return: Total energy (Joules)
        """
        angle_rad = math.radians(angle_degrees)
        height = length * (1 - math.cos(angle_rad))
        pe = mass * self.gravity * height
        return pe
    
    def pendulum_velocity_at_angle(self, length, release_angle_degrees, current_angle_degrees):
        """
        Velocity at any angle during swing using energy conservation.
        
        :param length: Pendulum length (m)
        :param release_angle_degrees: Release angle (degrees)
        :param current_angle_degrees: Current angle (degrees)
        :return: Velocity (m/s)
        """
        release_rad = math.radians(release_angle_degrees)
        current_rad = math.radians(current_angle_degrees)
        
        # Energy at release = Energy at current angle
        # g*L(1-cos(θ₀)) = g*L(1-cos(θ)) + 1/2*v²
        height_diff = length * (math.cos(current_rad) - math.cos(release_rad))
        
        velocity_squared = 2 * self.gravity * height_diff
        
        if velocity_squared < 0:
            raise ValueError("Object hasn't reached this angle yet")
        
        return math.sqrt(velocity_squared)
    
    # ==================== ENERGY ANALYSIS & SUMMARY ====================
    
    def comprehensive_energy_analysis(self, mass, velocity, height, 
                                     spring_constant=0, displacement=0,
                                     moment_of_inertia=0, angular_velocity=0):
        """
        Complete energy analysis of a system.
        
        :return: Dictionary with all energy values
        """
        ke_trans = self.kinetic_energy(mass, velocity)
        ke_rot = self.rotational_kinetic_energy(moment_of_inertia, angular_velocity)
        pe_grav = self.gravitational_potential_energy(mass, height)
        pe_elastic = self.elastic_potential_energy(spring_constant, displacement)
        
        total_energy = ke_trans + ke_rot + pe_grav + pe_elastic
        
        return {
            'kinetic_energy_translational': ke_trans,
            'kinetic_energy_rotational': ke_rot,
            'kinetic_energy_total': ke_trans + ke_rot,
            'potential_energy_gravitational': pe_grav,
            'potential_energy_elastic': pe_elastic,
            'potential_energy_total': pe_grav + pe_elastic,
            'total_mechanical_energy': total_energy,
            'ke_percent': (ke_trans + ke_rot) / total_energy * 100 if total_energy > 0 else 0,
            'pe_percent': (pe_grav + pe_elastic) / total_energy * 100 if total_energy > 0 else 0,
        }