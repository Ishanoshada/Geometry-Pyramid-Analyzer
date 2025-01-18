
# ===========================================================
# Research by Ishan Oshada
# Email: ishan.kodithuwakku.offical@gmail.com
# ===========================================================


import numpy as np
import math
try:

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
except:
    print("Please install matplotlib and mpl_toolkits to run this script")
    exit()

def draw_spiral(phi):
    # Function to create radii using the golden ratio (Fibonacci-like sequence)
    def fibonacci_sequence(n):
        sequence = [1, 1]  # Start with the first two Fibonacci numbers
        for i in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])  # Sum of two previous numbers
        return sequence

    # Number of terms to generate (length of Fibonacci sequence)
    n = 200  # Increased number for more intricate design
    fibonacci_nums = fibonacci_sequence(n)

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(18, 18))

    # Starting coordinates for the first arc
    x, y = 0, 0

    # List to store the end points of each arc for connecting the dashed lines
    end_points = [(x, y)]

    # Increase the number of points per arc for smoother curves
    points_per_arc = 200

    # Draw arcs
    for i in range(1, n):
        # Create the arcs, moving in the directions of the Fibonacci sequence
        arc_start_angle = (i - 1) * 90  # Rotate 90 degrees for each Fibonacci number
        arc_end_angle = i * 90
        arc_radius = fibonacci_nums[i]  # Use Fibonacci number as the radius

        # Draw arc (quarter circle) with more points for smoother curves
        theta = np.linspace(np.radians(arc_start_angle), np.radians(arc_end_angle), points_per_arc)
        arc_x = x + arc_radius * np.cos(theta)
        arc_y = y + arc_radius * np.sin(theta)

        # Plot the arc
        ax.plot(arc_x, arc_y, color='blue')

        # Store the end point of the arc
        end_points.append((arc_x[-1], arc_y[-1]))

        # Update the starting point for the next arc
        x = arc_x[-1]
        y = arc_y[-1]

    # Connect the points with dashed lines and label only the last 4 Fibonacci numbers
    for i in range(1, len(end_points)):
        x1, y1 = end_points[i - 1]
        x2, y2 = end_points[i]

        # Calculate the length of the line segment
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        # Plot the dashed line
        ax.plot([x1, x2], [y1, y2], color='red', linestyle='--')

        # Only label the last 4 Fibonacci numbers
        if i >= n - 4:
            # Label the line with the Fibonacci number
            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2
            ax.text(midpoint_x, midpoint_y, f"Fib: {fibonacci_nums[i]}",
                    ha='center', va='center', fontsize=8, color='black',
                    bbox=dict(facecolor='white', alpha=0.8))

    # Set aspect ratio to equal to ensure the pattern is not distorted
    ax.set_aspect('equal')

    # Remove the axis for a cleaner look
    ax.axis('off')

    # Title for the plot
    plt.title(f"Fibonacci Spiral with Last 4 Fibonacci Numbers (phi = {phi})")

    # Show the plot
    plt.show()





