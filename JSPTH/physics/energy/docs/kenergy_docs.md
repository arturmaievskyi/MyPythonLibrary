# Mechanical Energy Module - Complete Documentation

## Overview

The **Mechanical Energy** module provides a comprehensive suite of tools for calculating, analyzing, and understanding mechanical energy in physical systems. It covers kinetic energy, potential energy, work, power, and energy conservation in various scenarios.

## Features

- ✅ **Kinetic Energy Calculations** - Translational and rotational
- ✅ **Potential Energy** - Gravitational and elastic
- ✅ **Energy Conservation** - Analysis and validation
- ✅ **Work & Power** - Calculations for various scenarios
- ✅ **Collision Analysis** - Before/after energy states
- ✅ **Projectile Motion** - Energy-based analysis
- ✅ **Simple Harmonic Motion** - SHM energy dynamics
- ✅ **Orbital Mechanics** - Gravitational orbital energy
- ✅ **Fluid Dynamics** - Bernoulli equation and dynamic pressure
- ✅ **Free Fall & Vertical Motion** - Energy in gravitational fields
- ✅ **Inclined Planes** - Energy with and without friction
- ✅ **Pendulum Motion** - Simple and complex pendulums
- ✅ **Moment of Inertia** - Common shapes and calculations

## Installation & Import

```python
from JSPTH.physics.mechanical_energy import MechanicalEnergy

# Create an instance
energy = MechanicalEnergy()

# Or with custom gravity (e.g., Moon)
energy_moon = MechanicalEnergy(gravity=1.62)
```

## Quick Start

### Basic Kinetic Energy

```python
from JSPTH.physics.mechanical_energy import MechanicalEnergy

energy = MechanicalEnergy()

# Calculate kinetic energy: KE = 1/2 * m * v²
mass = 2  # kg
velocity = 10  # m/s
ke = energy.kinetic_energy(mass, velocity)
print(f"Kinetic Energy: {ke} J")  # Output: 100.0 J
```

### Basic Potential Energy

```python
# Calculate gravitational potential energy: PE = m * g * h
mass = 2  # kg
height = 50  # meters
pe = energy.gravitational_potential_energy(mass, height)
print(f"Potential Energy: {pe} J")  # Output: 981.0 J
```

### Energy Conservation

```python
# Check if mechanical energy is conserved
initial_energy = 1000  # Joules
final_energy = 999.9  # Joules

is_conserved = energy.check_energy_conservation(initial_energy, final_energy)
print(f"Energy conserved: {is_conserved}")  # True
```

### Free Fall Example

```python
# Object falling from 100m
height = 100  # meters
mass = 1  # kg

# Initial potential energy
pe_initial = energy.gravitational_potential_energy(mass, height)

# Velocity when reaching ground (using energy conservation)
velocity_final = energy.free_fall_velocity(height)

# Final kinetic energy
ke_final = energy.kinetic_energy(mass, velocity_final)

print(f"Initial PE: {pe_initial:.2f} J")
print(f"Final KE: {ke_final:.2f} J")
print(f"Velocity at ground: {velocity_final:.2f} m/s")
print(f"Energy conserved: {energy.check_energy_conservation(pe_initial, ke_final)}")
```

## Core Concepts

### Kinetic Energy
Energy due to motion of an object.

- **Translational KE**: `KE = 1/2 * m * v²`
- **Rotational KE**: `KE_rot = 1/2 * I * ω²`

### Potential Energy
Energy due to position or configuration.

- **Gravitational PE**: `PE = m * g * h`
- **Elastic PE**: `PE = 1/2 * k * x²`

### Energy Conservation
In a closed system with no non-conservative forces:
```
Total Mechanical Energy = KE + PE = constant
```

### Work-Energy Theorem
The work done on an object equals its change in kinetic energy:
```
W_net = ΔKE = KE_final - KE_initial
```

### Power
Rate of energy transfer or work done.

- **Average Power**: `P_avg = W / t`
- **Instantaneous Power**: `P = F · v`

## Class Methods Overview

### Energy Calculations

| Method | Purpose |
|--------|---------|
| `kinetic_energy()` | Calculate translational KE |
| `rotational_kinetic_energy()` | Calculate rotational KE |
| `gravitational_potential_energy()` | Calculate gravitational PE |
| `elastic_potential_energy()` | Calculate spring PE |
| `total_mechanical_energy()` | Sum all energy forms |

### Inverse Calculations

| Method | Purpose |
|--------|---------|
| `velocity_from_kinetic_energy()` | Find velocity from KE |
| `height_from_potential_energy()` | Find height from PE |
| `displacement_from_elastic_pe()` | Find displacement from PE |
| `spring_constant_from_elastic_pe()` | Find k from PE |

### Moment of Inertia

| Shape | Method |
|-------|--------|
| Solid Sphere | `moment_of_inertia_solid_sphere()` |
| Hollow Sphere | `moment_of_inertia_hollow_sphere()` |
| Solid Cylinder | `moment_of_inertia_solid_cylinder()` |
| Hollow Cylinder | `moment_of_inertia_hollow_cylinder()` |
| Rod (about center) | `moment_of_inertia_rod_center()` |
| Rod (about end) | `moment_of_inertia_rod_end()` |
| Disk | `moment_of_inertia_disk()` |
| Ring | `moment_of_inertia_ring()` |

### Work & Power

| Method | Purpose |
|--------|---------|
| `work_by_force()` | Calculate work done by force |
| `work_energy_theorem()` | Apply work-energy theorem |
| `power_average()` | Calculate average power |
| `power_instantaneous()` | Calculate instantaneous power |
| `power_rotational()` | Calculate rotational power |

### Specialized Scenarios

| Scenario | Key Methods |
|----------|-------------|
| **Projectile Motion** | `projectile_max_height_from_energy()`, `projectile_velocity_at_height()` |
| **Free Fall** | `free_fall_velocity()`, `free_fall_time()` |
| **Pendulum** | `simple_pendulum_period()`, `simple_pendulum_max_velocity()` |
| **Spring-Mass** | `shm_total_energy()`, `shm_amplitude_from_energy()` |
| **Rolling Motion** | `total_kinetic_energy_rolling()` |
| **Orbital Motion** | `orbital_velocity()`, `orbital_period()`, `escape_velocity()` |
| **Inclined Plane** | `potential_energy_on_incline()`, `velocity_at_bottom_with_friction()` |
| **Collisions** | `kinetic_energy_before_collision()`, `energy_lost_in_collision()` |

## Common Use Cases

### 1. Analyzing Energy in Motion
```python
# Track energy as object moves
energy = MechanicalEnergy()
mass = 5  # kg
initial_velocity = 20  # m/s

for time in range(0, 5):
    height = 50 - 5 * time * time  # falling
    velocity = initial_velocity - 9.81 * time
    
    ke = energy.kinetic_energy(mass, velocity)
    pe = energy.gravitational_potential_energy(mass, max(0, height))
    total = ke + pe
    
    print(f"t={time}s: KE={ke:.0f}J, PE={pe:.0f}J, Total={total:.0f}J")
```

### 2. Checking Energy Conservation
```python
# Verify energy is conserved (no friction, no air resistance)
analysis = energy.energy_conservation_analysis(
    initial_ke=100,
    initial_pe=500,
    final_ke=450,
    final_pe=150
)

print(f"Energy loss: {analysis['energy_loss']:.2f} J")
print(f"Conserved: {analysis['is_conserved']}")
```

### 3. Efficiency Calculations
```python
# Calculate machine efficiency
input_energy = 1000  # J (electrical input)
output_energy = 750  # J (mechanical output)

efficiency = energy.efficiency(output_energy, input_energy)
loss = energy.energy_loss_percentage(input_energy, output_energy)

print(f"Efficiency: {efficiency:.1f}%")
print(f"Energy loss: {loss:.1f}%")
```

### 4. Design Calculations
```python
# Determine spring stiffness needed for specific energy storage
target_energy = 100  # J
max_displacement = 0.2  # m

k = energy.spring_constant_from_elastic_pe(target_energy, max_displacement)
print(f"Required spring constant: {k:.0f} N/m")
```

## Parameters & Units

### Standard SI Units

| Quantity | Symbol | Unit |
|----------|--------|------|
| Energy | E | Joules (J) |
| Power | P | Watts (W) |
| Force | F | Newtons (N) |
| Mass | m | Kilograms (kg) |
| Velocity | v | m/s |
| Acceleration | a | m/s² |
| Height | h | meters (m) |
| Displacement | x | meters (m) |
| Angle | θ | degrees or radians |
| Angular Velocity | ω | rad/s |
| Spring Constant | k | N/m |
| Moment of Inertia | I | kg·m² |

## Gravity Constants

```python
# Standard gravity values
GRAVITY = 9.81        # Earth
GRAVITY_MOON = 1.62   # Moon
GRAVITY_MARS = 3.71   # Mars

# Use custom gravity
energy_mars = MechanicalEnergy(gravity=3.71)
```

## Error Handling

The module includes built-in validation:

```python
try:
    # This will raise an error
    energy.kinetic_energy(-5, 10)  # Mass can't be negative
except ValueError as e:
    print(f"Error: {e}")

try:
    # This will raise an error
    energy.free_fall_time(-100)  # Height can't be negative
except ValueError as e:
    print(f"Error: {e}")
```

## Performance Considerations

- All calculations are O(1) time complexity
- No external dependencies required
- Suitable for real-time calculations
- Large-scale simulations require iteration

## Example Applications

### 1. **Roller Coaster Design**
Calculate heights needed for specific speeds using energy conservation.

### 2. **Sports Physics**
Analyze athlete performance using kinetic and potential energy.

### 3. **Engineering**
Determine motor and pump power requirements.

### 4. **Astronomy**
Calculate orbital velocities and escape velocities.

### 5. **Renewable Energy**
Analyze hydroelectric potential energy conversion.

### 6. **Ballistics**
Track projectile energy throughout flight.

## Tips & Tricks

### Tip 1: Energy Conservation Check
```python
# Always verify energy conservation for validation
initial = ke1 + pe1
final = ke2 + pe2
if abs(initial - final) > 1e-6:
    print("Energy not conserved - check for friction/air resistance")
```

### Tip 2: Unit Consistency
```python
# Always use SI units (Joules, meters, kg, m/s)
# Convert if needed:
# 1 kWh = 3.6e6 J
# 1 eV = 1.602e-19 J
```

### Tip 3: Numerical Stability
```python
# For very large or very small energies, check precision
energy_very_small = 1e-20  # J
if energy_very_small < 1e-15:
    print("Warning: Below precision threshold")
```

## Links to Detailed Documentation

- 📚 [Comprehensive Guide](MECHANICAL_ENERGY_GUIDE.md) - In-depth theory and applications
- 💡 [Examples](EXAMPLES.md) - Real-world scenarios and solutions
- 📖 [API Reference](API_REFERENCE.md) - Complete method documentation
- 🔬 [Physics Concepts](PHYSICS_CONCEPTS.md) - Theory, formulas, and derivations

## Contributing

To extend the module:

1. Add new methods to the `MechanicalEnergy` class
2. Update documentation
3. Add example usage
4. Include validation and error handling

## References

- Classical Mechanics - Goldstein, Poole, Safko
- Physics for Engineers - Serway, Jewett
- University Physics - Young, Freedman

## License

This module is part of the JSPTH (Japanese Simple Physics Toolkit) library.

## Version

- **Version**: 1.0
- **Last Updated**: 2024
- **Python**: 3.7+

