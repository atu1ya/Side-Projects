import sympy as sp # Importing required library

def doubleintcalc():
    """

    Calculates a double integral of a function with respect to x and y, always calculating with respect to y first, and then x, given lower bound < upper bound.

    """
    x, y = sp.symbols('x y')
    
    # Asking for required inputs
    x_lower = input("Enter the lower bound for x: ")
    x_upper = input("Enter the upper bound for x: ")
    y_lower = input("Enter the lower bound for y: ")
    y_upper = input("Enter the upper bound for y: ")
    f = input("Enter the function to be integrated with variables x and y: ")

    # Checking if bounds are valid
    if x_lower > x_upper or y_lower > y_upper:
        print("Invalid bounds.")
        doubleintcalc()
    if x_lower is not int or x_upper is not int or y_lower is not int or y_upper is not int:
        print("Invalid input.")
        doubleintcalc()
    
    # Calculating the integral
    inner_integral = sp.integrate(f, (y, y_lower, y_upper))
    outer_integral = sp.integrate(inner_integral, (x, x_lower, x_upper))
    print(outer_integral)


def singleintcalc():
    """
    Calculates a single integral of a function with respect to x, with bounds, given lower bound < upper bound.
    """

    x = sp.symbols('x')

    # Asking for required inputs
    x_lower = int(input("Enter the lower bound for x: "))
    x_upper = int(input("Enter the upper bound for x: "))
    f = input("Enter the function to be integrated with variables x and y: ")
    
    # Checking if bounds are valid
    if x_lower > x_upper:
        print("Invalid bounds.")
        singleintcalc()
    if x_lower == x_upper:
        print("The integral of a constant is zero.")
        return
    if x_lower is not int or x_upper is not int:
        print("Invalid input.")
        singleintcalc()

    # Calculating the integral
    integral = sp.integrate(f, (x, x_lower, x_upper))
    print(integral)



def main():
    """
    Main function that asks the user if they would like to calculate a single or double integral.
    """
    print("Would you like to calculate a single or double integral?")
    userinput = input("Type 's' for single and 'd' for double. ")
    if userinput != 's' and userinput != 'd':
        print("Invalid input.")
        main()
    if userinput == 's':
        singleintcalc()
        
    elif userinput == 'd':
        doubleintcalc()

main() # Running function