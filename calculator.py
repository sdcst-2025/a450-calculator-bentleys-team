import math
import time

def title():
    print("Welcome to Bentleys Calculator")
    time.sleep(0.5)
    print("What would you like to do?")
    time.sleep(1)
    print("For addition, type 1")
    print("For subtraction, type 2")
    print("For multiplication, type 3")
    print("For division, type 4")
    print("To find circumference of a circle, type 5")
    print("To find volume of a rectangular prism, type 6")
    print("To find the area of a cylinder, type 7")
    print("To convert CAD to USD, type 8")

def addition():
    while True:
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A + B
            print(f"The sum is {C}.")
        except ValueError:
            print("Enter a valid number.")

def subtraction():
    while True:
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A - B
            print(f"The difference is {C}.")
        except ValueError:
            print("Enter a valid number.")

def multiply():
    while True: 
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A * B
            print(f"The product is {C}.")
        except ValueError:
            print("Enter a valid number.")

def division():
    while True: 
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A / B
            print(f"The quotient is {C}.")
        except ValueError:
            print("Enter a valid number.")

def circumference():
    while True: 
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                continue

            circ = 2 * math.pi * radius
            circ = round(circ, 2)
            print(f"The circumference is {circ}.")
        except ValueError:
            print("Enter a valid number.")

def rectangle_volume():
    while True: 
        try:
            length = float(input("Enter the length of the rectangular prism: "))
            if length <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                continue

            width = float(input("Enter the width of the rectangular prism: "))
            if width <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                continue

            height = float(input("Enter the height of the rectangular prism: "))
            if height <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                continue

            volume = length * width * height
            volume = round(volume, 2)
            print(f"The volume is {volume}.")
        except ValueError:
            print("Enter a valid number.")

def cylinder_area():
    while True: 
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            if radius <= 0: 
                print("\nInvalid - Cannot be negative or 0\n")
                continue
                
            height = float(input("Enter the height of the cylinder: "))
            if height <= 0: 
                print("\nInvalid - Cannot be negative or 0\n")
                continue

            area = (2 * math.pi* radius * height) + (2 * math.pi * (radius**2))
            area = round(area, 2)
            
            print(f"The area is {area}.")
        except ValueError:
            print("Enter a valid number.")

def CAD_USD():
    while True: 
        try:
            CAD = float(input("Enter the amount of Canadian dollars: "))
            
            decimals = len(str(CAD).split(".")[1])
            if decimals > 2:
                print("\nToo many decimal places\n")
                continue

            if CAD < 0:
                print("\nCannot be negative\n")
                continue

            USD = CAD * 0.73
            USD = round(USD, 2)

            print(f"That is ${USD} in USD")
        except ValueError:
            print("Enter a valid number.")

CAD_USD()
    