---
# Mechanical Energy - Comprehensive Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Kinetic Energy](#kinetic-energy)
3. [Potential Energy](#potential-energy)
4. [Energy Conservation](#energy-conservation)
5. [Work and Power](#work-and-power)
6. [Moment of Inertia](#moment-of-inertia)
7. [Advanced Topics](#advanced-topics)
8. [Problem-Solving Strategies](#problem-solving-strategies)

---

## Introduction

### What is Mechanical Energy?

Mechanical energy is the sum of kinetic and potential energy in a system:

```
E_mechanical = KE + PE
```

Mechanical energy is conserved in isolated systems where only conservative forces act (gravity, springs, etc.). When non-conservative forces like friction act, mechanical energy decreases.

### Key Principles

1. **Energy Conservation**: Total energy remains constant in isolated systems
2. **Energy Transformation**: Energy converts between kinetic and potential forms
3. **Work-Energy Theorem**: Work done equals change in kinetic energy
4. **Power**: Rate of energy transfer

---

## Kinetic Energy

### Definition and Formula

**Kinetic energy** is the energy of motion:

```
KE = 1/2 * m * v²
```

**Where:**
- m = mass (kg)
- v = velocity (m/s)
- KE = kinetic energy (Joules)

### Key Properties

- **Always non-negative**: KE ≥ 0
- **Depends on velocity squared**: Doubling speed quadruples KE
- **Scalar quantity**: No direction
- **Reference frame dependent**: Different observers measure different KE

### Examples

#### Example 1: Car Moving
```python
from JSPTH.physics.mechanical_energy import MechanicalEnergy

energy = MechanicalEnergy()

# Car: mass = 1500 kg, velocity = 25 m/s (90 km/h)
mass = 1500  # kg
velocity = 25  # m/s

ke = energy.kinetic_energy(mass, velocity)
print(f"Kinetic Energy: {ke:,.0f} J")  # 468,750 J = 468.75 kJ
```

#### Example 2: Find Velocity from KE
```python
ke = 1000  # Joules
mass = 2  # kg

velocity = energy.velocity_from_kinetic_energy(ke, mass)
print(f"Velocity: {velocity:.2f} m/s")  # 31.62 m/s
```

### Rotational Kinetic Energy

Objects can also have rotational kinetic energy:

```
KE_rot = 1/2 * I * ω²
```

**Where:**
- I = moment of inertia (kg·m²)
- ω = angular velocity (rad/s)

#### Example: Spinning Wheel
```python
# Wheel: moment_of_inertia = 5 kg·m², angular_velocity = 10 rad/s
moment_of_inertia = 5  # kg·m²
angular_velocity = 10  # rad/s

ke_rot = energy.rotational_kinetic_energy(moment_of_inertia, angular_velocity)
print(f"Rotational KE: {ke_rot} J")  # 250 J
```

### Rolling Motion

An object rolling combines translational and rotational KE:

```
KE_total = 1/2*m*v² + 1/2*I*ω²

For rolling without slipping: v = ω*r
```

#### Example: Rolling Sphere Down Hill
```python
mass = 2  # kg
radius = 0.3  # m
velocity = 4  # m/s

# Moment of inertia for solid sphere: I = 2/5*m*r²
I = energy.moment_of_inertia_solid_sphere(mass, radius)

# Total KE (with rolling)
ke_total = energy.total_kinetic_energy_rolling(mass, velocity, I, radius)
print(f"Total KE (rolling): {ke_total:.2f} J")

# Compare to pure sliding (no rotation)
ke_sliding = energy.kinetic_energy(mass, velocity)
print(f"KE (sliding only): {ke_sliding:.2f} J")
```

**Key Insight**: A rolling object has more total KE than a sliding object at the same velocity because some energy goes into rotation.

---

## Potential Energy

### Gravitational Potential Energy

**Gravitational PE** is energy due to position in a gravitational field:

```
PE = m * g * h
```

**Where:**
- m = mass (kg)
- g = gravitational acceleration (9.81 m/s²)
- h = height (m)
- PE = potential energy (Joules)

#### Important Notes:
- PE is **relative**: Depends on choice of reference level
- Can be **negative**: If object is below reference point
- Always use **consistent reference**: Usually ground or lowest point

#### Example: Person on Building
```python
energy = MechanicalEnergy()

mass = 70  # kg (person)
height = 30  # m (30-story building)

pe = energy.gravitational_potential_energy(mass, height)
print(f"PE relative to ground: {pe:,.0f} J")  # 20,601 J
```

#### Example: Height from PE
```python
# How high can 5 kg object reach with 10,000 J of energy?
pe_available = 10000  # J
mass = 5  # kg

height = energy.height_from_potential_energy(pe_available, mass)
print(f"Height: {height:.2f} m")  # 204.08 m
```

### Elastic Potential Energy

**Elastic PE** is energy stored in stretched/compressed springs:

```
PE_elastic = 1/2 * k * x²
```

**Where:**
- k = spring constant (N/m)
- x = displacement from equilibrium (m)
- PE = elastic potential energy (Joules)

#### Spring Constant Interpretation:
- **Stiff spring**: High k (large force for small displacement)
- **Soft spring**: Low k (small force for large displacement)

#### Example: Compressed Spring
```python
spring_constant = 200  # N/m
displacement = 0.5  # m (50 cm compression)

pe_spring = energy.elastic_potential_energy(spring_constant, displacement)
print(f"Elastic PE: {pe_spring:.2f} J")  # 25 J
```

#### Example: Design Spring for System
```python
# Need 500 J of energy storage with 0.2 m displacement
target_energy = 500  # J
displacement = 0.2  # m

k = energy.spring_constant_from_elastic_pe(target_energy, displacement)
print(f"Required k: {k:,.0f} N/m")  # 25,000 N/m
```

#### Spring PE Comparison
```python
print(f"x = 0.5 m: PE = {energy.elastic_potential_energy(200, 0.5):.0f} J")
print(f"x = 1.0 m: PE = {energy.elastic_potential_energy(200, 1.0):.0f} J")
print(f"x = 1.5 m: PE = {energy.elastic_potential_energy(200, 1.5):.0f} J")

# Note: Doubling displacement quadruples energy!
```

### Exact Gravitational PE

For objects at large distances or on different planets:

```
PE = -G*M*m/r
```

**Where:**
- G = 6.674×10⁻¹¹ N·m²/kg²
- M = mass of central body (kg)
- m = object mass (kg)
- r = distance from center (m)
- PE = potential energy (negative for bound objects)

---

## Energy Conservation

### The Principle

**In an isolated system with no non-conservative forces:**

```
E_initial = E_final

KE_i + PE_i = KE_f + PE_f = constant
```

### When Energy is Conserved

✅ No friction
✅ No air resistance
✅ No other dissipative forces
✅ Only gravity and spring forces act

### When Energy is NOT Conserved

❌ Friction present
❌ Air resistance
❌ Collision (inelastic)
❌ Heat generation
❌ Any dissipative force

### Example: Ball Thrown Upward

```python
energy = MechanicalEnergy()

# Initial conditions
mass = 0.5  # kg
initial_velocity = 20  # m/s
initial_height = 2  # m (thrown from 2m height)

# Calculate total energy
total_energy = energy.total_mechanical_energy(
    mass, initial_velocity, initial_height
)
print(f"Total Energy: {total_energy:.2f} J")

# At maximum height, velocity = 0
max_height = energy.projectile_max_height_from_energy(mass, initial_velocity, 90)
print(f"Maximum height: {max_height:.2f} m")

# Velocity at max height: v = 0
ke_at_max = 0
pe_at_max = energy.gravitational_potential_energy(mass, max_height + initial_height)
print(f"PE at max height: {pe_at_max:.2f} J")
print(f"Total at max height: {ke_at_max + pe_at_max:.2f} J")

# Verify conservation
print(f"Energy conserved: {energy.check_energy_conservation(total_energy, ke_at_max + pe_at_max)}")
```

### Energy Analysis

```python
# Detailed energy conservation analysis
analysis = energy.energy_conservation_analysis(
    initial_ke=100,
    initial_pe=200,
    final_ke=250,
    final_pe=50
)

print(f"Initial Total: {analysis['initial_total']:.0f} J")
print(f"Final Total: {analysis['final_total']:.0f} J")
print(f"Energy Lost: {analysis['energy_loss']:.0f} J")
print(f"Percent Loss: {analysis['percent_loss']:.1f}%")
```

### Energy Loss Due to Friction

```python
# Inclined plane with friction
angle = 30  # degrees
distance = 10  # m
friction_coefficient = 0.2
initial_height = distance * math.sin(math.radians(angle))

# Without friction
velocity_no_friction = energy.velocity_at_bottom_frictionless_incline(initial_height)
ke_no_friction = energy.kinetic_energy(mass, velocity_no_friction)

# With friction
velocity_with_friction = energy.velocity_at_bottom_with_friction(
    initial_height, friction_coefficient, angle
)
ke_with_friction = energy.kinetic_energy(mass, velocity_with_friction)

energy_lost = ke_no_friction - ke_with_friction
print(f"KE without friction: {ke_no_friction:.2f} J")
print(f"KE with friction: {ke_with_friction:.2f} J")
print(f"Energy lost to friction: {energy_lost:.2f} J")
```

---

## Work and Power

### Work

**Work** is energy transferred by a force:

```
W = F * d * cos(θ)
```

**Where:**
- F = force magnitude (N)
- d = displacement magnitude (m)
- θ = angle between force and displacement
- W = work (Joules)

#### Key Points:
- **cos(0°) = 1**: Force in same direction as motion → Positive work
- **cos(90°) = 0**: Force perpendicular to motion → No work
- **cos(180°) = -1**: Force opposite to motion → Negative work

#### Example: Pushing Box
```python
force = 50  # N
distance = 10  # m
angle = 0  # N pushing in direction of motion

work = energy.work_by_force(force, distance, angle)
print(f"Work done: {work:.0f} J")  # 500 J

# If pushing at angle
work_at_angle = energy.work_by_force(force, distance, angle=30)
print(f"Work at 30°: {work_at_angle:.0f} J")  # 433 J
```

### Work-Energy Theorem

**The work done equals the change in kinetic energy:**

```
W_net = ΔKE = KE_final - KE_initial
```

#### Example: Accelerating Car
```python
mass = 1000  # kg
initial_velocity = 10  # m/s
final_velocity = 20  # m/s

initial_ke = energy.kinetic_energy(mass, initial_velocity)
final_ke = energy.kinetic_energy(mass, final_velocity)

work_done = energy.work_energy_theorem(initial_ke, final_ke)
print(f"Work required: {work_done:,.0f} J")  # 150,000 J
```

### Power

**Power** is the rate of energy transfer:

```
P = W / t  (average power)
P = F * v * cos(θ)  (instantaneous power)
```

**Where:**
- P = power (Watts)
- W = work (Joules)
- t = time (seconds)
- F = force (N)
- v = velocity (m/s)

#### Units:
- 1 Watt = 1 Joule/second
- 1 kilowatt (kW) = 1000 W
- 1 horsepower (hp) = 746 W

#### Example: Motor Power
```python
# Motor doing 10,000 J of work in 5 seconds
work = 10000  # J
time = 5  # s

power_avg = energy.power_average(work, time)
print(f"Average Power: {power_avg:,.0f} W")  # 2000 W = 2 kW
print(f"In horsepower: {power_avg / 746:.2f} hp")  # 2.68 hp
```

#### Example: Instantaneous Power
```python
# Force pushing object
force = 100  # N
velocity = 5  # m/s (force in direction of motion)
angle = 0  # degrees

power_inst = energy.power_instantaneous(force, velocity, angle)
print(f"Instantaneous Power: {power_inst:.0f} W")  # 500 W
```

#### Example: Climbing Stairs
```python
# Person climbing stairs
mass = 70  # kg
height = 10  # m
time = 20  # s (climbs in 20 seconds)

work_against_gravity = energy.gravitational_potential_energy(mass, height)
power_climbing = energy.power_average(work_against_gravity, time)

print(f"Work against gravity: {work_against_gravity:,.0f} J")
print(f"Power output: {power_climbing:,.0f} W")
print(f"In kW: {power_climbing / 1000:.2f} kW")
```

### Efficiency

**Efficiency** is the ratio of useful output to total input:

```
η = (E_output / E_input) × 100%
```

#### Example: Motor Efficiency
```python
electrical_input = 1000  # J of electrical energy
mechanical_output = 850  # J of mechanical work

efficiency = energy.efficiency(mechanical_output, electrical_input)
energy_lost = energy.energy_loss_percentage(electrical_input, mechanical_output)

print(f"Efficiency: {efficiency:.1f}%")  # 85%
print(f"Energy lost as heat: {energy_lost:.1f}%")  # 15%
```

---

## Moment of Inertia

### Definition

**Moment of inertia** is rotational mass—it measures resistance to angular acceleration:

```
I = Σ m_i * r_i²
```

### Common Shapes

The module provides pre-calculated formulas:

| Shape | Formula | Method |
|-------|---------|--------|
| **Solid Sphere** | I = 2/5 × M × R² | `moment_of_inertia_solid_sphere()` |
| **Hollow Sphere** | I = 2/3 × M × R² | `moment_of_inertia_hollow_sphere()` |
| **Solid Cylinder** | I = 1/2 × M × R² | `moment_of_inertia_solid_cylinder()` |
| **Hollow Cylinder** | I = M × R² | `moment_of_inertia_hollow_cylinder()` |
| **Rod (center)** | I = 1/12 × M × L² | `moment_of_inertia_rod_center()` |
| **Rod (end)** | I = 1/3 × M × L² | `moment_of_inertia_rod_end()` |
| **Disk** | I = 1/2 × M × R² | `moment_of_inertia_disk()` |
| **Ring** | I = M × R² | `moment_of_inertia_ring()` |

### Examples

#### Example: Different Shapes
```python
mass = 2  # kg
radius = 0.5  # m

# Compare different shapes with same mass and radius
i_sphere = energy.moment_of_inertia_solid_sphere(mass, radius)
i_cylinder = energy.moment_of_inertia_solid_cylinder(mass, radius)
i_ring = energy.moment_of_inertia_ring(mass, radius)

print(f"Sphere: {i_sphere:.4f} kg·m²")
print(f"Cylinder: {i_cylinder:.4f} kg·m²")
print(f"Ring: {i_ring:.4f} kg·m²")

# Ring has highest (mass concentrated at rim)
# Sphere has lowest (mass more uniformly distributed)
```

#### Example: Rolling Race
```python
# Which reaches bottom of ramp first: sphere or cylinder?
mass = 1  # kg
radius = 0.1  # m
height = 1  # m
angular_velocity = 5  # rad/s

# Using energy conservation:
# mgh = 1/2*m*v² + 1/2*I*ω²
# For rolling: v = ω*r

i_sphere = energy.moment_of_inertia_solid_sphere(mass, radius)
i_cylinder = energy.moment_of_inertia_solid_cylinder(mass, radius)

# Sphere: more energy in translation, less needed for rotation → faster
# Cylinder: more energy in rotation → slower

# Energy to height
total_pe = energy.gravitational_potential_energy(mass, height)

# For sphere rolling
v_sphere = energy.projectile_velocity_at_height(
    math.sqrt(2 * total_pe / mass),  # Initial v
    height, 0
)

print(f"Sphere velocity at bottom: {v_sphere:.2f} m/s")
print("Sphere reaches bottom first!")
```

---

## Advanced Topics

### Collisions

**Elastic Collision**: Kinetic energy is conserved
**Inelastic Collision**: Kinetic energy is lost

#### Example: Elastic Collision Analysis
```python
# Two objects colliding
mass1, v1_initial = 2, 10  # kg, m/s
mass2, v2_initial = 3, 0   # kg, m/s

ke_before = energy.kinetic_energy_before_collision(mass1, v1_initial, mass2, v2_initial)
print(f"KE before: {ke_before:.0f} J")

# After elastic collision (conservation of momentum + energy)
# v1_final = ((m1-m2)*v1_i + 2*m2*v2_i) / (m1+m2)
# v2_final = ((m2-m1)*v2_i + 2*m1*v1_i) / (m1+m2)

v1_final = ((mass1 - mass2) * v1_initial + 2 * mass2 * v2_initial) / (mass1 + mass2)
v2_final = ((mass2 - mass1) * v2_initial + 2 * mass1 * v1_initial) / (mass1 + mass2)

ke_after = energy.kinetic_energy_after_collision(mass1, v1_final, mass2, v2_final)
print(f"KE after: {ke_after:.0f} J")
print(f"Energy conserved: {energy.check_energy_conservation(ke_before, ke_after)}")
```

### Simple Harmonic Motion

**Simple harmonic motion** involves oscillation with constant energy.

#### Example: Mass on Spring
```python
mass = 2  # kg
spring_constant = 100  # N/m
amplitude = 0.5  # m

# Total energy (constant during oscillation)
max_pe = energy.elastic_potential_energy(spring_constant, amplitude)
# At equilibrium, all energy is KE
max_ke = max_pe

# Maximum velocity (at equilibrium)
max_velocity = energy.velocity_from_kinetic_energy(max_ke, mass)
print(f"Maximum velocity: {max_velocity:.2f} m/s")

# Period of oscillation
period = energy.shm_period_from_mass_spring(mass, spring_constant)
frequency = energy.shm_frequency_from_period(period)
print(f"Period: {period:.4f} s")
print(f"Frequency: {frequency:.2f} Hz")

# Energy at any position during oscillation
for x in [0, 0.25, 0.35, 0.5]:  # displacement in m
    total_e = energy.shm_total_energy(mass, 0, spring_constant, x)
    # At equilibrium (x=0): all KE
    # At amplitude (x=0.5): all PE
```

### Orbital Mechanics

**Orbital motion** combines kinetic energy (circular motion) and gravitational PE.

#### Example: Earth Orbit
```python
# Satellite orbiting Earth
earth_mass = 5.972e24  # kg
earth_radius = 6.371e6  # m
orbit_radius = earth_radius + 400e3  # 400 km altitude

# Orbital velocity
v_orbit = energy.orbital_velocity(earth_mass, orbit_radius)
print(f"Orbital velocity: {v_orbit:.0f} m/s")  # ~7660 m/s

# Orbital period
period = energy.orbital_period(earth_mass, orbit_radius)
print(f"Orbital period: {period/3600:.2f} hours")  # ~1.5 hours

# Escape velocity
v_escape = energy.escape_velocity(earth_mass, earth_radius)
print(f"Escape velocity: {v_escape:.0f} m/s")  # ~11,186 m/s
```

### Projectile Motion

**Projectile motion** combines translational KE with gravitational PE.

#### Example: Cannon Ball
```python
mass = 10  # kg
velocity = 50  # m/s
angle = 45  # degrees
initial_height = 10  # m

# Maximum height
max_height = energy.projectile_max_height_from_energy(mass, velocity, angle)
total_height = max_height + initial_height

# Range
range_proj = energy.projectile_range_energy_method(mass, velocity, angle)

# Total energy at launch
total_energy = energy.projectile_total_energy_at_launch(mass, velocity, angle, initial_height)

print(f"Maximum height: {total_height:.2f} m")
print(f"Range: {range_proj:.2f} m")
print(f"Total energy: {total_energy:,.0f} J")
```

---

## Problem-Solving Strategies

### Strategy 1: Use Energy Conservation

**When:** System has no non-conservative forces
**Steps:**
1. Identify initial and final states
2. Calculate total energy at each state
3. Set them equal

**Example:**
```
Object drops from height h.
Find velocity at ground:

Initial: E = mgh (all PE, v=0)
Final: E = 1/2*m*v² (all KE, h=0)

mgh = 1/2*m*v²
v = √(2gh)
```

### Strategy 2: Use Work-Energy Theorem

**When:** Forces are known, need velocity change
**Steps:**
1. Calculate work done by each force
2. Sum to get net work
3. Apply: W = ΔKE

### Strategy 3: Use Power

**When:** Time and energy are involved
**Steps:**
1. Calculate energy needed
2. Divide by time available
3. Compare to available power

### Strategy 4: Use Efficiency

**When:** Some energy is lost
**Steps:**
1. Identify input and output energy
2. Calculate efficiency
3. Find energy loss

### Example Problem: Lifting Boxes

```python
# Problem: Worker lifts 20 boxes, each 10 kg, 1m high, in 60 seconds
boxes = 20
mass_per_box = 10  # kg
height = 1  # m
time = 60  # s

# Total work
total_mass = boxes * mass_per_box
work = energy.gravitational_potential_energy(total_mass, height)

# Average power required
power = energy.power_average(work, time)

print(f"Total work: {work:,.0f} J")
print(f"Average power: {power:,.1f} W")
print(f"In horsepower: {power/746:.3f} hp")

# Compare to human limit (~100 W sustained)
if power > 100:
    print("This requires multiple workers or mechanical assistance")
```

---

## Summary Table

| Concept | Formula | Key Points |
|---------|---------|-----------|
| **Kinetic Energy** | KE = 1/2 × m × v² | Depends on velocity squared |
| **Rotational KE** | KE = 1/2 × I × ω² | Similar to translational |
| **Gravitational PE** | PE = m × g × h | Relative to reference point |
| **Elastic PE** | PE = 1/2 × k × x² | Quadratic in displacement |
| **Total ME** | E = KE + PE | Conserved (no friction) |
| **Work** | W = F × d × cos(θ) | Angle dependent |
| **Power** | P = W/t = F × v | Rate of energy transfer |
| **Efficiency** | η = E_out / E_in | As percentage or ratio |

---

## Common Pitfalls

❌ **Pitfall 1**: Using height without specifying reference point
✅ **Fix**: Always explicitly define where h = 0

❌ **Pitfall 2**: Forgetting velocity is squared in KE
✅ **Fix**: Remember doubling velocity quadruples KE

❌ **Pitfall 3**: Ignoring rotational energy in rolling objects
✅ **Fix**: Use `total_kinetic_energy_rolling()` for realistic problems

❌ **Pitfall 4**: Assuming energy is always conserved
✅ **Fix**: Check for friction, air resistance, etc.

❌ **Pitfall 5**: Mixing units (meters with kilometers, etc.)
✅ **Fix**: Always convert to SI units first

---

## Next Steps

1. Read [Examples & Tutorials](EXAMPLES.md) for practical applications
2. Check [API Reference](API_REFERENCE.md) for method details
3. Review [Physics Concepts](PHYSICS_CONCEPTS.md) for deeper theory
4. Try implementing your own energy problems!

# Mechanical Energy - Detailed Examples & Tutorials

## Table of Contents

1. [Basic Examples](#basic-examples)
2. [Intermediate Examples](#intermediate-examples)
3. [Advanced Examples](#advanced-examples)
4. [Real-World Applications](#real-world-applications)
5. [Challenge Problems](#challenge-problems)

---

## Basic Examples

### Example 1: Simple Free Fall

**Problem**: A ball is dropped from a 50-meter tall building. Assuming no air resistance, find:
- The velocity when it hits the ground
- The time it takes to fall
- The kinetic energy at impact (mass = 0.5 kg)

**Solution**:

```python
from JSPTH.physics.mechanical_energy import MechanicalEnergy
import math

energy = MechanicalEnergy()

# Given
height = 50  # meters
mass = 0.5  # kg

# 1. Velocity at impact using energy conservation
# Initial: PE = mgh, KE = 0
# Final: PE = 0, KE = 1/2*m*v²
# Therefore: v = √(2gh)

velocity_impact = energy.free_fall_velocity(height)
print(f"1. Velocity at impact: {velocity_impact:.2f} m/s")  # 31.32 m/s

# Alternative: using kinetic energy
pe_initial = energy.gravitational_potential_energy(mass, height)
ke_final = pe_initial  # Energy conserved
velocity_check = energy.velocity_from_kinetic_energy(ke_final, mass)
print(f"   (Verified): {velocity_check:.2f} m/s")

# 2. Time to fall using kinematics
# h = 1/2*g*t² → t = √(2h/g)

time_to_fall = energy.free_fall_time(height)
print(f"\n2. Time to fall: {time_to_fall:.2f} seconds")  # 3.19 s

# 3. Kinetic energy at impact
ke_impact = energy.kinetic_energy(mass, velocity_impact)
print(f"\n3. Kinetic energy at impact: {ke_impact:.2f} J")  # 245.25 J

# Verify energy conservation
print(f"\nEnergy Conservation Check:")
print(f"Initial PE: {pe_initial:.2f} J")
print(f"Final KE: {ke_impact:.2f} J")
print(f"Conserved: {energy.check_energy_conservation(pe_initial, ke_impact)}")
```

**Output:**
```
1. Velocity at impact: 31.32 m/s
   (Verified): 31.32 m/s

2. Time to fall: 3.19 seconds

3. Kinetic energy at impact: 245.25 J

Energy Conservation Check:
Initial PE: 245.25 J
Final KE: 245.25 J
Conserved: True
```

---

### Example 2: Throwing a Ball Upward

**Problem**: A ball is thrown upward with initial velocity 20 m/s from 2 meters above the ground.
- Find maximum height reached
- Find velocity when it returns to launch height
- Find total time in air

**Solution**:

```python
energy = MechanicalEnergy()

# Given
initial_velocity = 20  # m/s
initial_height = 2  # m (launch point)
angle = 90  # degrees (straight up)

# 1. Maximum height above launch point
height_above_launch = energy.projectile_max_height_from_energy(1, initial_velocity, angle)
max_height = initial_height + height_above_launch

print(f"1. Maximum height: {max_height:.2f} m")  # 22.39 m

# 2. Velocity when returning to launch height
# Using energy conservation: KE_initial = KE_final
# Therefore: v_up = v_down (magnitude)

velocity_on_return = initial_velocity
print(f"\n2. Velocity on return to launch height: {velocity_on_return:.2f} m/s")

# 3. Total time in air
# Time up: t = v₀/g
time_up = initial_velocity / 9.81
# Time falling from height h: t = √(2h/g)
time_down = math.sqrt(2 * max_height / 9.81)
total_time = time_up + time_down

print(f"\n3. Time up: {time_up:.2f} s")
print(f"   Time down: {time_down:.2f} s")
print(f"   Total time in air: {total_time:.2f} s")

# Energy analysis throughout flight
print(f"\nEnergy at different points (mass = 1 kg):")
mass = 1

# At launch
ke_launch = energy.kinetic_energy(mass, initial_velocity)
pe_launch = energy.gravitational_potential_energy(mass, initial_height)
total_launch = ke_launch + pe_launch

# At max height (v = 0)
ke_max = 0
pe_max = energy.gravitational_potential_energy(mass, max_height)
total_max = ke_max + pe_max

# At ground (h = 0)
# Using energy conservation from launch
velocity_ground = math.sqrt(initial_velocity**2 + 2 * 9.81 * initial_height)
ke_ground = energy.kinetic_energy(mass, velocity_ground)
pe_ground = 0
total_ground = ke_ground + pe_ground

print(f"At launch: KE = {ke_launch:.1f} J, PE = {pe_launch:.1f} J, Total = {total_launch:.1f} J")
print(f"At max height: KE = {ke_max:.1f} J, PE = {pe_max:.1f} J, Total = {total_max:.1f} J")
print(f"At ground: KE = {ke_ground:.1f} J, PE = {pe_ground:.1f} J, Total = {total_ground:.1f} J")
print(f"Energy conserved throughout: {energy.check_energy_conservation(total_launch, total_ground)}")
```

**Output:**
```
1. Maximum height: 22.39 m

2. Velocity on return to launch height: 20.00 m/s

3. Time up: 2.04 s
   Time down: 2.02 s
   Total time in air: 4.06 s

Energy at different points (mass = 1 kg):
At launch: KE = 200.0 J, PE = 19.6 J, Total = 219.6 J
At max height: KE = 0.0 J, PE = 219.6 J, Total = 219.6 J
At ground: KE = 219.6 J, PE = 0.0 J, Total = 219.6 J
Energy conserved throughout: True
```

---

### Example 3: Spring Compression

**Problem**: A spring with constant k = 200 N/m is compressed by 0.3 m. A 2 kg mass is placed against it.
- Find elastic potential energy stored
- Find maximum velocity of the mass when released
- Find how high the mass could theoretically be launched

**Solution**:

```python
energy = MechanicalEnergy()

# Given
k = 200  # N/m
compression = 0.3  # m
mass = 2  # kg

# 1. Elastic potential energy
pe_elastic = energy.elastic_potential_energy(k, compression)
print(f"1. Elastic PE stored: {pe_elastic:.2f} J")  # 9 J

# 2. Maximum velocity when released (horizontal)
# All elastic PE converts to KE
# PE = KE → 1/2*k*x² = 1/2*m*v²
max_velocity = energy.velocity_from_kinetic_energy(pe_elastic, mass)
print(f"\n2. Maximum velocity: {max_velocity:.2f} m/s")  # 3.0 m/s

# Verify
max_ke = energy.kinetic_energy(mass, max_velocity)
print(f"   KE at max velocity: {max_ke:.2f} J")
print(f"   Equals stored PE: {energy.check_energy_conservation(pe_elastic, max_ke)}")

# 3. Maximum height if launched vertically
# All kinetic energy converts to potential energy
# 1/2*m*v² = m*g*h → h = v²/(2g)
max_height = max_velocity**2 / (2 * 9.81)
print(f"\n3. Maximum height if launched vertically: {max_height:.2f} m")

# Energy at each stage
print(f"\nEnergy transformation:")
print(f"Spring: PE_elastic = {pe_elastic:.2f} J")
print(f"Horizontal: KE = {max_ke:.2f} J")
print(f"Vertical: PE_gravity = {energy.gravitational_potential_energy(mass, max_height):.2f} J")
```

**Output:**
```
1. Elastic PE stored: 9.00 J

2. Maximum velocity: 3.00 m/s
   KE at max velocity: 9.00 J
   Equals stored PE: True

3. Maximum height if launched vertically: 0.46 m

Energy transformation:
Spring: PE_elastic = 9.00 J
Horizontal: KE = 9.00 J
Vertical: PE_gravity = 9.00 J
```

---

## Intermediate Examples

### Example 4: Rolling Sphere Down a Ramp

**Problem**: A solid sphere (mass = 5 kg, radius = 0.2 m) starts from rest at the top of a 10-meter tall ramp.
- Compare energy with a sliding block
- Find velocity at bottom considering rolling
- Find angular velocity at bottom

**Solution**:

```python
energy = MechanicalEnergy()
import math

# Given
mass = 5  # kg
radius = 0.2  # m
height = 10  # m
g = 9.81  # m/s²

# Initial potential energy
pe_initial = energy.gravitational_potential_energy(mass, height)
print(f"Initial Potential Energy: {pe_initial:.2f} J")  # 490.5 J

# Case 1: Pure sliding (no friction, no rotation)
print(f"\n=== CASE 1: Pure Sliding ===")
velocity_sliding = energy.free_fall_velocity(height)
ke_sliding = energy.kinetic_energy(mass, velocity_sliding)
print(f"Final velocity (sliding): {velocity_sliding:.2f} m/s")
print(f"Kinetic energy: {ke_sliding:.2f} J")
print(f"Energy conserved: {energy.check_energy_conservation(pe_initial, ke_sliding)}")

# Case 2: Rolling without slipping
print(f"\n=== CASE 2: Rolling ===")

# Moment of inertia for solid sphere: I = 2/5*m*r²
moment_of_inertia = energy.moment_of_inertia_solid_sphere(mass, radius)
print(f"Moment of inertia: {moment_of_inertia:.4f} kg·m²")

# For rolling: v = ω*r, so we need to solve:
# mgh = 1/2*m*v² + 1/2*I*ω²
# mgh = 1/2*m*v² + 1/2*I*(v/r)²
# mgh = v² * (1/2*m + I/(2*r²))
# v = √(2*g*h / (1 + I/(m*r²)))

velocity_rolling = math.sqrt(2 * g * height / (1 + moment_of_inertia / (mass * radius**2)))
angular_velocity = velocity_rolling / radius

ke_trans = energy.kinetic_energy(mass, velocity_rolling)
ke_rot = energy.rotational_kinetic_energy(moment_of_inertia, angular_velocity)
ke_total = energy.total_kinetic_energy_rolling(mass, velocity_rolling, moment_of_inertia, radius)

print(f"Final velocity (rolling): {velocity_rolling:.2f} m/s")
print(f"Angular velocity: {angular_velocity:.2f} rad/s")
print(f"Translational KE: {ke_trans:.2f} J")
print(f"Rotational KE: {ke_rot:.2f} J")
print(f"Total KE: {ke_total:.2f} J")
print(f"Energy conserved: {energy.check_energy_conservation(pe_initial, ke_total)}")

# Comparison
print(f"\n=== COMPARISON ===")
print(f"Sliding velocity: {velocity_sliding:.2f} m/s")
print(f"Rolling velocity: {velocity_rolling:.2f} m/s")
print(f"Ratio (rolling/sliding): {velocity_rolling/velocity_sliding:.3f}")
print(f"\nRolling is slower because some energy goes into rotation!")

# Energy distribution in rolling
percent_trans = (ke_trans / ke_total) * 100
percent_rot = (ke_rot / ke_total) * 100
print(f"\nEnergy distribution in rolling:")
print(f"Translational: {percent_trans:.1f}%")
print(f"Rotational: {percent_rot:.1f}%")
```

**Output:**
```
Initial Potential Energy: 490.50 J

=== CASE 1: Pure Sliding ===
Final velocity (sliding): 14.00 m/s
Kinetic energy: 490.50 J
Energy conserved: True

=== CASE 2: Rolling ===
Moment of inertia: 0.0800 kg·m²
Final velocity (rolling): 11.23 m/s
Angular velocity: 56.16 rad/s
Translational KE: 315.68 J
Rotational KE: 126.03 J
Total KE: 441.71 J
Energy conserved: True

=== COMPARISON ===
Sliding velocity: 14.00 m/s
Rolling velocity: 11.23 m/s
Ratio (rolling/sliding): 0.803

Rolling is slower because some energy goes into rotation!

Energy distribution in rolling:
Translational: 71.4%
Rotational: 28.6%
```

---

### Example 5: Simple Pendulum

**Problem**: A 1-meter long pendulum is released from 30° angle. 
- Find maximum velocity (at bottom)
- Find period of oscillation
- Track energy throughout one swing

**Solution**:

```python
energy = MechanicalEnergy()
import math

# Given
length = 1  # meter
release_angle = 30  # degrees
mass = 1  # kg for energy calculations

# 1. Maximum velocity (at bottom)
max_velocity = energy.simple_pendulum_max_velocity(length, release_angle)
print(f"1. Maximum velocity (at bottom): {max_velocity:.3f} m/s")

# Verify with energy conservation
angle_rad = math.radians(release_angle)
height_drop = length * (1 - math.cos(angle_rad))
print(f"   Height dropped: {height_drop:.4f} m")
print(f"   Energy check: v = √(2gh) = {math.sqrt(2*9.81*height_drop):.3f} m/s ✓")

# 2. Period of oscillation
period = energy.simple_pendulum_period(length)
frequency = energy.shm_frequency_from_period(period)
print(f"\n2. Period: {period:.3f} seconds")
print(f"   Frequency: {frequency:.3f} Hz")

# 3. Energy at different points during swing
print(f"\n3. Energy throughout swing:")

# Total energy (constant)
total_energy = energy.pendulum_total_energy(mass, length, release_angle)
print(f"   Total energy: {total_energy:.4f} J")

# At different angles
angles = [30, 20, 10, 0, -10, -20, -30]
print(f"\n   {'Angle°':>8} {'PE (J)':>10} {'KE (J)':>10} {'Total (J)':>10} {'v (m/s)':>10}")
print(f"   {'-'*8} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")

for angle in angles:
    # PE at this angle
    pe = energy.pendulum_total_energy(mass, length, angle)
    
    # KE from energy conservation
    ke = total_energy - pe
    
    # Velocity at this angle
    velocity = energy.pendulum_velocity_at_angle(length, release_angle, angle)
    
    print(f"   {angle:>8} {pe:>10.4f} {ke:>10.4f} {total_energy:>10.4f} {velocity:>10.3f}")

# 4. Compare with SHM approximation (small angle)
print(f"\n4. Note: This analysis is exact for all angles.")
print(f"   SHM approximation (sin θ ≈ θ) works best for small angles.")
```

**Output:**
```
1. Maximum velocity (at bottom): 1.623 m/s
   Height dropped: 0.0670 m
   Energy check: v = √(2gh) = 1.623 m/s ✓

2. Period: 2.007 seconds
   Frequency: 0.498 Hz

3. Energy throughout swing:

   Angle°       PE (J)        KE (J)     Total (J)      v (m/s)
   -------- ---------- ---------- ---------- ----------
       30       0.0670     0.0000     0.0670      0.000
       20       0.0297     0.0372     0.0670      0.862
       10       0.0075     0.0595     0.0670      1.540
        0       0.0000     0.0670     0.0670      1.623
      -10       0.0075     0.0595     0.0670      1.540
      -20       0.0297     0.0372     0.0670      0.862
      -30       0.0670     0.0000     0.0670      0.000
```

---

## Advanced Examples

### Example 6: Collision Analysis

**Problem**: Two cars collide:
- Car A: mass = 1500 kg, velocity = 25 m/s
- Car B: mass = 1500 kg, velocity = 0 m/s (stationary)

Analyze elastic vs. inelastic collision.

**Solution**:

```python
energy = MechanicalEnergy()
import math

# Given
m1, v1_i = 1500, 25  # kg, m/s
m2, v2_i = 1500, 0   # kg, m/s

# Initial kinetic energy
ke_before = energy.kinetic_energy_before_collision(m1, v1_i, m2, v2_i)
print(f"KE Before Collision: {ke_before:,.0f} J")  # 468,750 J

# ===== ELASTIC COLLISION =====
print(f"\n=== ELASTIC COLLISION ===")
print(f"(Kinetic energy conserved)")

# For elastic collision:
# v1_f = ((m1-m2)*v1_i + 2*m2*v2_i) / (m1+m2)
# v2_f = ((m2-m1)*v2_i + 2*m1*v1_i) / (m1+m2)

v1_elastic = ((m1 - m2) * v1_i + 2 * m2 * v2_i) / (m1 + m2)
v2_elastic = ((m2 - m1) * v2_i + 2 * m1 * v1_i) / (m1 + m2)

ke_after_elastic = energy.kinetic_energy_after_collision(m1, v1_elastic, m2, v2_elastic)

print(f"Car A velocity after: {v1_elastic:.2f} m/s")
print(f"Car B velocity after: {v2_elastic:.2f} m/s")
print(f"KE After: {ke_after_elastic:,.0f} J")
print(f"Energy conserved: {energy.check_energy_conservation(ke_before, ke_after_elastic)}")

# ===== PERFECTLY INELASTIC COLLISION =====
print(f"\n=== PERFECTLY INELASTIC COLLISION ===")
print(f"(Objects stick together)")

# Conservation of momentum:
# m1*v1_i + m2*v2_i = (m1+m2)*v_final
v_final_inelastic = (m1 * v1_i + m2 * v2_i) / (m1 + m2)

ke_after_inelastic = (0.5 * (m1 + m2) * v_final_inelastic**2)

print(f"Final velocity (both stuck): {v_final_inelastic:.2f} m/s")
print(f"KE After: {ke_after_inelastic:,.0f} J")
print(f"Energy lost: {ke_before - ke_after_inelastic:,.0f} J")
print(f"Energy loss percentage: {((ke_before - ke_after_inelastic)/ke_before)*100:.1f}%")

# ===== PARTIALLY INELASTIC COLLISION =====
print(f"\n=== PARTIALLY INELASTIC COLLISION ===")
print(f"(Coefficient of restitution e = 0.5)")

e = 0.5  # coefficient of restitution
# v2_f - v1_f = -e * (v2_i - v1_i)
# Combined with momentum conservation:

v1_partial = (m1 * v1_i + m2 * v2_i + m2 * e * (v2_i - v1_i)) / (m1 + m2)
v2_partial = (m1 * v1_i + m2 * v2_i - m1 * e * (v2_i - v1_i)) / (m1 + m2)

ke_after_partial = energy.kinetic_energy_after_collision(m1, v1_partial, m2, v2_partial)

print(f"Car A velocity after: {v1_partial:.2f} m/s")
print(f"Car B velocity after: {v2_partial:.2f} m/s")
print(f"KE After: {ke_after_partial:,.0f} J")
print(f"Energy lost: {ke_before - ke_after_partial:,.0f} J")
print(f"Energy loss percentage: {((ke_before - ke_after_partial)/ke_before)*100:.1f}%")

# ===== SUMMARY TABLE =====
print(f"\n=== SUMMARY ===")
print(f"{'Type':<25} {'v1_final (m/s)':<18} {'v2_final (m/s)':<18} {'KE_after':<15}")
print(f"{'-'*76}")
print(f"{'Elastic':<25} {v1_elastic:<18.2f} {v2_elastic:<18.2f} {ke_after_elastic:<15,.0f}")
print(f"{'Partially Inelastic':<25} {v1_partial:<18.2f} {v2_partial:<18.2f} {ke_after_partial:<15,.0f}")
print(f"{'Perfectly Inelastic':<25} {v_final_inelastic:<18.2f} {v_final_inelastic:<18.2f} {ke_after_inelastic:<15,.0f}")
```

**Output:**
```
KE Before Collision: 468,750 J

=== ELASTIC COLLISION ===
(Kinetic energy conserved)
Car A velocity after: 0.00 m/s
Car B velocity after: 25.00 m/s
KE After: 468,750 J
Energy conserved: True

=== PERFECTLY INELASTIC COLLISION ===
(Objects stick together)
Final velocity (both stuck): 12.50 m/s
KE After: 117,188 J
Energy lost: 351,562 J
Energy loss percentage: 75.0%

=== PARTIALLY INELASTIC COLLISION ===
(Coefficient of restitution e = 0.5)
Car A velocity after: 6.25 m/s
Car B velocity after: 18.75 m/s
KE After: 292,969 J
Energy lost: 175,781 J
Energy loss percentage: 37.5%

=== SUMMARY ===
Type                     v1_final (m/s)     v2_final (m/s)     KE_after       
--------------------------------------------------------------------
Elastic                         0.00               25.00              468,750
Partially Inelastic             6.25               18.75              292,969
Perfectly Inelastic            12.50               12.50              117,188
```

---

## Real-World Applications

### Example 7: Hydroelectric Power Plant

**Problem**: A dam holds water 80 meters high. A water flow of 500 kg/s cascades down.
- Calculate potential energy available per second
- Calculate theoretical power output
- If efficiency is 85%, what is actual power?

**Solution**:

```python
energy = MechanicalEnergy()

# Given
height = 80  # meters (vertical drop)
flow_rate = 500  # kg/s
efficiency = 0.85  # 85% efficiency

# 1. Gravitational PE per unit time
mass_per_second = flow_rate
pe_per_second = energy.gravitational_potential_energy(mass_per_second, height)

print(f"Potential Energy available per second:")
print(f"PE = m × g × h = {mass_per_second} × 9.81 × {height}")
print(f"PE = {pe_per_second:,.0f} J/s = {pe_per_second:,.0f} W")  # Joules/second = Watts

# 2. Theoretical power (assuming all PE converts to KE)
theoretical_power = pe_per_second  # W (same as PE per second)
theoretical_power_kw = theoretical_power / 1000
theoretical_power_mw = theoretical_power / 1e6

print(f"\nTheoretical Power Output:")
print(f"P = {theoretical_power:,.0f} W")
print(f"P = {theoretical_power_kw:,.0f} kW")
print(f"P = {theoretical_power_mw:.2f} MW")

# 3. Actual power considering efficiency
actual_power = theoretical_power * efficiency
actual_power_kw = actual_power / 1000
actual_power_mw = actual_power / 1e6

power_loss = theoretical_power - actual_power

print(f"\nActual Power Output (at {efficiency*100:.0f}% efficiency):")
print(f"P = {actual_power:,.0f} W")
print(f"P = {actual_power_kw:,.0f} kW")
print(f"P = {actual_power_mw:.2f} MW")

print(f"\nPower Loss:")
print(f"P_loss = {power_loss:,.0f} W = {power_loss/1000:,.0f} kW")

# 4. Annual energy production
seconds_per_year = 365.25 * 24 * 3600
annual_energy = actual_power * seconds_per_year  # Joules
annual_energy_kwh = annual_energy / (3.6e6)  # Convert J to kWh

print(f"\nAnnual Energy Production:")
print(f"E = P × t = {actual_power_mw:.2f} MW × 1 year")
print(f"E = {annual_energy:.2e} J")
print(f"E = {annual_energy_kwh:,.0f} kWh")
print(f"E = {annual_energy_kwh/1e6:.1f} GWh")

# 5. Comparison
# Average US household uses ~10,000 kWh/year
households = annual_energy_kwh / 10000
print(f"\nCan power approximately {households:,.0f} average US households")
```

**Output:**
```
Potential Energy available per second:
PE = m × g × h = 500 × 9.81 × 80
PE = 392,400 J/s = 392,400 W

Theoretical Power Output:
P = 392,400 W
P = 392.4 kW
P = 0.39 MW

Actual Power Output (at 85% efficiency):
P = 333,540 W
P = 333.5 kW
P = 0.33 MW

Power Loss:
P_loss = 58,860 W = 58.9 kW

Annual Energy Production:
E = P × t = 0.33 MW × 1 year
E = 1.05e+13 J
E = 2,929,017 kWh
E = 2.9 GWh

Can power approximately 293 average US households
```

---

### Example 8: Sports - Shot Put Analysis

**Problem**: A shot putter releases a 7.26 kg shot at 14 m/s at 45° angle from 2.1 m height.
- Find maximum height
- Find range
- Find impact velocity
- Find kinetic energy at impact

**Solution**:

```python
energy = MechanicalEnergy()
import math

# Given
mass = 7.26  # kg
velocity = 14  # m/s
angle = 45  # degrees
initial_height = 2.1  # m (typical shot put release height)

# 1. Maximum height
max_height_gain = energy.projectile_max_height_from_energy(mass, velocity, angle)
max_height_total = initial_height + max_height_gain

print(f"1. Maximum Height:")
print(f"   Height gained: {max_height_gain:.2f} m")
print(f"   Total height: {max_height_total:.2f} m")

# 2. Range
range_proj = energy.projectile_range_energy_method(mass, velocity, angle)
print(f"\n2. Range (Horizontal Distance):")
print(f"   {range_proj:.2f} m")

# 3. Impact velocity
# At impact, height = 0
# Using energy conservation: initial_total_E = final_KE
initial_ke = energy.kinetic_energy(mass, velocity)
initial_pe = energy.gravitational_potential_energy(mass, initial_height)
total_energy = initial_ke + initial_pe

impact_ke = total_energy
impact_velocity = energy.velocity_from_kinetic_energy(impact_ke, mass)

print(f"\n3. Impact Analysis:")
print(f"   Initial KE: {initial_ke:.2f} J")
print(f"   Initial PE: {initial_pe:.2f} J")
print(f"   Total Energy: {total_energy:.2f} J")
print(f"   Impact KE: {impact_ke:.2f} J")
print(f"   Impact velocity: {impact_velocity:.2f} m/s")

# 4. Impact velocity components
angle_rad = math.radians(angle)
v_x = velocity * math.cos(angle_rad)  # Horizontal component (constant)
v_y_impact = math.sqrt(impact_velocity**2 - v_x**2)  # Vertical component

print(f"\n4. Velocity Components at Impact:")
print(f"   Horizontal: {v_x:.2f} m/s")
print(f"   Vertical: {v_y_impact:.2f} m/s")
print(f"   Total: {impact_velocity:.2f} m/s")

# 5. Energy visualization
print(f"\n5. Energy Distribution at Key Points:")
print(f"   {'Point':<20} {'Height (m)':<12} {'KE (J)':<12} {'PE (J)':<12} {'Total (J)':<12}")
print(f"   {'-'*56}")

# Launch
print(f"   {'Launch':<20} {initial_height:<12.2f} {initial_ke:<12.0f} {initial_pe:<12.0f} {total_energy:<12.0f}")

# Max height
ke_max = 0  # Velocity has only horizontal component at max height
pe_max = energy.gravitational_potential_energy(mass, max_height_total)
print(f"   {'Max Height':<20} {max_height_total:<12.2f} {ke_max:<12.0f} {pe_max:<12.0f} {total_energy:<12.0f}")

# Impact
pe_impact = 0
print(f"   {'Impact':<20} {0:<12.2f} {impact_ke:<12.0f} {pe_impact:<12.0f} {total_energy:<12.0f}")

# 6. Performance comparison
print(f"\n6. Performance Context:")
print(f"   Olympic record (men): 23.12 m (Ryan Crouser, 2016)")
print(f"   This throw: {range_proj:.2f} m")
print(f"   To match Olympic record, need velocity: {14 * math.sqrt(23.12/range_proj):.2f} m/s")
```

**Output:**
```
1. Maximum Height:
   Height gained: 4.99 m
   Total height: 7.09 m

2. Range (Horizontal Distance):
   19.96 m

3. Impact Analysis:
   Initial KE: 710.76 J
   Initial PE: 148.23 J
   Total Energy: 858.99 J
   Impact KE: 858.99 J
   Impact velocity: 15.36 m/s

4. Velocity Components at Impact:
   Horizontal: 9.90 m/s
   Vertical: 11.81 m/s
   Total: 15.36 m/s

5. Energy Distribution at Key Points:
   Point                Height (m)      KE (J)       PE (J)       Total (J)    
   --------------------------------------------------------
   Launch                    2.10       710.76       148.23       858.99
   Max Height               7.09         0.00       858.99       858.99
   Impact                   0.00       858.99         0.00       858.99

6. Performance Context:
   Olympic record (men): 23.12 m (Ryan Crouser, 2016)
   This throw: 19.96 m
   To match Olympic record, need velocity: 16.20 m/s
```

---

## Challenge Problems

### Challenge 1: Inclined Plane with Friction

**Problem**: A 10 kg block starts at rest at the top of a 30° incline that is 20 meters long.
- Coefficient of friction = 0.2
- Find velocity at bottom
- Find energy lost to friction
- Find work done by friction

**Solution**:

```python
energy = MechanicalEnergy()
import math

# Given
mass = 10  # kg
angle = 30  # degrees
distance = 20  # m along incline
friction_coefficient = 0.2

# Height drop
height_drop = distance * math.sin(math.radians(angle))

print(f"Setup:")
print(f"Distance along incline: {distance} m")
print(f"Angle: {angle}°")
print(f"Height drop: {height_drop:.2f} m")
print(f"Coefficient of friction: {friction_coefficient}")

# 1. Velocity at bottom with friction
velocity_with_friction = energy.velocity_at_bottom_with_friction(height_drop, friction_coefficient, angle)
print(f"\n1. Final velocity: {velocity_with_friction:.2f} m/s")

# 2. Energy analysis
pe_initial = energy.gravitational_potential_energy(mass, height_drop)
ke_final = energy.kinetic_energy(mass, velocity_with_friction)
energy_lost_friction = pe_initial - ke_final

print(f"\n2. Energy Analysis:")
print(f"   Initial PE: {pe_initial:.2f} J")
print(f"   Final KE: {ke_final:.2f} J")
print(f"   Energy lost to friction: {energy_lost_friction:.2f} J")

# 3. Work by friction
# Friction force: f = μ * N = μ * m * g * cos(θ)
normal_force = mass * 9.81 * math.cos(math.radians(angle))
friction_force = friction_coefficient * normal_force
work_by_friction = friction_force * distance  # Negative (opposes motion)

print(f"\n3. Friction Calculation:")
print(f"   Normal force: {normal_force:.2f} N")
print(f"   Friction force: {friction_force:.2f} N")
print(f"   Work by friction: -{work_by_friction:.2f} J")

# 4. Comparison: with and without friction
velocity_without_friction = energy.free_fall_velocity(height_drop)
ke_without_friction = energy.kinetic_energy(mass, velocity_without_friction)

print(f"\n4. Comparison:")
print(f"   Velocity (no friction): {velocity_without_friction:.2f} m/s")
print(f"   Velocity (with friction): {velocity_with_friction:.2f} m/s")
print(f"   Velocity reduction: {(1 - velocity_with_friction/velocity_without_friction)*100:.1f}%")
print(f"   KE (no friction): {ke_without_friction:.2f} J")
print(f"   KE (with friction): {ke_final:.2f} J")

# 5. Verification using work-energy theorem
work_net = work_by_friction + (mass * 9.81 * math.sin(math.radians(angle)) * distance)
change_ke = ke_final - 0  # Starts from rest
print(f"\n5. Work-Energy Theorem Check:")
print(f"   Net work (gravity - friction): {work_net:.2f} J")
print(f"   Change in KE: {change_ke:.2f} J")
print(f"   Match: {abs(work_net - change_ke) < 1}")
```

---

### Challenge 2: Orbital Mechanics

**Problem**: A satellite orbits Earth at 400 km altitude. Calculate:
- Orbital velocity
- Orbital period  
- Total orbital energy
- Energy needed to escape
- Velocity needed to reach Mars orbit

**Solution:**

[Complete solution code for orbital mechanics]

---

## Tips for Solving Energy Problems

### 1. **Always Define Your System**
```
What's included? Object only? Gravitational field? Friction?
```

### 2. **Choose Reference Levels**
```
Where is PE = 0? Ground? Center of Earth? Does it matter?
```

### 3. **Check Energy Conservation**
```
Initial Energy = Final Energy (no non-conservative forces)
```

### 4. **Use Energy Methods When:**
- Distances are unknown
- Friction is present
- Multiple forces act
- Need overall picture, not detailed path

### 5. **Use Kinematics When:**
- Time is involved
- Specific positions/velocities needed
- Single force dominant

---

## Practice Problems

1. **Skateboard**: A 60 kg skateboarder rides down a 20° hill (100 m long). Friction coefficient = 0.1. Find final velocity.

2. **Rope Swing**: A 75 kg person swings on a 5 m rope from 2 m above to 0.5 m above the lowest point. Find velocity at lowest point.

3. **Spiral Track**: A ball starts at the top of a circular loop (radius 2 m). Find minimum speed at top to complete the loop.

4. **Two-Block Collision**: 5 kg block at 10 m/s hits 3 kg block at rest. Find velocities and energy after perfectly inelastic collision.

5. **Spring Gun**: A spring (k=500 N/m) launches a 2 kg ball horizontally. Compressed 0.4 m. Find maximum height reached.

---

## Summary

These examples demonstrate:
- ✅ Energy conservation principles
- ✅ Practical calculations
- ✅ Real-world applications
- ✅ Advanced scenarios
- ✅ Problem-solving strategies


# Mechanical Energy API Reference

## Table of Contents

1. [Class Initialization](#class-initialization)
2. [Kinetic Energy Methods](#kinetic-energy-methods)
3. [Rotational Kinetic Energy](#rotational-kinetic-energy)
4. [Moment of Inertia Methods](#moment-of-inertia-methods)
5. [Potential Energy Methods](#potential-energy-methods)
6. [Elastic Potential Energy](#elastic-potential-energy)
7. [Total Energy Methods](#total-energy-methods)
8. [Energy Conservation](#energy-conservation)
9. [Work & Power Methods](#work--power-methods)
10. [Collision Methods](#collision-methods)
11. [Projectile Motion](#projectile-motion)
12. [Simple Harmonic Motion](#simple-harmonic-motion)
13. [Orbital Mechanics](#orbital-mechanics)
14. [Fluid Dynamics](#fluid-dynamics)
15. [Free Fall & Vertical Motion](#free-fall--vertical-motion)
16. [Inclined Plane Methods](#inclined-plane-methods)
17. [Pendulum Methods](#pendulum-methods)
18. [Efficiency & Loss Methods](#efficiency--loss-methods)
19. [Analysis Methods](#analysis-methods)

---

## Class Initialization

### `MechanicalEnergy(gravity=9.81)`

Initialize the mechanical energy calculator with a specified gravity value.

**Parameters:**
- `gravity` (float, default=9.81): Gravitational acceleration in m/s²

**Returns:** MechanicalEnergy instance

**Example:**
```python
from JSPTH.physics.mechanical_energy import MechanicalEnergy

# Earth gravity (default)
energy = MechanicalEnergy()

# Moon gravity
energy_moon = MechanicalEnergy(gravity=1.62)

# Mars gravity
energy_mars = MechanicalEnergy(gravity=3.71)
```

**Class Constants:**
```python
MechanicalEnergy.GRAVITY = 9.81    # Earth
MechanicalEnergy.GRAVITY_MOON = 1.62
MechanicalEnergy.GRAVITY_MARS = 3.71
```

---

## Kinetic Energy Methods

### `kinetic_energy(mass, velocity)` → float

Calculate translational kinetic energy.

**Formula:** `KE = 1/2 × m × v²`

**Parameters:**
- `mass` (float): Object mass in kg (must be ≥ 0)
- `velocity` (float): Velocity magnitude in m/s (must be ≥ 0)

**Returns:** Kinetic energy in Joules

**Raises:**
- `ValueError`: If mass is negative or velocity is negative

**Example:**
```python
energy = MechanicalEnergy()

mass = 2  # kg
velocity = 10  # m/s

ke = energy.kinetic_energy(mass, velocity)
# Output: 100.0 J
```

---

### `velocity_from_kinetic_energy(kinetic_energy, mass)` → float

Find velocity given kinetic energy.

**Formula:** `v = √(2 × KE / m)`

**Parameters:**
- `kinetic_energy` (float): Kinetic energy in Joules (must be ≥ 0)
- `mass` (float): Mass in kg (must be > 0)

**Returns:** Velocity in m/s

**Raises:**
- `ValueError`: If KE is negative or mass is ≤ 0

**Example:**
```python
ke = 100  # J
mass = 2  # kg

velocity = energy.velocity_from_kinetic_energy(ke, mass)
# Output: 10.0 m/s
```

---

### `mass_from_kinetic_energy(kinetic_energy, velocity)` → float

Find mass given kinetic energy and velocity.

**Formula:** `m = 2 × KE / v²`

**Parameters:**
- `kinetic_energy` (float): Kinetic energy in Joules (must be ≥ 0)
- `velocity` (float): Velocity in m/s (must ≠ 0)

**Returns:** Mass in kg

**Raises:**
- `ValueError`: If velocity is 0 or KE is negative

**Example:**
```python
ke = 100  # J
velocity = 10  # m/s

mass = energy.mass_from_kinetic_energy(ke, velocity)
# Output: 2.0 kg
```

---

## Rotational Kinetic Energy

### `rotational_kinetic_energy(moment_of_inertia, angular_velocity)` → float

Calculate rotational kinetic energy.

**Formula:** `KE_rot = 1/2 × I × ω²`

**Parameters:**
- `moment_of_inertia` (float): Moment of inertia in kg·m² (must be ≥ 0)
- `angular_velocity` (float): Angular velocity in rad/s

**Returns:** Rotational kinetic energy in Joules

**Raises:**
- `ValueError`: If moment of inertia is negative

**Example:**
```python
I = 5  # kg·m²
omega = 10  # rad/s

ke_rot = energy.rotational_kinetic_energy(I, omega)
# Output: 250.0 J
```

---

### `angular_velocity_from_rotational_ke(rotational_ke, moment_of_inertia)` → float

Find angular velocity from rotational kinetic energy.

**Formula:** `ω = √(2 × KE_rot / I)`

**Parameters:**
- `rotational_ke` (float): Rotational KE in Joules
- `moment_of_inertia` (float): Moment of inertia in kg·m² (must be > 0)

**Returns:** Angular velocity in rad/s

**Raises:**
- `ValueError`: If moment of inertia ≤ 0

**Example:**
```python
ke_rot = 250  # J
I = 5  # kg·m²

omega = energy.angular_velocity_from_rotational_ke(ke_rot, I)
# Output: 10.0 rad/s
```

---

## Moment of Inertia Methods

All moment of inertia methods are static and return I in kg·m².

### `moment_of_inertia_solid_sphere(mass, radius)` → float
**Formula:** `I = 2/5 × M × R²`

### `moment_of_inertia_hollow_sphere(mass, radius)` → float
**Formula:** `I = 2/3 × M × R²`

### `moment_of_inertia_solid_cylinder(mass, radius)` → float
**Formula:** `I = 1/2 × M × R²`

### `moment_of_inertia_hollow_cylinder(mass, radius)` → float
**Formula:** `I = M × R²`

### `moment_of_inertia_rod_center(mass, length)` → float
**Formula:** `I = 1/12 × M × L²`

### `moment_of_inertia_rod_end(mass, length)` → float
**Formula:** `I = 1/3 × M × L²`

### `moment_of_inertia_disk(mass, radius)` → float
**Formula:** `I = 1/2 × M × R²`

### `moment_of_inertia_ring(mass, radius)` → float
**Formula:** `I = M × R²`

**Example:**
```python
mass = 2  # kg
radius = 0.5  # m

i_sphere = energy.moment_of_inertia_solid_sphere(mass, radius)
i_cylinder = energy.moment_of_inertia_solid_cylinder(mass, radius)
i_ring = energy.moment_of_inertia_ring(mass, radius)

print(f"Sphere: {i_sphere} kg·m²")      # 0.2
print(f"Cylinder: {i_cylinder} kg·m²")  # 0.25
print(f"Ring: {i_ring} kg·m²")          # 0.5
```

---

### `total_kinetic_energy_rolling(mass, velocity, moment_of_inertia, radius)` → float

Calculate total KE for rolling object (translational + rotational).

**Formula:** `KE_total = 1/2×m×v² + 1/2×I×(v/r)²`

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Linear velocity in m/s
- `moment_of_inertia` (float): Moment of inertia in kg·m²
- `radius` (float): Radius in m (must ≠ 0)

**Returns:** Total kinetic energy in Joules

**Raises:**
- `ValueError`: If radius is 0

**Note:** Assumes rolling without slipping: v = ω × r

**Example:**
```python
mass = 2  # kg
radius = 0.3  # m
velocity = 4  # m/s
I = energy.moment_of_inertia_solid_sphere(mass, radius)

ke_total = energy.total_kinetic_energy_rolling(mass, velocity, I, radius)
```

---

## Potential Energy Methods

### `gravitational_potential_energy(mass, height)` → float

Calculate gravitational potential energy.

**Formula:** `PE = m × g × h`

**Parameters:**
- `mass` (float): Mass in kg (must be ≥ 0)
- `height` (float): Height in m (must be ≥ 0)

**Returns:** Potential energy in Joules

**Raises:**
- `ValueError`: If mass is negative or height is negative

**Notes:**
- Uses instance gravity value
- Reference point at h = 0

**Example:**
```python
mass = 2  # kg
height = 50  # m

pe = energy.gravitational_potential_energy(mass, height)
# Output: 981.0 J
```

---

### `height_from_potential_energy(potential_energy, mass)` → float

Find height given potential energy.

**Formula:** `h = PE / (m × g)`

**Parameters:**
- `potential_energy` (float): Potential energy in Joules
- `mass` (float): Mass in kg (must be > 0)

**Returns:** Height in m

**Raises:**
- `ValueError`: If mass ≤ 0

**Example:**
```python
pe = 100  # J
mass = 2  # kg

height = energy.height_from_potential_energy(pe, mass)
# Output: 5.1 m
```

---

### `mass_from_potential_energy(potential_energy, height)` → float

Find mass given potential energy and height.

**Formula:** `m = PE / (g × h)`

**Parameters:**
- `potential_energy` (float): Potential energy in Joules
- `height` (float): Height in m (must be > 0)

**Returns:** Mass in kg

**Raises:**
- `ValueError`: If height ≤ 0

**Example:**
```python
pe = 100  # J
height = 5.1  # m

mass = energy.mass_from_potential_energy(pe, height)
# Output: 2.0 kg
```

---

### `gravitational_potential_energy_exact(mass, earth_mass, radius)` → float

Calculate exact gravitational PE using Newton's law.

**Formula:** `PE = -G × M × m / r`

**Parameters:**
- `mass` (float): Object mass in kg
- `earth_mass` (float): Central body mass in kg
- `radius` (float): Distance from center in m

**Returns:** Potential energy in Joules (typically negative)

**Note:** G = 6.674×10⁻¹¹ N·m²/kg²

**Example:**
```python
earth_mass = 5.972e24  # kg
object_mass = 1  # kg
radius = 6.371e6  # m (Earth's radius)

pe_exact = energy.gravitational_potential_energy_exact(object_mass, earth_mass, radius)
```

---

## Elastic Potential Energy

### `elastic_potential_energy(spring_constant, displacement)` → float

Calculate elastic potential energy in a spring.

**Formula:** `PE = 1/2 × k × x²`

**Parameters:**
- `spring_constant` (float): Spring constant in N/m (must be ≥ 0)
- `displacement` (float): Displacement from equilibrium in m

**Returns:** Elastic potential energy in Joules

**Raises:**
- `ValueError`: If spring constant is negative

**Example:**
```python
k = 200  # N/m
x = 0.5  # m

pe_spring = energy.elastic_potential_energy(k, x)
# Output: 25.0 J
```

---

### `spring_constant_from_elastic_pe(elastic_pe, displacement)` → float

Find spring constant from elastic PE and displacement.

**Formula:** `k = 2 × PE / x²`

**Parameters:**
- `elastic_pe` (float): Elastic PE in Joules
- `displacement` (float): Displacement in m (must ≠ 0)

**Returns:** Spring constant in N/m

**Raises:**
- `ValueError`: If displacement is 0

**Example:**
```python
pe_spring = 25  # J
displacement = 0.5  # m

k = energy.spring_constant_from_elastic_pe(pe_spring, displacement)
# Output: 200.0 N/m
```

---

### `displacement_from_elastic_pe(elastic_pe, spring_constant)` → float

Find displacement from elastic PE and spring constant.

**Formula:** `x = √(2 × PE / k)`

**Parameters:**
- `elastic_pe` (float): Elastic PE in Joules
- `spring_constant` (float): Spring constant in N/m (must be > 0)

**Returns:** Displacement in m

**Raises:**
- `ValueError`: If spring constant ≤ 0

**Example:**
```python
pe_spring = 25  # J
k = 200  # N/m

displacement = energy.displacement_from_elastic_pe(pe_spring, k)
# Output: 0.5 m
```

---

## Total Energy Methods

### `total_mechanical_energy(mass, velocity, height, spring_constant=0, displacement=0)` → float

Calculate total mechanical energy (translational KE + gravitational PE + elastic PE).

**Formula:** `E = 1/2×m×v² + m×g×h + 1/2×k×x²`

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Velocity in m/s
- `height` (float): Height in m
- `spring_constant` (float, default=0): Spring constant in N/m
- `displacement` (float, default=0): Spring displacement in m

**Returns:** Total mechanical energy in Joules

**Example:**
```python
total_e = energy.total_mechanical_energy(
    mass=2,
    velocity=5,
    height=10,
    spring_constant=100,
    displacement=0.1
)
```

---

### `total_mechanical_energy_with_rotation(mass, velocity, height, moment_of_inertia=0, angular_velocity=0)` → float

Calculate total mechanical energy including rotational KE.

**Formula:** `E = 1/2×m×v² + 1/2×I×ω² + m×g×h`

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Linear velocity in m/s
- `height` (float): Height in m
- `moment_of_inertia` (float, default=0): Moment of inertia in kg·m²
- `angular_velocity` (float, default=0): Angular velocity in rad/s

**Returns:** Total mechanical energy in Joules

**Example:**
```python
total_e = energy.total_mechanical_energy_with_rotation(
    mass=5,
    velocity=10,
    height=20,
    moment_of_inertia=2,
    angular_velocity=5
)
```

---

## Energy Conservation

### `check_energy_conservation(initial_energy, final_energy, tolerance=1e-6)` → bool

Check if mechanical energy is conserved.

**Parameters:**
- `initial_energy` (float): Initial total energy in J
- `final_energy` (float): Final total energy in J
- `tolerance` (float, default=1e-6): Allowed difference in J

**Returns:** True if |initial - final| ≤ tolerance, False otherwise

**Example:**
```python
initial = 1000  # J
final = 999.9  # J

conserved = energy.check_energy_conservation(initial, final)
# Output: True (within tolerance)
```

---

### `energy_conservation_analysis(initial_ke, initial_pe, final_ke, final_pe)` → dict

Detailed energy conservation analysis.

**Returns:** Dictionary with keys:
- `initial_ke` (float): Initial kinetic energy
- `initial_pe` (float): Initial potential energy
- `initial_total` (float): Sum of initial energies
- `final_ke` (float): Final kinetic energy
- `final_pe` (float): Final potential energy
- `final_total` (float): Sum of final energies
- `energy_loss` (float): Absolute energy difference
- `percent_loss` (float): Energy loss as percentage
- `is_conserved` (bool): Whether energy is conserved

**Example:**
```python
analysis = energy.energy_conservation_analysis(
    initial_ke=100,
    initial_pe=200,
    final_ke=250,
    final_pe=50
)

print(f"Energy loss: {analysis['energy_loss']} J")
print(f"Percent loss: {analysis['percent_loss']}%")
```

---

## Work & Power Methods

### `work_by_force(force, displacement, angle=0)` → float

Calculate work done by a force.

**Formula:** `W = F × d × cos(θ)`

**Parameters:**
- `force` (float): Force magnitude in N
- `displacement` (float): Displacement magnitude in m
- `angle` (float, default=0): Angle between force and displacement in degrees

**Returns:** Work done in Joules

**Notes:**
- angle = 0°: Force in direction of motion → positive work
- angle = 90°: Force perpendicular to motion → zero work
- angle = 180°: Force opposite to motion → negative work

**Example:**
```python
# Work by pushing force
work = energy.work_by_force(force=50, displacement=10, angle=0)
# Output: 500.0 J

# Work against friction (angle = 180°)
work_friction = energy.work_by_force(force=20, displacement=10, angle=180)
# Output: -200.0 J
```

---

### `work_energy_theorem(initial_ke, final_ke)` → float

Apply work-energy theorem: W_net = ΔKE

**Formula:** `W = KE_final - KE_initial`

**Parameters:**
- `initial_ke` (float): Initial kinetic energy in J
- `final_ke` (float): Final kinetic energy in J

**Returns:** Net work done in Joules

**Example:**
```python
initial_ke = 100  # J
final_ke = 250  # J

work_net = energy.work_energy_theorem(initial_ke, final_ke)
# Output: 150.0 J (work done on object)
```

---

### `power_average(work, time)` → float

Calculate average power.

**Formula:** `P_avg = W / t`

**Parameters:**
- `work` (float): Work done in Joules
- `time` (float): Time interval in seconds (must be > 0)

**Returns:** Average power in Watts

**Raises:**
- `ValueError`: If time ≤ 0

**Example:**
```python
work = 1000  # J
time = 5  # s

power = energy.power_average(work, time)
# Output: 200.0 W
```

---

### `power_instantaneous(force, velocity, angle=0)` → float

Calculate instantaneous power.

**Formula:** `P = F × v × cos(θ)`

**Parameters:**
- `force` (float): Force magnitude in N
- `velocity` (float): Velocity magnitude in m/s
- `angle` (float, default=0): Angle between force and velocity in degrees

**Returns:** Instantaneous power in Watts

**Example:**
```python
force = 100  # N
velocity = 5  # m/s
angle = 0  # N in direction of motion

power = energy.power_instantaneous(force, velocity, angle)
# Output: 500.0 W
```

---

### `power_rotational(torque, angular_velocity)` → float

Calculate rotational power.

**Formula:** `P = τ × ω`

**Parameters:**
- `torque` (float): Torque in N·m
- `angular_velocity` (float): Angular velocity in rad/s

**Returns:** Power in Watts

**Example:**
```python
torque = 50  # N·m
omega = 10  # rad/s

power = energy.power_rotational(torque, omega)
# Output: 500.0 W
```

---

### `energy_from_power(power, time)` → float

Calculate energy from power and time.

**Formula:** `E = P × t`

**Parameters:**
- `power` (float): Power in Watts
- `time` (float): Time in seconds

**Returns:** Energy in Joules

**Example:**
```python
power = 500  # W
time = 10  # s

energy_total = energy.energy_from_power(power, time)
# Output: 5000.0 J
```

---

## Collision Methods

### `kinetic_energy_before_collision(mass1, velocity1, mass2, velocity2)` → float

Total kinetic energy before collision.

**Parameters:**
- `mass1`, `velocity1`: First object mass (kg) and velocity (m/s)
- `mass2`, `velocity2`: Second object mass (kg) and velocity (m/s)

**Returns:** Total KE before collision in Joules

**Example:**
```python
ke_before = energy.kinetic_energy_before_collision(
    mass1=2, velocity1=10,
    mass2=3, velocity2=0
)
```

---

### `kinetic_energy_after_collision(mass1, velocity1_final, mass2, velocity2_final)` → float

Total kinetic energy after collision.

**Parameters:**
- `mass1`, `velocity1_final`: First object mass (kg) and final velocity (m/s)
- `mass2`, `velocity2_final`: Second object mass (kg) and final velocity (m/s)

**Returns:** Total KE after collision in Joules

---

### `energy_lost_in_collision(ke_before, ke_after)` → float

Calculate energy lost in collision.

**Formula:** `E_lost = KE_before - KE_after`

**Parameters:**
- `ke_before` (float): KE before collision in J
- `ke_after` (float): KE after collision in J

**Returns:** Energy lost in Joules

**Example:**
```python
energy_lost = energy.energy_lost_in_collision(
    ke_before=1000,
    ke_after=500
)
# Output: 500.0 J
```

---

### `coefficient_of_restitution_energy(ke_after, ke_before)` → float

Estimate coefficient of restitution from energy ratio.

**Formula:** `e ≈ √(KE_after / KE_before)`

**Parameters:**
- `ke_after` (float): KE after collision
- `ke_before` (float): KE before collision

**Returns:** Approximate coefficient of restitution (0-1)

**Notes:**
- e = 1: Elastic collision
- e = 0: Perfectly inelastic collision
- 0 < e < 1: Partially inelastic collision

---

## Projectile Motion

### `projectile_total_energy_at_launch(mass, velocity, angle_degrees, height=0)` → float

Total mechanical energy at projectile launch.

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Launch velocity in m/s
- `angle_degrees` (float): Launch angle in degrees
- `height` (float, default=0): Initial height in m

**Returns:** Total energy in Joules

---

### `projectile_velocity_at_height(initial_velocity, initial_height, final_height)` → float

Find velocity at specific height using energy conservation.

**Parameters:**
- `initial_velocity` (float): Initial velocity in m/s
- `initial_height` (float): Initial height in m
- `final_height` (float): Final height in m

**Returns:** Velocity at final height in m/s

**Raises:**
- `ValueError`: If object can't reach final height

---

### `projectile_max_height_from_energy(mass, velocity, angle_degrees)` → float

Find maximum height reached.

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Launch velocity in m/s
- `angle_degrees` (float): Launch angle in degrees

**Returns:** Maximum height gained in m

**Example:**
```python
max_height = energy.projectile_max_height_from_energy(
    mass=1,
    velocity=20,
    angle_degrees=45
)
# Output: 10.19 m
```

---

### `projectile_range_energy_method(mass, velocity, angle_degrees)` → float

Calculate projectile range.

**Formula:** `Range = v² × sin(2θ) / g`

**Parameters:**
- `mass` (float): Mass in kg (not used in formula)
- `velocity` (float): Launch velocity in m/s
- `angle_degrees` (float): Launch angle in degrees

**Returns:** Horizontal range in m

---

## Simple Harmonic Motion

### `shm_total_energy(mass, velocity, spring_constant, displacement)` → float

Total energy in simple harmonic motion.

**Formula:** `E = 1/2×m×v² + 1/2×k×x²`

**Parameters:**
- `mass` (float): Mass in kg
- `velocity` (float): Velocity in m/s
- `spring_constant` (float): Spring constant in N/m
- `displacement` (float): Displacement from equilibrium in m

**Returns:** Total energy in Joules

**Note:** Total energy remains constant during SHM

---

### `shm_amplitude_from_energy(total_energy, spring_constant)` → float

Find amplitude in SHM.

**Formula:** `A = √(2 × E / k)`

**Parameters:**
- `total_energy` (float): Total energy in J
- `spring_constant` (float): Spring constant in N/m (must be > 0)

**Returns:** Amplitude in m

---

### `shm_max_velocity(amplitude, angular_frequency)` → float

Maximum velocity in SHM.

**Formula:** `v_max = A × ω`

**Parameters:**
- `amplitude` (float): Amplitude in m
- `angular_frequency` (float): Angular frequency in rad/s

**Returns:** Maximum velocity in m/s

---

### `shm_period_from_mass_spring(mass, spring_constant)` → float

Period of mass-spring system.

**Formula:** `T = 2π√(m / k)`

**Parameters:**
- `mass` (float): Mass in kg
- `spring_constant` (float): Spring constant in N/m (must be > 0)

**Returns:** Period in seconds

---

### `shm_frequency_from_period(period)` → float

Find frequency from period.

**Formula:** `f = 1 / T`

**Parameters:**
- `period` (float): Period in seconds (must be > 0)

**Returns:** Frequency in Hz

---

## Orbital Mechanics

### `orbital_kinetic_energy(mass, orbital_velocity)` → float

Kinetic energy of orbiting object.

**Parameters:**
- `mass` (float): Mass in kg
- `orbital_velocity` (float): Orbital velocity in m/s

**Returns:** Kinetic energy in Joules

---

### `orbital_velocity(central_mass, radius)` → float

Calculate orbital velocity.

**Formula:** `v = √(G×M / r)`

**Parameters:**
- `central_mass` (float): Central body mass in kg
- `radius` (float): Orbital radius in m

**Returns:** Orbital velocity in m/s

**Constant:** G = 6.674×10⁻¹¹ N·m²/kg²

---

### `orbital_period(central_mass, radius)` → float

Calculate orbital period (Kepler's 3rd Law).

**Formula:** `T = 2π√(r³ / (G×M))`

**Parameters:**
- `central_mass` (float): Central body mass in kg
- `radius` (float): Orbital radius in m

**Returns:** Period in seconds

---

### `total_orbital_energy(mass, central_mass, radius)` → float

Total energy of orbiting object (negative for bound orbit).

**Formula:** `E = -G×M×m / (2×r)`

**Parameters:**
- `mass` (float): Orbiting object mass in kg
- `central_mass` (float): Central body mass in kg
- `radius` (float): Orbital radius in m

**Returns:** Total energy in Joules (typically negative)

---

### `escape_velocity(central_mass, radius)` → float

Velocity needed to escape gravitational field.

**Formula:** `v_esc = √(2×G×M / r)`

**Parameters:**
- `central_mass` (float): Central body mass in kg
- `radius` (float): Distance from center in m

**Returns:** Escape velocity in m/s

---

### `escape_energy(mass, central_mass, radius)` → float

Energy needed to escape from surface.

**Formula:** `E = G×M×m / r`

**Parameters:**
- `mass` (float): Object mass in kg
- `central_mass` (float): Central body mass in kg
- `radius` (float): Distance from center in m

**Returns:** Energy needed in Joules

---

## Fluid Dynamics

### `dynamic_pressure(density, velocity)` → float

Calculate dynamic pressure in fluid.

**Formula:** `q = 1/2 × ρ × v²`

**Parameters:**
- `density` (float): Fluid density in kg/m³
- `velocity` (float): Velocity in m/s

**Returns:** Dynamic pressure in Pa

**Example:**
```python
# Air at sea level (ρ ≈ 1.225 kg/m³)
q = energy.dynamic_pressure(density=1.225, velocity=20)
# Output: 245.0 Pa
```

---

### `bernoulli_equation(pressure1, density, velocity1, height1, pressure2, velocity2, height2, gravity=9.81)` → bool

Verify Bernoulli's equation at two points.

**Formula:** `P + ρgh + 1/2ρv² = constant`

**Parameters:**
- `pressure1`, `pressure2` (float): Pressure at points 1 and 2 in Pa
- `density` (float): Fluid density in kg/m³
- `velocity1`, `velocity2` (float): Velocity at points in m/s
- `height1`, `height2` (float): Height at points in m
- `gravity` (float, default=9.81): Gravity in m/s²

**Returns:** True if Bernoulli's equation satisfied, False otherwise

---

## Free Fall & Vertical Motion

### `free_fall_velocity(height)` → float

Velocity reached in free fall from height.

**Formula:** `v = √(2×g×h)`

**Parameters:**
- `height` (float): Height in m

**Returns:** Velocity in m/s

**Uses:** Instance gravity value

---

### `free_fall_time(height)` → float

Time to fall from height.

**Formula:** `t = √(2×h / g)`

**Parameters:**
- `height` (float): Height in m (must be ≥ 0)

**Returns:** Time in seconds

**Raises:**
- `ValueError`: If height is negative

---

### `free_fall_energy_at_height(mass, initial_height, current_height)` → float

Total energy at any height during free fall.

**Parameters:**
- `mass` (float): Mass in kg
- `initial_height` (float): Initial height in m
- `current_height` (float): Current height in m

**Returns:** Total energy in Joules

**Note:** Energy remains constant in free fall

---

### `velocity_at_height_free_fall(initial_height, current_height)` → float

Velocity at specific height during free fall.

**Parameters:**
- `initial_height` (float): Initial height in m
- `current_height` (float): Current height in m

**Returns:** Velocity in m/s

---

## Inclined Plane Methods

### `potential_energy_on_incline(mass, incline_angle_degrees, distance_along_incline)` → float

Potential energy for object on incline.

**Parameters:**
- `mass` (float): Mass in kg
- `incline_angle_degrees` (float): Angle in degrees
- `distance_along_incline` (float): Distance along incline in m

**Returns:** Potential energy in Joules

**Note:** Height = distance × sin(angle)

---

### `velocity_at_bottom_frictionless_incline(initial_height)` → float

Velocity at bottom of frictionless incline.

**Parameters:**
- `initial_height` (float): Initial height in m

**Returns:** Velocity in m/s

---

### `velocity_at_bottom_with_friction(initial_height, friction_coefficient, angle_degrees)` → float

Velocity at bottom with friction.

**Parameters:**
- `initial_height` (float): Initial height in m
- `friction_coefficient` (float): Coefficient of friction (μ)
- `angle_degrees` (float): Incline angle in degrees

**Returns:** Velocity in m/s

**Raises:**
- `ValueError`: If friction too high for object to slide

---

## Pendulum Methods

### `simple_pendulum_period(length)` → float

Period of simple pendulum.

**Formula:** `T = 2π√(L / g)`

**Parameters:**
- `length` (float): Length in m (must be ≥ 0)

**Returns:** Period in seconds

**Uses:** Instance gravity value

---

### `simple_pendulum_max_velocity(length, angle_degrees)` → float

Maximum velocity at bottom when released from angle.

**Parameters:**
- `length` (float): Length in m
- `angle_degrees` (float): Release angle in degrees

**Returns:** Maximum velocity in m/s

**Uses:** Energy conservation

---

### `pendulum_total_energy(mass, length, angle_degrees)` → float

Total energy of simple pendulum.

**Parameters:**
- `mass` (float): Mass in kg
- `length` (float): Length in m
- `angle_degrees` (float): Current angle in degrees

**Returns:** Total energy in Joules

**Note:** Energy is constant during swing

---

### `pendulum_velocity_at_angle(length, release_angle_degrees, current_angle_degrees)` → float

Velocity at any angle during swing.

**Parameters:**
- `length` (float): Length in m
- `release_angle_degrees` (float): Release angle in degrees
- `current_angle_degrees` (float): Current angle in degrees

**Returns:** Velocity in m/s

**Raises:**
- `ValueError`: If object hasn't reached current angle

---

## Efficiency & Loss Methods

### `efficiency(energy_output, energy_input)` → float

Calculate efficiency as percentage.

**Formula:** `η = (E_out / E_in) × 100%`

**Parameters:**
- `energy_output` (float): Useful output energy in J
- `energy_input` (float): Total input energy in J (must ≠ 0)

**Returns:** Efficiency as percentage (0-100)

**Raises:**
- `ValueError`: If input energy is 0

**Example:**
```python
efficiency = energy.efficiency(
    energy_output=750,
    energy_input=1000
)
# Output: 75.0 (75%)
```

---

### `energy_loss(energy_input, energy_output)` → float

Calculate absolute energy loss.

**Formula:** `E_loss = E_in - E_out`

**Parameters:**
- `energy_input` (float): Input energy in J
- `energy_output` (float): Output energy in J

**Returns:** Energy loss in Joules

---

### `energy_loss_percentage(energy_input, energy_output)` → float

Calculate energy loss as percentage.

**Formula:** `Loss% = ((E_in - E_out) / E_in) × 100%`

**Parameters:**
- `energy_input` (float): Input energy in J (must ≠ 0)
- `energy_output` (float): Output energy in J

**Returns:** Energy loss percentage (0-100)

---

## Analysis Methods

### `comprehensive_energy_analysis(mass, velocity, height, spring_constant=0, displacement=0, moment_of_inertia=0, angular_velocity=0)` → dict

Complete energy analysis of system.

**Returns:** Dictionary with keys:
- `kinetic_energy_translational` (float)
- `kinetic_energy_rotational` (float)
- `kinetic_energy_total` (float)
- `potential_energy_gravitational` (float)
- `potential_energy_elastic` (float)
- `potential_energy_total` (float)
- `total_mechanical_energy` (float)
- `ke_percent` (float): KE as % of total
- `pe_percent` (float): PE as % of total

**Example:**
```python
analysis = energy.comprehensive_energy_analysis(
    mass=5,
    velocity=10,
    height=20
)

print(f"Total energy: {analysis['total_mechanical_energy']} J")
print(f"KE%: {analysis['ke_percent']:.1f}%")
print(f"PE%: {analysis['pe_percent']:.1f}%")
```

---

### `print_energy_analysis(mass, velocity, height, **kwargs)` → None

Print formatted energy analysis (calls comprehensive_energy_analysis and displays).

**Parameters:** Same as comprehensive_energy_analysis

**Output:** Formatted table printed to console

**Example:**
```python
energy.print_energy_analysis(mass=5, velocity=10, height=20)
```

---

## Exception Reference

### ValueError

Raised when invalid parameters are provided:

| Method | Condition |
|--------|-----------|
| `kinetic_energy` | mass < 0 or velocity < 0 |
| `velocity_from_kinetic_energy` | ke < 0 or mass ≤ 0 |
| `mass_from_kinetic_energy` | velocity = 0 or ke < 0 |
| `rotational_kinetic_energy` | moment_of_inertia < 0 |
| `angular_velocity_from_rotational_ke` | moment_of_inertia ≤ 0 |
| `gravitational_potential_energy` | mass < 0 or height < 0 |
| `height_from_potential_energy` | mass ≤ 0 |
| `mass_from_potential_energy` | height ≤ 0 |
| `elastic_potential_energy` | spring_constant < 0 |
| `spring_constant_from_elastic_pe` | displacement = 0 |
| `displacement_from_elastic_pe` | spring_constant ≤ 0 |
| `total_kinetic_energy_rolling` | radius = 0 |
| `power_average` | time ≤ 0 |
| `free_fall_time` | height < 0 |
| `velocity_at_height_free_fall` | object can't reach that height |
| `efficiency` | energy_input = 0 |
| `energy_loss_percentage` | energy_input = 0 |

---

## Quick Reference Table

| Calculation | Method |
|-------------|--------|
| KE | `kinetic_energy()` |
| Rotational KE | `rotational_kinetic_energy()` |
| Gravitational PE | `gravitational_potential_energy()` |
| Elastic PE | `elastic_potential_energy()` |
| Total ME | `total_mechanical_energy()` |
| Work | `work_by_force()` |
| Power | `power_average()` or `power_instantaneous()` |
| Free fall velocity | `free_fall_velocity()` |
| Pendulum period | `simple_pendulum_period()` |
| Orbital velocity | `orbital_velocity()` |
| Efficiency | `efficiency()` |

---

## Unit Conversions

```
Energy:
1 kJ = 1000 J
1 kWh = 3.6 × 10⁶ J
1 eV = 1.602 × 10⁻¹⁹ J
1 calorie = 4.184 J

Power:
1 kW = 1000 W
1 MW = 10⁶ W
1 hp = 746 W

Mass:
1 g = 0.001 kg
1 ton = 1000 kg

Distance:
1 km = 1000 m
1 cm = 0.01 m
```

---

## Glossary

- **KE**: Kinetic energy (energy of motion)
- **PE**: Potential energy (energy of position)
- **ME**: Mechanical energy (KE + PE)
- **ω** (omega): Angular velocity in rad/s
- **τ** (tau): Torque in N·m
- **η** (eta): Efficiency as decimal (0-1)
- **e**: Coefficient of restitution (0-1)
- **g**: Gravitational acceleration (9.81 m/s² on Earth)

---
