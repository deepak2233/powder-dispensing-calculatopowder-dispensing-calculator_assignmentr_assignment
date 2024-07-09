# Powder Dispensing Calculator

This repository contains a Python script to calculate the amount of powder needed based on a user-defined area and a predefined calibration factor. The script provides both a command-line interface (CLI) and a graphical user interface (GUI) for user interaction.

## Features

- **Unit Conversion:** Allows input in different units (mm² and cm²) and converts to mm² for calculation.
- **Graphical User Interface (GUI):** Simple GUI implemented using Tkinter.
- **Logging:** Logs user inputs and calculated outputs for debugging and auditing purposes.
- **Command-Line Interface (CLI):** User-friendly interaction through the command line.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/powder-dispensing-calculator.git
   cd powder-dispensing-calculator

2. python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. pip install -r requirements.txt

4. python powder_calculator.py

5. python powder_calculator.py --gui



# Output Format
   $ python powder_calculator.py
   Powder Dispensing Calculation
   ----------------------------
   This program calculates the amount of powder needed based on the area you input.
   The calibration factor is: 1 mm² = 1 gram

   Enter the desired area (e.g., '5 mm2' or '0.5 cm2'): 5 mm2

   The required powder amount is 5.00 grams.



