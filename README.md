# Pyramid Mathematics and Geometry Calculator


This repository contains tools for calculating pyramid dimensions, randomly generating formulas using base lengths, height, and other geometric properties, and comparing these results against known constants like π (Pi). Both **Python** and **Go** implementations are available.

# Table of Contents

1. [Introduction](#pyramid-mathematics-and-geometry-calculator)
2. [Directory Structure](#directory-structure)
3. [Project Structure](#project-structure)
4. [Key Parameters](#key-parameters)
5. [Special Calculations](#special-calculations)
6. [Speed of Light Approximation](#speed-of-light-approximation)
7. [Python Tools](#python-tools)
   - [Key Features](#key-features)
   - [How to Use](#how-to-use)
   - [Example Output](#example-output)
8. [cs.py - Supporting Constants](#cs-py---supporting-constants-for-pyramid-analysis)
   - [Key Constants](#key-constants)
   - [Use in pyramid_analysis.py](#use-in-pyramid_analysispy)
9. [pyramid_viz.py](#pyramid_vizpy---visualization-and-golden-ratio-spiral)
   - [Pyramid Calculator](#pyramid-calculator)
10. [Go Tool](#go-tool)
    - [Features](#features)
    - [Usage](#usage)
    - [Arguments](#arguments)
    - [Output](#output)
    - [How It Works](#how-it-works)
11. [Analysis](#analysis)
    - [Comparison of Ancient Egyptian Pyramids](#comparison-of-ancient-egyptian-pyramids-measurements-with-pi-and-golden-ratio)
    - [My Best Pyramids with Pi and Golden Ratio](#My-best-pyramids-with-pi-and-golden-ratio)
    - [Analysis of Ancient Egyptian Pyramids and Pi/Golden Ratio Relationships](#analysis-of-ancient-egyptian-pyramids-and-pigolden-ratio-relationships)
12. [Research Contact](#research-by-ishan-oshada)
13. [PyramidMath - A Python Package for Pyramid Geometry and Mathematical Constants](#pyramidmath---a-python-package-for-pyramid-geometry-and-mathematical-constants)
14. [Sinhala](#sinhala)
14. [License](#license)



### Directory Structure:

```python
geometry-pyramid-analysis/
├── README.md
├── data/
├── pyramid.py
├── pyramid_analysis.py
├── requirements.txt
├── cs.py
├── img/
├── pyramid_analysis.go
├── egypt.py
├── my_pyramids.py
└── pyramid_viz.py
```



### Project Structure

- **pyramid.py**: Contains essential functions and classes for working with pyramid properties.
- **pyramid_analysis.py**: Performs detailed analysis of pyramid geometries, such as calculating base areas, heights, and other geometric properties.
- **pyramid_analysis.go**: Go-based implementation of pyramid analysis, providing an alternative backend for geometric computations.
- **cs.py**: Constants file containing important mathematical and geometric constants used throughout the project.
- **pyramid_viz.py**: Visualization module using graphical representations to depict pyramids and their properties.
- **my_pyramids.py**: My pyramid calculations, including Pi and Golden Ratio differences.
- **egypt.py**: All Egyptian pyramids, Pi, and Golden Ratio differences calculations.
- **data/**: Directory for storing data files, such as geometric values or test datasets.
- **img/**: Directory for storing images used for visualizations.
- **requirements.txt**: File listing Python dependencies required for the project.

![img5](/img/pyr_giza.png)

## Key Parameters
- **Base Lengths**: North and East
- **Height**
- **Slope Angle**
- **Apothem**: Calculated using the Pythagorean theorem.
- **Edge**: Distance from peak to a corner of the base.
- **Diagonal** (same as **CG**): Calculated using  sqrt{2Base Length^2}

## Special Calculations

![sp](/img/s1.png)

![sp2](/img/s2.png)
This formula demonstrates how geometric constants can be linked to fundamental physics constants. The data in `data/light_of_speed.txt` played a key role in my discovery of this relationship, and the formula was devised as part of the pyramid geometry analysis in this project.

**Known Values**:
- Height: 515.28 ft
- Base Length North: 809.4 ft
- Base Length East: 809.4 ft
- Apothem: 655.20651 ft
- Diagonal Base: 1144.66446 ft
- Half Base: 404.7 ft

The calculated value is:

$$ \text{Calculated Speed of Light} = 2.997884 \, \text{ft/s} $$

**Actual Speed of Light**:

$$ \text{Actual Speed of Light} = 2.997924 \times 10^8 \, \text{m/s} $$

**Difference**:

$$ \text{Difference} = 0.000040 \, \text{ft/s} $$

This difference is small enough to indicate that the pyramid's dimensions, through this calculation, yield a close approximation to the actual speed of light.


---


## Python Tools

The Python tool uses random operations on pyramid dimensions (base lengths, height, etc.) and compares the calculated values with constants like π. It continuously runs until it finds a low difference between the calculated and actual constant values. The results are logged in a text file (`pyramid_results_n.txt`).

### Key Features:
- **Random Calculations**: Randomly combines pyramid lengths and applies random mathematical operations.
- **Comparison with Constants**: Compares the calculated results with constants such as π and logs any low differences.
- **Safety Checks**: Functions like `safe_tan`, `safe_cos`, `safe_sin`, and others ensure valid mathematical operations without errors.
- **Output to File**: Results with low differences are saved to a text file for future reference.

### How to Use:

1. Clone the repository:
    ```bash
    git clone https://github.com/ishanoshada/geometry-pyramid-analyzer.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    

3. Run the Python script:
    ```bash
    python pyramid_analysis.py
    ```
    ```bash
    python pyramid_analysis.py output.txt
    ```

4. The script will prompt you for base lengths and height, and it will start calculating and comparing values.

5. Results with low differences will be printed to the console and saved to the file `pyramid_results_n.txt` | `output.txt` .



## cs.py - Supporting Constants for Pyramid Analysis

The `cs.py` module provides essential constants that are utilized in the `pyramid_analysis.py` calculations. These constants are critical for performing various mathematical and geometric operations related to pyramid structures. Below is a summary of the available constants in `cs.py`:

### Key Constants:
- **Pi (`pi`)**: The constant π used in many geometric formulas.
- **Square Roots**: The module contains square roots for small integers like 2, 3, 5, 7, and others, which are often used for geometric and trigonometric calculations.
- **Cube and Higher Roots**: Cube roots for large numbers such as 1,000,000 and 1,250,000, along with higher-order roots for composite numbers.
- **Irrational and Transcendental Constants**: Includes mathematical constants like the square root of 3/2 and 5/2, as well as logarithmic constants.
- **Universal Constants**: Constants like the speed of light, gravitational constant, and Planck's constant are included for more advanced physics-related calculations.

### Use in `pyramid_analysis.py`
The constants provided in `cs.py` are imported into `pyramid_analysis.py` and used to calculate various properties of a pyramid, such as:
- Slope angle
- Base lengths
- Heights and apothems
- Ratios involving the Golden Ratio, Tribonacci constant, and square roots of small integers.

Example usage in `pyramid_analysis.py`:
```python
...........
from cs import constants
..........

```

This integration ensures that your pyramid analysis tool can work with predefined mathematical constants, allowing for more accurate and efficient computations when dealing with pyramid geometries.


### Example Output:

```
Formula Value: base_length_north + base_length_east / height => base_length_north, base_length_east, height
Low Difference Found:
Constant: pi
Calculated Value: 3.141593
Actual Value: 3.141593
Difference: 0.000000
Formula Used: base_length_north + base_length_east / height
Lengths Used: base_length_north, base_length_east, height
--------------------------------------------------

Low Difference Found:
Constant: .......
Calculated Value: 1.618089
Actual Value: ......
Difference: 0.000055
Formula Used: log(log(apothem / base_length_north + base_length_east - edge))
Lengths Used: apothem, base_length_north, base_length_east, edge, diagonal_base, half_base
Length Values: apothem = 655.20651; base_length_north = 809.40000; base_length_east = 809.40000; edge = 655.20651; diagonal_base = 1144.66446; half_base = 404.70000
--------------------------------------------------

Low Difference Found:
Constant: power(2,2/pi)
Calculated Value: 1.554665
Actual Value: 1.554682
Difference: 0.000017
Formula Used: log(apothem / base_length_east) - height + diagonal_base / half_base
Lengths Used: apothem, base_length_east, base_length_north, height, diagonal_base, half_base
Length Values: apothem = 655.20651; base_length_east = 809.40000; base_length_north = 809.40000; height = 515.28000; diagonal_base = 1144.66446; half_base = 404.70000
--------------------------------------------------

```




## Usage:
Run the `pyramid.py` file from your terminal or command prompt.

```bash
python pyramid.py
```

You will be prompted with two options:
1. **Enter angle to predict dimensions**:
    - You can provide a slope angle and either the height or base length to predict the other parameters.
    - Select the desired constraint (height or base length).

2. **Enter known dimensions**:
    - Manually input base lengths (north/east) and height to perform calculations.

The tool will then output:
- The pyramid's calculated dimensions.
- Comparisons with mathematical constants like π, φ (Golden Ratio), Tribonacci, √5, etc.
- A spiral visualization generated from the Golden Ratio.

## Example Output:
### Example 1: Entering slope angle to predict dimensions
```
Pyramid Calculator
1. Enter angle to predict dimensions
2. Enter known dimensions
Choose option (1 or 2): 1
Enter slope angle in degrees: 51
Select constraint:
1. Specify desired height
2. Specify desired base length
3. Use default height (481 feet)
Choose constraint (1, 2, or 3): 1
Enter desired height in feet: 500

Detailed Analysis of Pyramid with 51° slope:

Measurements and Calculated Values:
North Base Length: 640.27 ft
Eastern Base Length: 640.27 ft
Height: 500.00 ft

Apothem = 640.36122669
Diagonal = 904.28967846
Edge Length: 640.27 ft

Special Calculations vs Mathematical Constants:
(North base + Eastern base) / Height = 2.56109075
Actual π value = 3.14159265
Difference from π = 0.58050189
My Method 1: (sin(North base / (Eastern base / 2) / Height) * North base) = 3.14160107 , diff = 0.58050842 
My Method 2: (calculate_apothem()-calculate_edge()+base_length_north/self.height*base_length_east/half_base) = 3.14160107 , diff = 0.58050842

Edge / (Base length / 2) = 1.99999999
Actual φ (Golden Ratio) = 1.61803399
Difference from φ = 0.38196600

Apothem / Height = 1.28072245
Actual √φ = 1.27201965
Difference from √φ = 0.00870280

Pyramid Slope Angle: 51.000000 degrees

Diagonal base / Base Length = 1.41421356
Difference from √2 = 0.00000000

Calculated Tribonacci Constant = 1.83928676
Actual Tribonacci Constant = 1.8393
Difference from Tribonacci Constant = 0.00000000

(Base Length + Apothem) / Apothem = 1.99856565
Actual √5 = 2.23606798
Difference from √5 = 0.23750233

(Height + CG + CG) / (North Base + Eastern Base) = 1.73205080
Actual √3 = 1.73205081
Difference from √3 = 0.00000001

Apothem / (Apothem + Half Base Length) = 0.81812425
Actual φ - 1 = 0.61803399
Difference from φ - 1 = 0.20009026

Spiral Visualizing Golden Ratio...

```

### Example 2: Entering known dimensions
```
Pyramid Calculator
1. Enter angle to predict dimensions
2. Enter known dimensions
Choose option (1 or 2): 2
Enter base length north in feet: 640
Enter base length east in feet: 640
Enter height in feet: 500

Detailed Analysis of Custom Pyramid:

Measurements and Calculated Values:
North Base Length: 640.00 ft
Eastern Base Length: 640.00 ft
Height: 500.00 ft

Apothem = 640.36122669
Diagonal = 904.28967846
Edge Length: 640.00 ft

Special Calculations vs Mathematical Constants:
(North base + Eastern base) / Height = 2.56109075
Actual π value = 3.14159265
Difference from π = 0.58050189
My Method 1: (sin(North base / (Eastern base / 2) / Height) * North base) = 3.14160107 , diff = 0.58050842 
My Method 2: (calculate_apothem()-calculate_edge()+base_length_north/self.height*base_length_east/half_base) = 3.14160107 , diff = 0.58050842

Edge / (Base length / 2) = 1.99999999
Actual φ (Golden Ratio) = 1.61803399
Difference from φ = 0.38196600

Apothem / Height = 1.28072245
Actual √φ = 1.27201965


Difference from √φ = 0.00870280

Pyramid Slope Angle: 51.000000 degrees

Diagonal base / Base Length = 1.41421356
Difference from √2 = 0.00000000

Calculated Tribonacci Constant = 1.83928676
Actual Tribonacci Constant = 1.8393
Difference from Tribonacci Constant = 0.00000000

(Base Length + Apothem) / Apothem = 1.99856565
Actual √5 = 2.23606798
Difference from √5 = 0.23750233

(Height + CG + CG) / (North Base + Eastern Base) = 1.73205080
Actual √3 = 1.73205081
Difference from √3 = 0.00000001

Apothem / (Apothem + Half Base Length) = 0.81812425
Actual φ - 1 = 0.61803399
Difference from φ - 1 = 0.20009026
```
Here's an updated section for the `README.md` with the usage details for `pyramid_viz.py` and the pyramid calculator example:

---

### `pyramid_viz.py` - Visualization and Golden Ratio Spiral

The `pyramid_viz.py` script allows you to visualize pyramids in 2D and also draws a pyramid based on the golden ratio value, which relates to the golden spiral. You can use it to explore the geometric properties of pyramids, and the script can calculate values such as apothem, diagonal, and edge length. Additionally, it compares the calculated values to mathematical constants like Pi.

### Pyramid Calculator

This section lets you interact with the pyramid calculator. You can either input dimensions to predict the pyramid's properties or enter known dimensions for a detailed analysis.

#### Example of Usage:

1. **Enter angle to predict dimensions** or **Enter known dimensions**.
2. **Choose option (1 or 2)** to proceed.

**Example output:**

```bash
Pyramid Calculator
1. Enter angle to predict dimensions
2. Enter known dimensions
Choose option (1 or 2): 2
Enter base length north in feet: 809.4
Enter base length east in feet: 809.4
Enter height in feet: 515.28

Detailed Analysis of Custom Pyramid:

Measurements and Calculated Values:
North Base Length: 809.40 ft
Eastern Base Length: 809.40 ft
Height: 515.28 ft

Apothem = 655.20650821
Diagonal = 1144.66445738
Edge Length: 655.21 ft

Special Calculations vs Mathematical Constants:
(North base + Eastern base) / Height = 3.14159292
Actual π value = 3.14159265
Difference from π = 0.00000027
My Method 1: (sin(North base / (Eastern base / 2) / Height) * North base) = 3.1415850322659074
...
```

![img2](/img/pyramid.png)
![img3](/img/spiral.png)

---


## Go Tool

The Go implementation performs similar calculations but in a statically typed language. It allows for efficient, concurrent processing and can be used for large-scale computations or when performance is a critical factor.

### Key Features:
- **Pyramid Calculations**: Similar to the Python tool, Go performs random calculations with the base lengths, height, and other pyramid parameters.
- **Comparison with Constants**: Finds and reports low differences between calculated values and known constants like π.
- **Efficient and Concurrent**: Can be extended to handle concurrent calculations and large datasets.

### How to Use:

2. Build the Go tool:
    ```bash
    go build pyramid_analysis.go
    ```

3. Run the Go tool:
    ```bash
    ./pyramid_analysis
    ```

4. Similar to the Python version, the Go tool will prompt you for base lengths and height and begin comparing results with constants.

## Features

- **Constant Approximation**: Detect configurations approximating π or Φ with high precision.
- **Customizable Ranges**: Specify base length and height ranges for analysis.
- **Step Control**: Fine-tune the granularity of the analysis by adjusting step sizes.
- **Output File**: Save results in a neatly formatted, sorted text file.
- **Graceful Exit**: Responds to termination signals, ensuring clean exits.

---

## Usage

Run the application using command-line flags to configure the analysis.

### Syntax

```bash
go run pyramid_analysis.go --base=<base_range> --height=<height_range> --output=<output_file> --basestep=<base_step> --heightstep=<height_step>
```

### Arguments

| Flag           | Description                                             | Default       |
|----------------|---------------------------------------------------------|---------------|
| `--base`       | Base length range in the format `start-end`.            | `100-200`     |
| `--height`     | Height range in the format `start-end`.                 | `100-200`     |
| `--output`     | File to save the analysis results.                      | `data.txt`    |
| `--basestep`   | Increment step for the base length during analysis.     | `1`           |
| `--heightstep` | Increment step for the height during analysis.          | `1`           |

### Example

To analyze a base range of `150-160` and height range of `130-140` with step sizes of `0.5` for both dimensions, and save results to `results.txt`:

```bash
go run pyramid_analysis.go --base=150-160 --height=130-140 --output=results.txt --basestep=0.5 --heightstep=0.5
```

---

## Output

The program outputs a file (e.g., `results.txt`) containing a table of results:

```
Constant Name   Base Length     Height          Calculated Pi        Pi Difference        Calculated GR        GR Difference       
π               756.0400        481.3100        3.1415927365         0.0000000829         1.6189931602         0.0009591714        
π               755.9300        481.2400        3.1415925526         0.0000001010         1.6189932188         0.0009592301        
π               756.1500        481.3800        3.1415929204         0.0000002668         1.6189931016         0.0009591128        
π               755.8200        481.1700        3.1415923686         0.0000002850         1.6189932774         0.0009592887        
π               756.2600        481.4500        3.1415931042         0.0000004506         1.6189930430         0.0009590542        
π               755.7100        481.1000        3.1415921846         0.0000004690         1.6189933361         0.0009593473        
π               756.3700        481.5200        3.1415932879         0.0000006343         1.6189929844         0.0009589957        
π               755.6000        481.0300        3.1415920005         0.0000006531         1.6189933948         0.0009594060        
π               756.4800        481.5900        3.1415934716         0.0000008180         1.6189929259         0.0009589371        
π               755.4900        480.9600        3.1415918164         0.0000008372         1.6189934535         0.0009594647        
π               756.5900        481.6600        3.1415936553         0.0000010017         1.6189928673         0.0009588786        
π               755.3800        480.8900        3.1415916322         0.0000010214         1.6189935122         0.0009595234        
π               756.7000        481.7300        3.1415938389         0.0000011853         1.6189928088         0.0009588201        
π               755.2700        480.8200        3.1415914479         0.0000012056         1.6189935709         0.0009595821        
π               756.8100        481.8000        3.1415940224         0.0000013688         1.6189927503         0.0009587616        
π               755.1600        480.7500        3.1415912637         0.0000013899         1.6189936296         0.0009596409        
π               756.9200        481.8700        3.1415942059         0.0000015523         1.6189926918         0.0009587031        
π               755.0500        480.6800        3.1415910793         0.0000015743         1.6189936884         0.0009596996        
π               757.0300        481.9400        3.1415943893         0.0000017358         1.6189926334         0.0009586446        
π               754.9400        480.6100        3.1415908949         0.0000017587         1.6189937472         0.0009597584        
π               757.1400        482.0100        3.1415945727         0.0000019191         1.6189925749         0.0009585862        
π               754.8300        480.5400        3.1415907105         0.0000019431         1.6189938059         0.0009598172        
π               757.2500        482.0800        3.1415947561         0.0000021025         1.6189925165         0.0009585277        
π               754.7200        480.4700        3.1415905259         0.0000021276         1.6189938648         0.0009598760        
π               757.3600        482.1500        3.1415949393         0.0000022857         1.6189924581         0.0009584693        
π               754.6100        480.4000        3.1415903414         0.0000023122         1.6189939236         0.0009599348    
Golden Ratio    756.1500        481.2100        3.1427027701         0.0011101165         1.6186395060         0.0006055173        
Golden Ratio    756.2600        481.2800        3.1427027926         0.0011101390         1.6186394989         0.0006055101        
π               757.6100        482.4800        3.1404825070         0.0011101465         1.6193471745         0.0013131858        
Golden Ratio    756.3700        481.3500        3.1427028150         0.0011101614         1.6186394917         0.0006055030        
π               755.7100        481.2700        3.1404824735         0.0011101801         1.6193471852         0.0013131965        
Golden Ratio    756.4800        481.4200        3.1427028374         0.0011101838         1.6186394846         0.0006054958        
Golden Ratio    756.5900        481.4900        3.1427028599         0.0011102063         1.6186394774         0.0006054887        
Golden Ratio    756.7000        481.5600        3.1427028823         0.0011102287         1.6186394703         0.0006054816        
Golden Ratio    756.8100        481.6300        3.1427029047         0.0011102511         1.6186394632         0.0006054744        
Golden Ratio    756.9200        481.7000        3.1427029271         0.0011102735         1.6186394560         0.0006054673        
Golden Ratio    757.0300        481.7700        3.1427029495         0.0011102960         1.6186394489         0.0006054601        
Golden Ratio    757.1400        481.8400        3.1427029719         0.0011103184         1.6186394418         0.0006054530        
Golden Ratio    757.2500        481.9100        3.1427029943         0.0011103407         1.6186394346         0.0006054459        
Golden Ratio    757.3600        481.9800        3.1427030167         0.0011103631         1.6186394275         0.0006054387        
Golden Ratio    757.4700        482.0500        3.1427030391         0.0011103855         1.6186394204         0.0006054316        
Golden Ratio    757.5800        482.1200        3.1427030615         0.0011104079         1.6186394132         0.0006054245        
Golden Ratio    757.6900        482.1900        3.1427030838         0.0011104303         1.6186394061         0.0006054174        
Golden Ratio    757.8000        482.2600        3.1427031062         0.0011104526         1.6186393990         0.0006054103        
Golden Ratio    757.9100        482.3300        3.1427031286         0.0011104750         1.6186393919         0.0006054031        
π               757.5000        482.4100        3.1404821625         0.0011104911         1.6193472844         0.0013132957        
π               755.6000        481.2000        3.1404821280         0.0011105256         1.6193472954         0.0013133067        
π               757.3900        482.3400        3.1404818178         0.0011108358         1.6193473944         0.0013134056        
```

---

## How It Works

1. **Iterative Analysis**: 
   - For each combination of base length and height within the specified ranges, the program calculates:
     - Approximation of **π**: `2 × base length / height`
     - Approximation of **Φ**: Ratio of pyramid's edge length to half its base.
   
2. **Constant Crossing Detection**:
   - Identifies dimensions where the calculated constants are within a small difference (`<0.01`) of the actual values.

3. **Result Sorting**:
   - Prioritizes configurations with the smallest difference for **π** and **Φ**.

4. **Signal Handling**:
   - Ensures that partial progress is not lost if the program is interrupted.

---
<br>

# Analysis

## Comparison of Ancient Egyptian Pyramids' Measurements with Pi and Golden Ratio


| Pyramid | Height (ft) | Base Length (ft)) | Pi Comparison | Pi Difference | Golden Ratio Comparison | Golden Ratio Difference |
|---------|------------|-----------------|---------------|---------------|------------------------|-------------------------|
| Great Pyramid (Pyramid of Khufu) | 480.971144 | 755.905536 | 3.1432 | 0.001654277 | 2.0000 | 0.381966011 |
| Pyramid of Khafre | 470.80054 | 706.364852 | 3.0007 | 0.140895789 | 2.0000 | 0.381966011 |
| Pyramid of Menkaure | 213.2546 | 335.301848 | 3.1446 | 0.003022731 | 2.0000 | 0.381966011 |
| Pyramid of Djoser (Step Pyramid) | 203.41208 | 357.61156 | 3.5161 | 0.374536379 | 2.0000 | 0.381966011 |
| Pyramid of Sneferu (Bent Pyramid) | 344.4882 | 618.766424 | 3.5924 | 0.450788299 | 2.0000 | 0.381966011 |
| Pyramid of Sneferu (Red Pyramid) | 341.20736 | 721.7848 | 4.2308 | 1.089176577 | 2.0000 | 0.381966011 |
| Pyramid of Teti | 170.60368 | 255.90552 | 3.0000 | 0.141592654 | 2.0000 | 0.381966011 |
| Pyramid of Amenemhat II | 180.4462 | 344.4882 | 3.8182 | 0.676589165 | 2.0000 | 0.381966011 |
| Pyramid of Unas | 141.07612 | 221.4567 | 3.1395 | 0.002057770 | 2.0000 | 0.381966011 |
| Pyramid of Userkaf | 160.76116 | 237.8609 | 2.9592 | 0.182408980 | 2.0000 | 0.381966011 |
| Pyramid of Sahure | 154.19948 | 255.90552 | 3.3191 | 0.177556283 | 2.0000 | 0.381966011 |
| Pyramid of Neferirkare | 196.8504 | 344.4882 | 3.5000 | 0.358407346 | 2.0000 | 0.381966011 |
| Pyramid of Niuserre | 164.042 | 344.4882 | 4.2000 | 1.058407346 | 2.0000 | 0.381966011 |
| Pyramid of Amenemhat I | 164.042 | 328.084 | 4.0000 | 0.858407346 | 2.0000 | 0.381966011 |
| Pyramid of Amenemhat III | 173.88452 | 301.83728 | 3.4717 | 0.330105460 | 2.0000 | 0.381966011 |
| Pyramid of Senusret II | 157.48032 | 255.90552 | 3.2500 | 0.108407346 | 2.0000 | 0.381966011 |
| Pyramid of Pepi I | 172.2441 | 257.54594 | 2.9905 | 0.151116463 | 2.0000 | 0.381966011 |
| Pyramid of Merenre | 164.042 | 246.063 | 3.0000 | 0.141592654 | 2.0000 | 0.381966011 |
| Pyramid of Pepi II | 170.60368 | 259.18636 | 3.0385 | 0.103131115 | 2.0000 | 0.381966011 |
| Pyramid of Khendjer | 121.39108 | 170.60368 | 2.8108 | 0.330781843 | 2.0000 | 0.381966011 |
| Pyramid of Ibi | 114.82939999999999 | 196.8504 | 3.4286 | 0.286978775 | 2.0000 | 0.381966011 |
| Pyramid of Qakare Ibi | 104.98688 | 180.4462 | 3.4375 | 0.295907346 | 2.0000 | 0.381966011 |
| Pyramid of Khui | 131.2336 | 203.41208 | 3.1000 | 0.041592654 | 2.0000 | 0.381966011 |
| Pyramid of Senusret III | 200.13124 | 344.4882 | 3.4426 | 0.301030297 | 2.0000 | 0.381966011 |
| Pyramid of Neferuptah | 114.82939999999999 | 147.6378 | 2.5714 | 0.570164082 | 2.0000 | 0.381966011 |
| Meidum Pyramid | 301.83728 | 472.44096 | 3.1304 | 0.011157871 | 2.0000 | 0.381966011 |
| Southern Pyramid of Mazghuna | 114.82939999999999 | 170.60368 | 2.9714 | 0.170164082 | 2.0000 | 0.381966011 |
| Northern Pyramid of Mazghuna | 104.98688 | 164.042 | 3.1250 | 0.016592654 | 2.0000 | 0.381966011 |
| Pyramid of Sekhemkhet | 147.6378 | 229.65879999999999 | 3.1111 | 0.030481542 | 2.0000 | 0.381966011 |
| Layer Pyramid | 141.07612 | 278.8714 | 3.9535 | 0.811895719 | 2.0000 | 0.381966011 |


![img4](/img/pyra_deta.png)

## My Best Pyramids with Pi and Golden Ratio

| Pyramid | Height (ft) | Base Length (ft) | Pi Comparison | Pi Difference | Golden Ratio Comparison | Golden Ratio Difference |
|---------|------------|-----------------|---------------|---------------|------------------------|-------------------------|
| my_pyramid1 | 515.28 | 809.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid2 | 524.32 | 823.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid3 | 506.24 | 795.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid4 | 533.36 | 837.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid5 | 542.4 | 852.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid6 | 551.44 | 866.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid7 | 497.2 | 781.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid8 | 560.48 | 880.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid9 | 569.52 | 894.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid10 | 578.56 | 908.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid11 | 488.16 | 766.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid12 | 587.6 | 923.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid13 | 596.64 | 937.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid14 | 605.68 | 951.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid15 | 614.72 | 965.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid16 | 479.12 | 752.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid17 | 623.76 | 979.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid18 | 632.8 | 994.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid19 | 470.08 | 738.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid20 | 461.04 | 724.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid21 | 452.0 | 710.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid22 | 442.96 | 695.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid23 | 433.92 | 681.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid24 | 424.88 | 667.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid25 | 415.84 | 653.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid26 | 406.8 | 639.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid27 | 397.76 | 624.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid28 | 388.72 | 610.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid29 | 126.56 | 198.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid30 | 135.6 | 213.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid31 | 144.64 | 227.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid32 | 153.68 | 241.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid33 | 162.72 | 255.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid34 | 117.52 | 184.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid35 | 379.68 | 596.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid36 | 108.48 | 170.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid37 | 171.76 | 269.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid38 | 370.64 | 582.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid39 | 99.44 | 156.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid40 | 180.8 | 284.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid41 | 361.6 | 568.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid42 | 90.4 | 142.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid43 | 189.84 | 298.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid44 | 352.56 | 553.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid45 | 198.88 | 312.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid46 | 343.52 | 539.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid47 | 207.92 | 326.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid48 | 216.96 | 340.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid49 | 334.48 | 525.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid50 | 226.0 | 355.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid51 | 325.44 | 511.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid52 | 235.04 | 369.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid53 | 316.4 | 497.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid54 | 307.36 | 482.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid55 | 298.32 | 468.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid56 | 289.28 | 454.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid57 | 244.08 | 383.4 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid58 | 280.24 | 440.2 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid59 | 271.2 | 426.0 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid60 | 253.12 | 397.6 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid61 | 262.16 | 411.8 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid62 | 481.31 | 756.04 | 3.1416 | 0.000000083 | 1.6190 | 0.000959171 |
| my_pyramid63 | 481.24 | 755.93 | 3.1416 | 0.000000101 | 1.6190 | 0.000959230 |
| my_pyramid64 | 481.38 | 756.15 | 3.1416 | 0.000000267 | 1.6190 | 0.000959113 |
| my_pyramid65 | 481.17 | 755.82 | 3.1416 | 0.000000285 | 1.6190 | 0.000959289 |
| my_pyramid66 | 481.45 | 756.26 | 3.1416 | 0.000000451 | 1.6190 | 0.000959054 |
| my_pyramid67 | 481.1 | 755.71 | 3.1416 | 0.000000469 | 1.6190 | 0.000959347 |
| my_pyramid68 | 481.52 | 756.37 | 3.1416 | 0.000000634 | 1.6190 | 0.000958996 |
| my_pyramid69 | 481.03 | 755.6 | 3.1416 | 0.000000653 | 1.6190 | 0.000959406 |
| my_pyramid70 | 481.59 | 756.48 | 3.1416 | 0.000000818 | 1.6190 | 0.000958937 |
| my_pyramid71 | 480.96 | 755.49 | 3.1416 | 0.000000837 | 1.6190 | 0.000959465 |
| my_pyramid72 | 549.08 | 863.32 | 3.1446 | 0.003012868 | 1.6180 | 0.000000003 |
| my_pyramid73 | 424.88 | 668.04 | 3.1446 | 0.003012882 | 1.6180 | 0.000000008 |
| my_pyramid74 | 496.8 | 781.12 | 3.1446 | 0.003012821 | 1.6180 | 0.000000011 |
| my_pyramid75 | 621.0 | 976.4 | 3.1446 | 0.003012821 | 1.6180 | 0.000000011 |
| my_pyramid76 | 124.2 | 195.28 | 3.1446 | 0.003012821 | 1.6180 | 0.000000011 |
| my_pyramid77 | 372.6 | 585.84 | 3.1446 | 0.003012821 | 1.6180 | 0.000000011 |
| my_pyramid78 | 248.4 | 390.56 | 3.1446 | 0.003012821 | 1.6180 | 0.000000011 |
| my_pyramid79 | 549.08 | 863.32 | 3.1446 | 0.003012868 | 1.6180 | 0.000000003 |
| my_pyramid80 | 424.88 | 668.04 | 3.1446 | 0.003012882 | 1.6180 | 0.000000008 |
| my_pyramid81 | 394.8 | 623.24 | 3.1572 | 0.015651521 | 1.6140 | 0.004000000 |
| my_pyramid82 | 575.36 | 904.64 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid83 | 431.52 | 678.48 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid84 | 143.84 | 226.16 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid85 | 359.6 | 565.4 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid86 | 215.76 | 339.24 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid87 | 287.68 | 452.32 | 3.1446 | 0.003012463 | 1.6180 | 0.000000125 |
| my_pyramid88 | 0.043 | 0.0676 | 3.1442 | 0.002593393 | 1.6182 | 0.000133413 |
| my_pyramid89 | 336.64 | 529.3 | 3.1446 | 0.003012860 | 1.6180 | 0.000000001 |
| my_pyramid90 | 491.89 | 773.4 | 3.1446 | 0.003012848 | 1.6180 | 0.000000003 |
| my_pyramid91 | 518.03 | 814.5 | 3.1446 | 0.003012871 | 1.6180 | 0.000000004 |
| my_pyramid92 | 181.39 | 285.2 | 3.1446 | 0.003012892 | 1.6180 | 0.000000011 |
| my_pyramid93 | 362.78 | 570.4 | 3.1446 | 0.003012892 | 1.6180 | 0.000000011 |
| my_pyramid94 | 544.17 | 855.6 | 3.1446 | 0.003012892 | 1.6180 | 0.000000011 |
| my_pyramid95 | 0.043 | 0.0676 | 3.1442 | 0.002593393 | 1.6182 | 0.000133413 |

## Analysis of Ancient Egyptian Pyramids and Pi/Golden Ratio Relationships

![img6](/img/py7.png)

### Observations

1. **Pi Comparison**:
   - The ratio between the base length and height of the Great Pyramid of Giza (Khufu) shows remarkable closeness to \(\pi\) (3.1432), with a minimal difference of 0.0017.
   - Many other pyramids, such as Menkaure (3.1446) and Unas (3.1395), have proportions close to \(\pi\), but others, like the Red Pyramid (4.2308), deviate significantly.
   - Pyramids such as Teti (3.0000) and Khendjer (2.8108) have ratios far removed from \(\pi\), indicating variability in the architectural intent or design constraints.

2. **Golden Ratio**:
   - All pyramids have a consistent golden ratio comparison difference of 0.3819, suggesting the golden ratio was not directly used in most ancient pyramid constructions.
   - This consistency in deviation hints that the golden ratio was likely coincidental rather than intentional in Egyptian pyramid designs.

3. **Deviation from Precision**:
   - Pyramids like Djoser (3.5161) and Amenemhat II (3.8182) exhibit large deviations from both \(\pi\) and the golden ratio, possibly due to their non-standard designs or structural limitations.
   - Earlier pyramids (e.g., Step Pyramid of Djoser) show less adherence to the mathematical proportions observed in later structures like the Great Pyramid.

4. **Custom Pyramids and Precision**:
   - In contrast to ancient pyramids, the "my_pyramid" series displays extreme precision with a pi ratio of 3.1416 and golden ratio of 1.6190, almost perfectly aligning with mathematical values. 
   - This level of precision is reflective of modern computational methods and could symbolize what ancient builders might have achieved with advanced tools and knowledge.

5. **Variation by Period**:
   - Old Kingdom pyramids (e.g., Khufu, Khafre) display closer adherence to \(\pi\) compared to Middle and Late Kingdom pyramids, which show greater deviations.
   - This suggests a potential decline in precision engineering or a shift in architectural priorities over time.

![img1](/img/pyr4.png)

### Key Findings
- The Great Pyramid remains the closest to \(\pi\), supporting theories of advanced mathematical understanding during its construction.
- The golden ratio does not appear to be a deliberate design element but may have emerged naturally in some cases due to structural aesthetics or practical constraints.
- Modern precise pyramids (e.g., "my_pyramid" series) highlight the limitations of ancient construction methods while showcasing the possibilities of intentional mathematical design.

### Implications
This analysis underscores the mathematical ingenuity of ancient Egyptian architects, particularly in the Great Pyramid. While other pyramids suggest varying levels of precision and intent, the diversity in designs reflects a blend of practical, aesthetic, and possibly symbolic considerations, rather than a universal application of mathematical constants like \(\pi\) or the golden ratio.

![img8](/img/pyr1.png)

# Research by Ishan Oshada  
Email: [ishan.kodithuwakku.offical@gmail.com](ishan.kodithuwakku.offical@gmail.com)



# PyramidMath - A Python Package for Pyramid Geometry and Mathematical Constants

**Overview**  
`pyramid_math` is a Python package designed for anyone interested in exploring the geometry of pyramids, specifically their relationship to mathematical constants such as Pi (\(\pi\)), the Golden Ratio (\(\phi\)), and the Tribonacci constant. The package provides tools for calculating key pyramid properties like the apothem, edge length, slope angle, and more, all while comparing these measurements to well-known mathematical constants.

This package offers a practical way to study ancient Egyptian pyramids, including the Great Pyramid of Giza, Pyramid of Khafre, and others, as well as custom pyramids. It also enables users to perform detailed analyses of these iconic structures and provides insight into how ancient engineers might have utilized mathematical concepts.

**Mathematical Significance**  
By using the package, users can calculate various pyramid properties and compare them with mathematical constants. This comparison may offer clues about ancient Egyptian understanding of geometry, mathematics, and proportions in architectural design.

---

### Features and Benefits

- **Geometrical Calculations**: Automatically calculates the apothem, edge length, and slope angle of a pyramid.
- **Comparison with Constants**: Compares various pyramid dimensions to mathematical constants like \(\pi\), \(\phi\), and the Tribonacci constant.
- **Predefined and Custom Pyramids**: Users can access predefined pyramids such as the Great Pyramid of Giza, or create their own custom pyramids by inputting measurements.
- **Educational Tool**: Great for students, researchers, and math enthusiasts interested in exploring the mathematical properties of pyramids.

---

### Installation

You can easily install `pyramid_math` via `pip` from PyPI:

```bash
pip install pyramid_math
```

Or you can visit the GitHub repository to explore the source code and contribute to the project:

[GitHub Repository - Pyramid Math](https://github.com/Ishanoshada/Pyramid-Math/)

---

### Enhanced Usage Examples

Below are enhanced descriptions of some of the features of the package, which include examples of how to use the package for detailed analyses:

1. **Predefined Pyramid Example**:
   - This is useful for those who want to explore the properties of famous pyramids, such as the Great Pyramid of Giza. When you perform a detailed analysis on a predefined pyramid, it automatically compares the pyramid’s measurements with the values of \(\pi\) and \(\phi\), offering insight into ancient Egyptian construction techniques and their possible use of these constants.

   ```python
   # Load the Great Pyramid of Giza from the predefined database
   giza = Pyramid.from_database("great_pyramid_giza")

   # Perform detailed analysis
   giza.detailed_analysis(json=False)
   ```

2. **Custom Pyramid Example**:
   - This allows you to input any pyramid’s dimensions and run the package’s special calculations, providing detailed insights into how the pyramid compares to known mathematical constants.

   ```python
   # Create a custom pyramid with specified measurements (base lengths and height)
   pyramid = Pyramid("Test Pyramid", 100, 100, 50)

   # Perform special calculations on the custom pyramid
   special_calcs = pyramid.perform_special_calculations()
   print(special_calcs)
   ```

3. **Mathematical Constants and Comparisons**:
   - The most exciting aspect of this package is the ability to compare pyramid measurements with well-known mathematical constants, including:
     - **π (Pi)**: The ratio of the perimeter to the height.
     - **φ (Golden Ratio)**: The ratio of the edge length to half the base length.
     - **Tribonacci Constant**: A constant derived from the geometry of the pyramid.
     - **√5, √3**: Square roots of well-known constants compared with pyramid measurements.

---

### Detailed Output Example:

The detailed analysis output can help you compare various calculated and theoretical constants:

```bash
Detailed Analysis of Great Pyramid of Giza:
Measurements and Calculated Values:
North Base Length: 756.00 ft
Eastern Base Length: 756.00 ft
Height: 481.00 ft

Special Calculations vs Mathematical Constants:
(North base + Eastern base) / Height = 3.1454
Actual π value = 3.1416
Difference from π = 0.0038

Edge / (Base length / 2) = 1.6180
Actual φ (Golden Ratio) = 1.6180
Difference from φ = 0.0000

Apothem / Height = 0.7273
Actual √φ = 0.8510
Difference from √φ = 0.1237

Pyramid Slope Angle: 51.84 degrees

calculate_diagonal (CG) / Base Length = 0.9220
Difference from √2 = 0.0214

Calculated Tribonacci Constant = 1.8393
Actual Tribonacci Constant = 1.8393
Difference from Tribonacci Constant = 0.0000

(Base Length + Apothem) / Apothem = 2.6180
Actual √5 = 2.2361
Difference from √5 = 0.3819
```

This analysis not only compares dimensions but also highlights the closeness to the constants, revealing how precisely the pyramids' proportions match certain mathematical relationships.

---

## Sinhala

For a detailed explanation of the pyramid analysis in **Sinhala**, you can read the blog post here:

[Read the blog in Sinhala: Pyramid Analysis](https://ishan-oshada.vercel.app/post/Pyramid-Analysis-si/)



## License

This repository is licensed under the MIT License. See `LICENSE` for more information.


