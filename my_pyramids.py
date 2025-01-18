
# ===========================================================
# Research by Ishan Oshada
# Email: ishan.kodithuwakku.offical@gmail.com
# ===========================================================



import math

def read_pyramid_data(file_path):
    pyramids_data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if i == 0:  # Skip header
            continue
        parts = line.split()
        
        pyramid_key = f"my_pyramid{i}"
        
        # Extract values from the current line
    
        base_length = float(parts[1])
       
        height = float(parts[2])
        
        # Calculate the edge length using the Pythagorean theorem
        edge = math.sqrt((base_length / 2) ** 2 + height ** 2)
        
        # Assuming the values are the same for pi and GR difference
        pyramids_data[pyramid_key] = {
            "height": height,
            "north_base_length": base_length,
            "east_base_length": base_length,  # Assuming square base
            "edge": edge,
            
        }
    
    return pyramids_data

# Example usage
pyramids_data = read_pyramid_data('data/best.txt')
#print(pyramids_data)




import math

# Constants for comparisons
pi = math.pi
phi = (1 + math.sqrt(5)) / 2
# Updated function to calculate the comparisons with correct formulas
def calculate_comparisons(pyramids_data):
    results = []
    for pyramid, data in pyramids_data.items():
        # Pi comparison
        pi_value = (data["north_base_length"] + data["east_base_length"]) / data["height"]
        pi_diff = abs(pi_value - pi)
        
        # Golden Ratio comparison
        half_base = data["north_base_length"] / 2
        golden_ratio_value = data["edge"] / half_base
        golden_ratio_diff = abs(golden_ratio_value - phi)
        
        results.append({
            "Pyramid": pyramid,
            "Height (m)": data["height"],
            "Base Length (m)": data["north_base_length"],  # Using north base length as representative
            "Pi Comparison": pi_value,
            "Pi Difference": pi_diff,
            "Golden Ratio Comparison": golden_ratio_value,
            "Golden Ratio Difference": golden_ratio_diff
        })
    return results

# Recalculate results with updated formulas
comparisons = calculate_comparisons(pyramids_data)

# Creating a markdown table format
markdown_table = "| Pyramid | Height (m) | Base Length (m) | Pi Comparison | Pi Difference | Golden Ratio Comparison | Golden Ratio Difference |\n"
markdown_table += "|---------|------------|-----------------|---------------|---------------|------------------------|-------------------------|\n"

for result in comparisons:
    markdown_table += f"| {result['Pyramid']} | {result['Height (m)']} | {result['Base Length (m)']} | {result['Pi Comparison']:.4f} | {result['Pi Difference']:.9f} | {result['Golden Ratio Comparison']:.4f} | {result['Golden Ratio Difference']:.9f} |\n"

#markdown_table
print(markdown_table)


# Sort pyramids data by Pi Difference and Golden Ratio Difference in ascending order
sorted_comparisons = sorted(comparisons, key=lambda x: (x['Pi Difference'], x['Golden Ratio Difference']))

# Extracting the sorted result in dictionary format
sorted_comparisons_dict = [
    {
        "Pyramid": result['Pyramid'],
        "Height (m)": result['Height (m)'],
        "Base Length (m)": result['Base Length (m)'],
        "Pi Comparison": result['Pi Comparison'],
        "Pi Difference": result['Pi Difference'],
        "Golden Ratio Comparison": result['Golden Ratio Comparison'],
        "Golden Ratio Difference": result['Golden Ratio Difference']
    }
    for result in sorted_comparisons
]

#print(sorted_comparisons_dict)
