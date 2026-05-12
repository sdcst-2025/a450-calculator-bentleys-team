import math
import time


#defining all different options for the calculator
def addition():
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A + B
            print(f"The sum is {C}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def subtraction():
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A - B
            print(f"The difference is {C}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def multiply():
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A * B
            print(f"The product is {C}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def division():
        try:
            A = float(input("Enter your first number: "))
            B = float(input("Enter your second number: "))
            C = A / B
            print(f"The quotient is {C}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def circumference():
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
            return
            
            circ = 2 * math.pi * radius
            circ = round(circ, 2)
            print(f"The circumference is {circ}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")

def rectangle_volume():
        try:
            length = float(input("Enter the length of the rectangular prism: "))
            if length <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
                return

            width = float(input("Enter the width of the rectangular prism: "))
            if width <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
                return

            height = float(input("Enter the height of the rectangular prism: "))
            if height <= 0:
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
                return

            volume = length * width * height
            volume = round(volume, 2)
            print(f"The volume is {volume}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def cylinder_area():
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            if radius <= 0: 
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
                return
                
            height = float(input("Enter the height of the cylinder: "))
            if height <= 0: 
                print("\nInvalid - Cannot be negative or 0\n")
                time.sleep(2)
                return
                
            area = (2 * math.pi* radius * height) + (2 * math.pi * (radius**2))
            area = round(area, 2)
            
            print(f"The area is {area}.")
            time.sleep(2)
        except ValueError:
            print("Enter a valid number.")
            time.sleep(1)

def CAD_USD():
        try:
            CAD = float(input("Enter the amount of Canadian dollars: "))
            
            decimals = len(str(CAD).split(".")[1])
            if decimals > 2:
                print("\nToo many decimal places\n")
                time.sleep(2)
                return
                
            if CAD < 0:
                print("\nCannot be negative\n")
                time.sleep(2)
                return
                
            USD = CAD * 0.73
            USD = round(USD, 2)

            print(f"That is ${USD} in USD")
        except ValueError:
            print("Enter a valid number.")


#defining the title function for the calculator
def title():
    while True:
        print("Welcome to Bentleys Calculator")
        time.sleep(0.5)

        try:
            print("For addition, type 1")
            time.sleep(0.1)
            print("For subtraction, type 2")
            time.sleep(0.1)
            print("For multiplication, type 3")
            time.sleep(0.1)
            print("For division, type 4")
            time.sleep(0.1)
            print("To find circumference of a circle, type 5")
            time.sleep(0.1)
            print("To find volume of a rectangular prism, type 6")
            time.sleep(0.1)
            print("To find the area of a cylinder, type 7")
            time.sleep(0.1)
            print("To convert CAD to USD, type 8")
            time.sleep(0.1)
            print("To exit the calculator, type 9")
            time.sleep(1)

            choice = int(input("What would you like to do: "))
        except ValueError:
            print("\nNot a valid choice.\n")
            time.sleep(1)
            continue

        
        #checking which option is chosen, and running it
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiply()
        elif choice == 4:
            division()
        elif choice == 5:
            circumference()
        elif choice == 6:
            rectangle_volume()
        elif choice == 7:
            cylinder_area()
        elif choice == 8:
            CAD_USD()
        elif choice == 9:
            print("Goodbye")
            break
        else:
             print("Choose a number from 1-9")
             time.sleep(1)
        



title()