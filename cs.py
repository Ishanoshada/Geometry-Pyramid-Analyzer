
# ===========================================================
# Research by Ishan Oshada
# Email: ishan.kodithuwakku.offical@gmail.com
# ===========================================================


import numpy as np
import math
import random
import os

import math
import numpy as np

constants = {
    'pi': math.pi,  # Pi
    'golden_ratio': (1 + np.sqrt(5)) / 2,  # Golden Ratio
    'tribonacci': 1.839286755,  # Tribonacci constant
    #'e': math.e,  # Euler's Number
    #'phi': (1 + np.sqrt(5)) / 2,  # Phi (Golden Ratio)

    # # Square roots of small integers
    #'sqrt_2': np.sqrt(2),  # Square root of 2
    # 'sqrt_3': np.sqrt(3),  # Square root of 3
    # 'sqrt_5': np.sqrt(5),  # Square root of 5
    # 'sqrt_7': np.sqrt(7),  # Square root of 7
    # 'sqrt_11': np.sqrt(11),  # Square root of 11
    # 'sqrt_13': np.sqrt(13),  # Square root of 13
    # 'sqrt_17': np.sqrt(17),  # Square root of 17
    # 'sqrt_19': np.sqrt(19),  # Square root of 19
    # 'sqrt_23': np.sqrt(23),  # Square root of 23
    # 'sqrt_29': np.sqrt(29),  # Square root of 29
    # 'sqrt_31': np.sqrt(31),  # Square root of 31
    # 'sqrt_37': np.sqrt(37),  # Square root of 37
    # 'sqrt_41': np.sqrt(41),  # Square root of 41

    # # Square roots of larger numbers
    # 'sqrt_50': np.sqrt(50),  # Square root of 50
    # 'sqrt_200': np.sqrt(200),  # Square root of 200
    # 'sqrt_500': np.sqrt(500),  # Square root of 500

    # # Logarithmic constants
    # 'ln2': np.log(2),  # Natural logarithm of 2

    # # Irrational and transcendental constants
    # 'sqrt_3_over_2': np.sqrt(3) / 2,  # sqrt(3) / 2
    # 'sqrt_5_over_2': np.sqrt(5) / 2,  # sqrt(5) / 2
    # 'sqrt_7_over_2': np.sqrt(7) / 2,  # sqrt(7) / 2
    # 'sqrt_11_over_3': np.sqrt(11) / 3,  # sqrt(11) / 3
    # 'sqrt_13_over_3': np.sqrt(13) / 3,  # sqrt(13) / 3

    # # Advanced constants (Geometrical)
    # 'sqrt_2_over_2': np.sqrt(2) / 2,  # sqrt(2) / 2 (Geometric constant)
    # 'sqrt_5_over_3': np.sqrt(5) / 3,  # sqrt(5) / 3 (Geometric constant)

    # # More transcendental constants (some values for e, pi)
    # 'e_squared': math.e**2,  # Euler's number squared
    # 'pi_squared': math.pi**2,  # Pi squared

    # # More advanced irrational constants
    # 'sqrt_1001': np.sqrt(1001),  # Square root of 1001
    # 'sqrt_1234': np.sqrt(1234),  # Square root of 1234
    # 'sqrt_2048': np.sqrt(2048),  # Square root of 2048
    # 'sqrt_4096': np.sqrt(4096),  # Square root of 4096

    # # Difficult Roots of Large Prime Numbers
    # 'sqrt_1019': np.sqrt(1019),  # Square root of a large prime number
    # 'sqrt_2027': np.sqrt(2027),  # Square root of a large prime number
    # 'sqrt_3053': np.sqrt(3053),  # Square root of a large prime number
    # 'sqrt_4099': np.sqrt(4099),  # Square root of a large prime number
    # 'sqrt_5009': np.sqrt(5009),  # Square root of a large prime number

    # # Cube Roots of Large Numbers
    # 'cbrt_1000000': np.cbrt(1000000),  # Cube root of 1,000,000
    # 'cbrt_1250000': np.cbrt(1250000),  # Cube root of 1,250,000
    # 'cbrt_2000000': np.cbrt(2000000),  # Cube root of 2,000,000
    # 'cbrt_3150000': np.cbrt(3150000),  # Cube root of 3,150,000

    # # Fourth Roots of Numbers
    # 'sqrt_4_625': np.sqrt(np.sqrt(625)),  # Fourth root of 625
    # 'sqrt_4_1024': np.sqrt(np.sqrt(1024)),  # Fourth root of 1024
    # 'sqrt_4_2500': np.sqrt(np.sqrt(2500)),  # Fourth root of 2500
    # 'sqrt_4_10000': np.sqrt(np.sqrt(10000)),  # Fourth root of 10000

    # # Roots of Larger Exponents
    # 'root_5_3125': np.power(3125, 1/5),  # 5th root of 3125
    # 'root_6_46656': np.power(46656, 1/6),  # 6th root of 46656
    # 'root_7_823543': np.power(823543, 1/7),  # 7th root of 823543

    # # Roots of Composite Numbers (Difficult Roots)
    # 'sqrt_12345': np.sqrt(12345),  # Square root of 12345
    # 'sqrt_98765': np.sqrt(98765),  # Square root of 98765
    # 'sqrt_123456': np.sqrt(123456),  # Square root of 123456
    # 'sqrt_999999': np.sqrt(999999),  # Square root of 999999
    # 'sqrt_9999999': np.sqrt(9999999),  # Square root of 9999999

    # # Higher Order Roots of Composite Numbers
    # 'root_3_998001': np.cbrt(998001),  # Cube root of 998001
    # 'root_4_1048576': np.sqrt(np.sqrt(1048576)),  # 4th root of 1048576
    # 'root_5_317052': np.power(317052, 1/5),  # 5th root of 317052
    # 'root_6_16777216': np.power(16777216, 1/6),  # 6th root of 16777216

    # # More Roots with Difficult Computations
    # 'sqrt_5000000': np.sqrt(5000000),  # Square root of 5000000

    # # Universal Constants
    # 'speed_of_light': 299792458,  # Speed of light in m/s
    # 'speed_of_light2': 2.997924,
    # 'gravitational_constant': 6.67430,  # Gravitational constant in m^3 kg^-1 s^-2
    # 'planck_constant': 6.626070,  # Planck's constant in J·s
    # 'boltzmann_constant': 1.38064,  # Boltzmann constant in J/K
    # 'avogadro_number': 6.0221407,  # Avogadro's number in mol^-1
    # 'gas_constant': 8.3145,  # Gas constant in J/(mol·K)
}

