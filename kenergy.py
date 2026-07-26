import unittest
from JSPTH.physics.energy.kinetic_energy import KineticEnergyCalculator

class TestKineticEnergy(unittest.TestCase):
    def setUp(self):
        self.calc = KineticEnergyCalculator()
    
    def test_kinetic_energy_basic(self):
        """Test basic KE calculation"""
        ke = self.calc.kinetic_energy(100, 10)
        self.assertEqual(ke, 5000)
    
    def test_velocity_from_ke(self):
        """Test inverse calculation"""
        v = self.calc.velocity_from_kinetic_energy(5000, 100)
        self.assertAlmostEqual(v, 10, places=10)
    
    def test_energy_conservation_elastic(self):
        """Test elastic collision conserves energy"""
        ke_i, ke_f = self.calc.elastic_collision_kinetic_energy(2, 10, 3, 0)
        self.assertAlmostEqual(ke_i, ke_f, places=9)
    
    def test_invalid_negative_mass(self):
        """Test that negative mass raises error"""
        with self.assertRaises(ValueError):
            self.calc.kinetic_energy(-100, 10)
    
    def test_relativistic_vs_classical(self):
        """Compare relativistic and classical at low speeds"""
        mass = 1
        velocity = 0.01 * self.calc.SPEED_OF_LIGHT
        
        ke_classical = self.calc.kinetic_energy(mass, velocity)
        ke_relativistic = self.calc.relativistic_kinetic_energy(mass, velocity)
        
        # Should be very similar at low speeds
        ratio = ke_relativistic / ke_classical
        self.assertAlmostEqual(ratio, 1.0, places=4)

if __name__ == '__main__':
    unittest.main()