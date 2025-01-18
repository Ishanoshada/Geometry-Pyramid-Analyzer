
# ===========================================================
# Research by Ishan Oshada
# Email: ishan.kodithuwakku.offical@gmail.com
# ===========================================================


import numpy as np
import random
import os
import cs
import sys

try:
    fname = sys.argv[1]
except:
    fname = "pyramid_results_n.txt"

class Pyramid:
    def __init__(self, base_length_north, base_length_east, height):
        """
        Initialize pyramid with base lengths and height
        """
        self.base_length_north = base_length_north
        self.base_length_east = base_length_east
        self.height = height
        self.half_base = base_length_north / 2
        self.apothem = np.sqrt(self.height**2 + self.half_base**2)
        self.edge = np.sqrt(self.height**2 + self.half_base**2)
        self.diagonal_base = np.sqrt(base_length_north**2 + base_length_east**2)

    def safe_tan(self, value):
        """ Return tan(value) only if within safe bounds. """
        try:
            return np.tan(value) if abs(value) < 100 else 0
        except Exception:
            return 0

    def safe_cos(self, value):
        
        """ Return cos(value) only if within safe bounds. """
        try:
            return np.cos(value) if abs(value) < 100 else 0
        except Exception:
            return 0

    def safe_sin(self, value):
        """ Return sin(value) only if within safe bounds. """
        try:
            return np.sin(value) if abs(value) < 100 else 0
        except Exception:
            return 0

    def safe_log(self, value):
        """ Return log(value) only if value > 0. """
        try:
            return np.log(value) if value > 0 else 0
        except Exception:
            return 0

    def random_calculate_length(self):
        """
        Randomly combine lengths and apply random operations
        """
        # List of potential lengths with names
        lengths = [
            ('base_length_north', self.base_length_north),
            ('base_length_east', self.base_length_east),
            ('height', self.height),
            ('half_base', self.half_base),
            ('apothem', self.apothem),
            ('edge', self.edge),
            ('diagonal_base', self.diagonal_base)
        ]
        
        # Randomly select a number of lengths (between 2 and 6)
        num_lengths = random.randint(2, 6)
        selected_lengths = random.sample(lengths, num_lengths)
        
        # Randomly choose a math operation to apply between lengths
        operations = ['+', '-', '*', '/', '**', 'sqrt', 'log', 'sin', 'cos', 'tan']
        
        result = selected_lengths[0][1]  # Start with the first selected length
        formula = selected_lengths[0][0]  # Start formula with first length name
        
        for i in range(1, len(selected_lengths)):
            operation = random.choice(operations)
            length_value = selected_lengths[i][1]
            length_name = selected_lengths[i][0]
            
            try:
                if operation == '+':
                    result += length_value
                    formula += f" + {length_name}"
                elif operation == '-':
                    result -= length_value
                    formula += f" - {length_name}"
                elif operation == '*':
                    result *= length_value
                    formula += f" * {length_name}"
                elif operation == '/':
                    result /= length_value if length_value != 0 else 1
                    formula += f" / {length_name}"
                elif operation == '**':
                    result = result**length_value if abs(result) < 1e308 else 0
                    formula += f" ** {length_name}"
                elif operation == 'sqrt':
                    if result >= 0:
                        result = np.sqrt(result)
                        formula = f"sqrt({formula})"
                    else:
                        return None, None, None  # Skip invalid operations (e.g., sqrt(negative))
                elif operation == 'log':
                    if result > 0:
                        result = self.safe_log(result)
                        formula = f"log({formula})"
                    else:
                        return None, None, None  # Skip invalid operations (e.g., log(negative))
                elif operation == 'sin':
                    result = self.safe_sin(result)
                    formula = f"sin({formula})"
                elif operation == 'cos':
                    result = self.safe_cos(result)
                    formula = f"cos({formula})"
                elif operation == 'tan':
                    result = self.safe_tan(result)
                    formula = f"tan({formula})"
            except Exception as e:
                continue  # Skip any invalid operations (e.g., log(negative), sqrt(negative))
        
        return result, formula, [length_name for length_name, _ in selected_lengths]

    def compare_constants(self, threshold=0.0001):
        """
        Compare calculated lengths with constants, and check for low differences
        """
        constants = cs.constants  # Ensure this imports your constants correctly

        # To store previously used formulas and lengths
        used_formulas = set()

        # Keep running until a result is found
        while True:
            calculated_value, formula, length_names = self.random_calculate_length()
            
            if formula is None:  # Skip invalid operations
                continue
            
            # Get the values for the lengths used in the formula
            length_values = [getattr(self, length_name) for length_name in length_names]

            # Check if the formula is already in the used formulas set
            formula_key = f"{formula} => {', '.join(length_names)}"
            if formula_key in used_formulas:
                continue  # Skip saving this formula if it's already used

            for constant_name, constant_value in constants.items():
                # Compare calculated value to each constant
                difference = abs(calculated_value - constant_value)
                
                if difference < threshold:
                    # Prepare the result to be saved to the file
                    result_text = f"\nLow Difference Found:\n"
                    result_text += f"Constant: {constant_name}\n"
                    result_text += f"Calculated Value: {calculated_value:.6f}\n"
                    result_text += f"Actual Value: {constant_value:.6f}\n"
                    result_text += f"Difference: {difference:.6f}\n"
                    result_text += f"Formula Used: {formula}\n"
                    result_text += f"Lengths Used: {', '.join(length_names)}\n"
                    result_text += f"Length Values: {'; '.join([f'{name} = {value:.5f}' for name, value in zip(length_names, length_values)])}\n"
                    result_text += "-" * 50 + "\n"
                    
                    # Print the result in the console for visibility
                    print(f"\nFormula Value: {formula_key}")
                    print(result_text)

                    # Check if the formula is already in the file
                    if not self.is_formula_in_file(formula):
                        # Save to file
                        with open(fname, "a") as f:
                            f.write(result_text)
                        
                        # Add the formula to the used formulas set
                        used_formulas.add(formula_key)
                    break  # Continue the loop without returning to keep brute-forcing

    def is_formula_in_file(self, formula):
        """
        Check if the formula is already present in the file.
        """
        if not os.path.exists(fname):
            return False  # File does not exist, so no formulas are saved

        with open(fname, "r") as file:
            content = file.read()
        
        # Check if the formula already exists in the file content
        if f"Formula Used: {formula}" in content:
            return True
        
        return False


def main():
    while True:  # Keep running the program until manually stopped
        # User inputs for base length and height
        base_length_north = float(input("Enter the base length (North side): "))
        base_length_east = float(input("Enter the base length (East side): "))
        height = float(input("Enter the height of the pyramid: "))

        # Create pyramid object
        pyramid = Pyramid(base_length_north, base_length_east, height)
        
        # Run the comparison and keep printing results
        pyramid.compare_constants(threshold=0.00001)

if __name__ == "__main__":
    main()