# constants.update({
#     # # Universal Constants
#     # 'fine_structure_constant': 7.297352,  # Fine structure constant (dimensionless)
#     # #'magnetic_constant': 4 * np.pi * 1e-7,  # Magnetic constant (μ₀) in N/A²
#     # 'electric_constant': 8.85418781,  # Electric constant (ε₀) in F/m
#     # 'earth_mass': 5.97237,  # Earth mass in kg
#     # 'earth_radius': 6371000,  # Earth radius in meters
#     # # 'solar_mass': 1.989e3,  # Solar mass in kg
#     # # 'solar_radius': 696340000,  # Solar radius in meters
#     # # 'sun_temperature': 5778,  # Sun's surface temperature in K
#     # # 'jupiter_mass': 1.898e27,  # Jupiter's mass in kg
#     # # 'jupiter_radius': 69911000,  # Jupiter's radius in meters
#     # # 'moon_mass': 7.34767309e22,  # Moon's mass in kg
#     # # 'moon_radius': 1737100,  # Moon's radius in meters
#     # # 'planck_length': 1.616255e-35,  # Planck length in meters
#     # # 'planck_time': 5.391247e-44,  # Planck time in seconds
#     # # 'planck_mass': 2.176434e-8,  # Planck mass in kg
#     # 'planck_temperature': 1.416784,  # Planck temperature in K
#     # 'planck_charge': 1.875545956,  # Planck charge in coulombs
#     # 'hubble_constant': 2.3e-18,  # Hubble constant in s^-1 (approx.)
#     # 'dark_energy_density': 1.2e-29,  # Dark energy density in g/cm³
#     # 'dark_matter_density': 5e-27,  # Dark matter density in kg/m³
#     # 'solar_luminosity': 3.828e26,  # Solar luminosity in watts
#     # 'earth_gravity': 9.80665,  # Earth's gravity acceleration in m/s²
#     # 'earth_surface_gravity': 9.81,  # Earth's surface gravity in m/s²
#     # 'gravitational_wave_speed': 299792458,  # Gravitational wave speed (speed of light) in m/s
# })

