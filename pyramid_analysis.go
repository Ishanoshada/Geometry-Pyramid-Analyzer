// ===========================================================
// Research by Ishan Oshada
// Email: ishan.kodithuwakku.offical@gmail.com
// ===========================================================

package main

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"os"
	"strings"
	"strconv"
	"log"
	"sort"
	"os/signal"
	"syscall"
)

// PyramidMetrics holds the calculated metrics for the pyramid
type PyramidMetrics struct {
	BaseLength      float64
	Height          float64
	CalculatedPi    float64
	PiDifference    float64
	CalculatedGR    float64
	GRDifference    float64
	ConstantName    string // Add constant name (π or Golden Ratio)
}

// GizaPyramidAnalysis encapsulates the logic for analysis
type GizaPyramidAnalysis struct {
	PI             float64
	GoldenRatio    float64
	BaseStep       float64
	HeightStep     float64
	BaseRanges     [][]float64 // Multiple ranges for base
	HeightRanges   [][]float64 // Multiple ranges for height
}

// NewGizaPyramidAnalysis initializes default parameters
func NewGizaPyramidAnalysis() *GizaPyramidAnalysis {
	return &GizaPyramidAnalysis{
		PI:             math.Pi,
		GoldenRatio:    1.618033988749895,
		BaseStep:       0.1,
		HeightStep:     0.1,
	}
}

// calculatePyramidMetrics computes Pi and Golden Ratio for a given base and height
func (g *GizaPyramidAnalysis) calculatePyramidMetrics(baseLength, height float64) *PyramidMetrics {
	if math.Abs(height) < 1e-10 {
		return nil // Avoid division by zero
	}

	halfBase := baseLength / 2
	edge := math.Sqrt(math.Pow(height, 2) + math.Pow(halfBase, 2))
	if math.Abs(halfBase) < 1e-10 {
		return nil
	}

	pivalue := (baseLength * 2) / height
	goldenratio := edge / halfBase

	// Determine which constant is closer
	constant := "Golden Ratio"
	if math.Abs(pivalue-g.PI) < math.Abs(goldenratio-g.GoldenRatio) {
		constant = "π"
	}

	return &PyramidMetrics{
		BaseLength:      baseLength,
		Height:          height,
		CalculatedPi:    pivalue,
		PiDifference:    math.Abs(pivalue - g.PI),
		CalculatedGR:    goldenratio,
		GRDifference:    math.Abs(goldenratio - g.GoldenRatio),
		ConstantName:    constant,
	}
}

func saveToFile(filename string, data []PyramidMetrics) error {
	// Open the file in write mode (overwrite if exists)
	file, err := os.OpenFile(filename, os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)

	// Write the header row
	fmt.Fprintf(writer, "%-15s %-15s %-15s %-20s %-20s %-20s %-20s\n",
		"Constant Name", "Base Length", "Height", "Calculated Pi", "Pi Difference",
		"Calculated GR", "GR Difference")

	// Sort the data by PiDifference then GRDifference
	sort.SliceStable(data, func(i, j int) bool {
		// First sort by PiDifference, then by GRDifference if PiDifference is equal
		if data[i].PiDifference == data[j].PiDifference {
			return data[i].GRDifference < data[j].GRDifference
		}
		return data[i].PiDifference < data[j].PiDifference
	})

	// Write the data rows
	for _, d := range data {
		fmt.Fprintf(writer, "%-15s %-15.4f %-15.4f %-20.10f %-20.10f %-20.10f %-20.10f\n",
			d.ConstantName, d.BaseLength, d.Height, d.CalculatedPi, d.PiDifference,
			d.CalculatedGR, d.GRDifference)
	}

	writer.Flush()
	return nil
}

func (g *GizaPyramidAnalysis) findConstantCrossings(outputFile string) []PyramidMetrics {
	var results []PyramidMetrics

	// Iterate through all base and height ranges
	for _, baseRange := range g.BaseRanges {
		for _, heightRange := range g.HeightRanges {
			// Process base and height values dynamically in small steps
			baseVal := baseRange[0]
			for baseVal <= baseRange[1] {
				heightVal := heightRange[0]
				for heightVal <= heightRange[1] {
					if heightVal == 0 {
						heightVal += g.HeightStep
						continue
					}

					// Calculate the metrics for the current base and height
					metrics := g.calculatePyramidMetrics(baseVal, heightVal)
					if metrics == nil {
						heightVal += g.HeightStep
						continue
					}

					// Check for Pi and Golden Ratio crossings
					if metrics.PiDifference < 0.01 || metrics.GRDifference < 0.01 {
						// Add to results
						results = append(results, *metrics)
						fmt.Printf("Crossing found: Base Length = %.4f, Height = %.4f\n", baseVal, heightVal)
					}
					// Increase height and move to next value
					heightVal += g.HeightStep
				}
				// Increase base and move to next value
				baseVal += g.BaseStep
			}
		}
	}
	return results
}

// Parse a range from the command line in format "start-end"
func parseRange(rangeStr string) ([]float64, error) {
	parts := strings.Split(rangeStr, "-")
	if len(parts) != 2 {
		return nil, fmt.Errorf("invalid range format, expected 'start-end' format")
	}
	start, err := strconv.ParseFloat(parts[0], 64)
	if err != nil {
		return nil, fmt.Errorf("invalid start value: %v", err)
	}
	end, err := strconv.ParseFloat(parts[1], 64)
	if err != nil {
		return nil, fmt.Errorf("invalid end value: %v", err)
	}
	return []float64{start, end}, nil
}

func main() {
	// Define command-line arguments
	baseRangeStr := flag.String("base", "100-200", "Base length range in 'start-end' format")
	heightRangeStr := flag.String("height", "100-200", "Height range in 'start-end' format")
	outputFile := flag.String("output", "data.txt", "Output file to save findings")
	baseStep := flag.Float64("basestep", 1, "Base step value")
	heightStep := flag.Float64("heightstep", 1, "Height step value")
	flag.Parse()

	// Parse the base and height ranges
	baseRange, err := parseRange(*baseRangeStr)
	if err != nil {
		log.Fatalf("Error parsing base range: %v\n", err)
	}

	heightRange, err := parseRange(*heightRangeStr)
	if err != nil {
		log.Fatalf("Error parsing height range: %v\n", err)
	}

	// Initialize the analysis with user-provided ranges
	analysis := NewGizaPyramidAnalysis()
	analysis.BaseStep = *baseStep
	analysis.HeightStep = *heightStep
	analysis.BaseRanges = [][]float64{baseRange}
	analysis.HeightRanges = [][]float64{heightRange}

	// Set up signal handling
	sigs := make(chan os.Signal, 1)
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	// Start the analysis in a goroutine so we can listen for termination signals
	go func() {
		fmt.Println("Finding constant crossings...")
		results := analysis.findConstantCrossings(*outputFile)

		// Save the sorted results to the output file
		fmt.Println("Saving results to file...")
		err = saveToFile(*outputFile, results)
		if err != nil {
			log.Fatalf("Error saving results: %v\n", err)
		}
		fmt.Println("Analysis completed.")
	}()

	// Wait for termination signal
	<-sigs
	fmt.Println("Program interrupted. Exiting...")
}
