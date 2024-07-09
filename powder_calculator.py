import logging
import argparse
import tkinter as tk
from tkinter import messagebox

# Setup logging
logging.basicConfig(filename='powder_calculation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def calculate_powder_amount(area_mm2):

    calibration_factor = 1.0  # 1 mm² = 1 gram
    return area_mm2 * calibration_factor

def convert_to_mm2(area, unit):

    if unit == 'cm2':
        return area * 100  # 1 cm² = 100 mm²
    elif unit == 'mm2':
        return area
    else:
        raise ValueError("Unsupported unit. Please use 'mm2' or 'cm2'.")

def get_user_input():

    while True:
        try:
            user_input = input("Enter the desired area (e.g., '5 mm2' or '0.5 cm2'): ").strip()
            area_str, unit = user_input.split()
            area = float(area_str)
            
            if area < 0:
                raise ValueError("Area cannot be negative.")
            
            area_mm2 = convert_to_mm2(area, unit)
            return area_mm2
        except (ValueError, IndexError) as ve:
            print(f"Invalid input: {ve}. Please enter a valid area and unit.")

def main_cli():

    print("Powder Dispensing Calculation")
    print("----------------------------")
    print("This program calculates the amount of powder needed based on the area you input.")
    print("The calibration factor is: 1 mm² = 1 gram\n")

    area_mm2 = get_user_input()
    powder_amount = calculate_powder_amount(area_mm2)
    
    print(f"\nThe required powder amount is {powder_amount:.2f} grams.")
    logging.info(f"User Input: {area_mm2} mm², Calculated Powder Amount: {powder_amount:.2f} grams")

# GUI Implementation using Tkinter
def calculate_powder():
    try:
        area = float(area_entry.get())
        unit = unit_var.get()
        if area < 0:
            raise ValueError("Area cannot be negative.")
        
        area_mm2 = convert_to_mm2(area, unit)
        powder_amount = calculate_powder_amount(area_mm2)
        
        result_label.config(text=f"The required powder amount is {powder_amount:.2f} grams.")
        logging.info(f"User Input: {area_mm2} mm², Calculated Powder Amount: {powder_amount:.2f} grams")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")

def create_gui():
    global area_entry, unit_var, result_label

    window = tk.Tk()
    window.title("Powder Dispensing Calculator")

    tk.Label(window, text="Enter the desired area:").grid(row=0, column=0, padx=10, pady=10)
    area_entry = tk.Entry(window)
    area_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="Select the unit:").grid(row=1, column=0, padx=10, pady=10)
    unit_var = tk.StringVar(value='mm2')
    tk.Radiobutton(window, text="mm²", variable=unit_var, value='mm2').grid(row=1, column=1, padx=10, pady=10)
    tk.Radiobutton(window, text="cm²", variable=unit_var, value='cm2').grid(row=1, column=2, padx=10, pady=10)

    tk.Button(window, text="Calculate", command=calculate_powder).grid(row=2, column=0, columnspan=3, pady=10)
    result_label = tk.Label(window, text="")
    result_label.grid(row=3, column=0, columnspan=3, pady=10)

    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Powder Dispensing Calculator")
    parser.add_argument('--gui', action='store_true', help="Launch the GUI application")
    args = parser.parse_args()

    if args.gui:
        create_gui()
    else:
        main_cli()

if __name__ == "__main__":
    main()