class Pyramid:
    def __init__(self, name, base_length_north, base_length_east, height):
        """
        Initialize pyramid with base lengths and height in feet
        """
        self.name = name
        self.base_length_north = base_length_north
        self.base_length_east = base_length_east
        self.height = height
        self.diagonal_base = np.sqrt(base_length_north**2 + base_length_east**2)

    @classmethod
    def from_angle(cls, angle_degrees, desired_height=None, desired_base=None):
        """
        Create a pyramid instance from a given slope angle.
        Either provide desired_height or desired_base to calculate the other dimension.
        """
        angle_radians = np.radians(angle_degrees)

        if desired_height is not None:
            # Calculate base length from height and angle
            base_length = 2 * desired_height / np.tan(angle_radians)
            height = desired_height
        elif desired_base is not None:
            # Calculate height from base length and angle
            height = np.tan(angle_radians) * (desired_base / 2)
            base_length = desired_base
        else:
            # Default to height of 481.0 feet (similar to Great Pyramid)
            height = 481.0
            base_length = 2 * height / np.tan(angle_radians)

        return cls(
            name=f"Pyramid with {angle_degrees}° slope",
            base_length_north=base_length,
            base_length_east=base_length,  # Assuming square base
            height=height
        )

    def calculate_apothem(self):
        """
        Calculate the apothem using Pythagorean theorem
        """
        half_base = self.base_length_north / 2
        apothem = np.sqrt(self.height**2 + half_base**2)
        return apothem

    def calculate_edge(self):
        """
        Calculate the edge (distance from peak to a corner of the base) using Pythagorean theorem
        """
        half_base = self.base_length_north / 2
        edge = np.sqrt(self.height**2 + half_base**2)
        return edge

    def calculate_slope_angle(self):
        """
        Calculate the slope angle of the pyramid in degrees
        """
        half_base = self.base_length_north / 2
        # Angle between base and face (arctan of height/half_base)
        slope_angle = np.degrees(np.arctan(self.height / half_base))
        return slope_angle

    def perform_special_calculations(self):
        """
        Perform the specific calculations requested
        """
        half_base = self.base_length_east/2
        pivalue = (self.base_length_north + self.base_length_east) / self.height
        pivalue2  = math.sin(self.base_length_north/(self.base_length_east/2)/self.height)*self.base_length_north
        pivalue3 =  self.calculate_apothem()-self.calculate_edge()+self.base_length_north/self.height*self.base_length_east/half_base
        edge = self.calculate_edge()
        half_base = self.base_length_north / 2
        goldenratio = edge / half_base
        goldenratio2 = abs(math.sin(math.log(self.base_length_east))-edge)/half_base
        apothem = self.calculate_apothem()
        sqrt_goldenratio = apothem / self.height
        slope_angle = self.calculate_slope_angle()

        return {
            'pivalue': pivalue,
            'pivalue2':pivalue2,
            'pivalue3':pivalue3,
            'goldenratio': goldenratio,
            'goldenratio2': goldenratio,
            'sqrt_goldenratio': sqrt_goldenratio,
            'slope_angle': slope_angle
        }

    def calculate_diagonal(self):
        """
        Calculate the diagonal using the formula sqrt(2 * (Base length)^2)
        """
        diagonal = np.sqrt(2 * (self.base_length_north ** 2))
        return diagonal

    def calculate_CG(self):
        """
        Calculate the Center of Gravity (CG), using the diagonal for this pyramid.
        For simplicity, we will just use the diagonal calculated previously.
        """
        return self.calculate_diagonal()

    def compare_CG_base_length(self):
        """
        Compare CG to Base length and check the difference with √2
        """
        cg = self.calculate_CG()
        ratio = cg / self.base_length_north
        sqrt_2 = np.sqrt(2)
        difference = abs(ratio - sqrt_2)
        return ratio, difference

    def calculate_tribonacci_constant(self):
        """
        Calculate the Tribonacci constant using the formula:
        (CG + CG + Half Base Length) / (Slant Length + Base Length)
        """
        cg = self.calculate_CG()
        half_base = self.base_length_north / 2
        slant_length = self.calculate_apothem()  # Using apothem as slant length

        tribonacci_constant = (cg + cg + half_base) / (slant_length + self.base_length_north)
        return tribonacci_constant

    def compare_tribonacci_constant(self):
        """
        Compare the calculated Tribonacci constant to the known Tribonacci constant
        """
        tribonacci_constant = self.calculate_tribonacci_constant()
        tribonacci_actual = 1.839286755
        difference = abs(tribonacci_constant - tribonacci_actual)
        return tribonacci_constant, difference

    def compare_root_5(self):
        """
        Compare (Base Length + Apothem) / Apothem to √5
        """
        apothem = self.calculate_apothem()
        root_5 = np.sqrt(5)
        ratio = (self.base_length_north + apothem) / apothem
        difference = abs(ratio - root_5)
        return ratio, difference

    def compare_root_3(self):
        """
        Compare (Height + CG + CG) / (North Base + Eastern Base) to √3
        """
        cg = self.calculate_CG()
        root_3 = np.sqrt(3)
        ratio = (self.height + cg + cg) / (self.base_length_north + self.base_length_east)
        difference = abs(ratio - root_3)
        return ratio, difference

    def compare_golden_ratio_minus_1(self):
        """
        Compare (Apothem / (Apothem + Half Base Length)) to φ - 1
        """
        apothem = self.calculate_apothem()
        half_base = self.base_length_north / 2
        golden_ratio = (1 + np.sqrt(5)) / 2
        ratio = apothem / (apothem + half_base)
        difference = abs(ratio - (golden_ratio - 1))
        return ratio, difference

    def detailed_analysis(self):
        """
        Comprehensive analysis of the pyramid with constant comparisons
        """
        special_calcs = self.perform_special_calculations()

        print(f"\nDetailed Analysis of {self.name}:")
        print("\nMeasurements and Calculated Values:")
        print(f"North Base Length: {self.base_length_north:.2f} ft")
        print(f"Eastern Base Length: {self.base_length_east:.2f} ft")
        print(f"Height: {self.height:.2f} ft")
        apothem = self.calculate_apothem()
        print(f"\nApothem = {apothem:.8f}")
        print(f"Diagonal = {self.calculate_diagonal():.8f}")
        print(f"Edge Length: {self.calculate_edge():.2f} ft\n\n")
        print("\nSpecial Calculations vs Mathematical Constants:")

        print(f"(North base + Eastern base) / Height = {special_calcs['pivalue']:.8f}")
        print(f"Actual π value = {math.pi:.8f}")
        print(f"Difference from π = {abs(special_calcs['pivalue'] - math.pi):.8f}")
        print(f"My Method 1: (sin(North base / (Eastern base / 2) / Height) * North base) = {special_calcs['pivalue2']} , diff = {abs(special_calcs['pivalue2']-math.pi):.8f}")
        print(f"My Method 2: (calculate_apothem()-calculate_edge()+base_length_north/self.height*base_length_east/half_base) = {special_calcs['pivalue3']} , diff = {abs(special_calcs['pivalue3']-math.pi):.8f}")


        phi = (1 + np.sqrt(5)) / 2
        print(f"\nEdge / (Base length / 2) = {special_calcs['goldenratio']:.8f}")
        print(f"Actual φ (Golden Ratio) = {phi:.8f}")
        print(f"Difference from φ = {abs(special_calcs['goldenratio'] - phi):.8f}")
        print(f"MY Method 3: (abs(sin(log(base_length_east))-edge)/half_base) = {special_calcs['goldenratio2']}, diff = {abs(special_calcs['goldenratio2']-phi):.8f}")




        sqrt_phi = np.sqrt(phi)
        print(f"\nApothem / Height = {special_calcs['sqrt_goldenratio']:.8f}")
        print(f"Actual √φ = {sqrt_phi:.8f}")
        print(f"Difference from √φ = {abs(special_calcs['sqrt_goldenratio'] - sqrt_phi):.8f}")

        print(f"\nPyramid Slope Angle: {special_calcs['slope_angle']:.6f} degrees")

        cg_ratio, cg_difference = self.compare_CG_base_length()
        print(f"\nCenter of Gravity (CG) / Base Length = {cg_ratio:.8f}")
        print(f"Difference from √2 = {cg_difference:.4f}")

        tribonacci_constant, tribonacci_difference = self.compare_tribonacci_constant()
        print(f"\nCalculated Tribonacci Constant = {tribonacci_constant:.8f}")
        print(f"Actual Tribonacci Constant = 1.8393")
        print(f"Difference from Tribonacci Constant = {tribonacci_difference:.8f}")

        root_5_ratio, root_5_difference = self.compare_root_5()
        print(f"\n(Base Length + Apothem) / Apothem = {root_5_ratio:.8f}")
        print(f"Actual √5 = {np.sqrt(5):.8f}")
        print(f"Difference from √5 = {root_5_difference:.8f}")

        root_3_ratio, root_3_difference = self.compare_root_3()
        print(f"\n(Height + CG + CG) / (North Base + Eastern Base) = {root_3_ratio:.8f}")
        print(f"Actual √3 = {np.sqrt(3):.8f}")
        print(f"Difference from √3 = {root_3_difference:.8f}")

        golden_ratio_minus_1_ratio, golden_ratio_minus_1_difference = self.compare_golden_ratio_minus_1()
        print(f"\nApothem / (Apothem + Half Base Length) = {golden_ratio_minus_1_ratio:.8f}")
        print(f"Actual φ - 1 = {phi - 1:.8f}")
        print(f"Difference from φ - 1 = {golden_ratio_minus_1_difference:.8f}")

    def visualize(self):
        """
        Visualize the pyramid in 3D with tan or sand color
        """
        # Coordinates for the pyramid
        half_base = self.base_length_north / 2
        base_corners = [
            [-half_base, -half_base, 0],
            [half_base, -half_base, 0],
            [half_base, half_base, 0],
            [-half_base, half_base, 0]
        ]

        apex = [0, 0, self.height]

        # Define faces of the pyramid
        faces = [
            [base_corners[0], base_corners[1], apex],
            [base_corners[1], base_corners[2], apex],
            [base_corners[2], base_corners[3], apex],
            [base_corners[3], base_corners[0], apex],
            [base_corners[0], base_corners[1], base_corners[2], base_corners[3]]
        ]

        # Create 3D plot
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_box_aspect([1, 1, 1])

        # Plot the faces
        ax.add_collection3d(Poly3DCollection(faces, color='sandybrown', linewidths=1, edgecolors='brown', alpha=0.6))

        # Set the limits
        ax.set_xlim([-half_base, half_base])
        ax.set_ylim([-half_base, half_base])
        ax.set_zlim([0, self.height])

        # Labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f"{self.name} - 3D Visualization")

        plt.show()

    def spiral(self):
            special_calcs = self.perform_special_calculations()
            draw_spiral(special_calcs["goldenratio"])

def main():
    print("Pyramid Calculator")
    print("1. Enter angle to predict dimensions")
    print("2. Enter known dimensions")
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        angle = float(input("Enter slope angle in degrees: "))
        print("\nSelect constraint:")
        print("1. Specify desired height")
        print("2. Specify desired base length")
        print("3. Use default height (481 feet)")
        constraint = input("Choose constraint (1, 2, or 3): ")

        if constraint == "1":
            height = float(input("Enter desired height in feet: "))
            pyramid = Pyramid.from_angle(angle, desired_height=height)
        elif constraint == "2":
            base = float(input("Enter base length north or east in feet: "))
            pyramid = Pyramid.from_angle(angle, desired_base=base)
        else:
            pyramid = Pyramid.from_angle(angle)
    else:
        nbase = float(input("Enter base length north in feet: "))
        ebase = float(input("Enter base length east in feet: "))
        height = float(input("Enter height in feet: "))
        pyramid = Pyramid(
            name="Custom Pyramid",
            base_length_north=nbase,
            base_length_east=ebase,
            height=height
        )

    pyramid.detailed_analysis()
    pyramid.visualize()
    pyramid.spiral()

if __name__ == "__main__":
    main()
