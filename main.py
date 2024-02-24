# Problem Set 2
# Degree Converter

'''
    Create a program that converts temperature from Celsius to Fahrenheit and vice versa.
'''

# Fahrenheit to Celsius formula: c = (f - 32) * 5/9
# Celsius to Fahrenheit formula: f = c * 9/5 + 32

def to_celsius():
    f = int(input("Enter temperature in fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"This converts to {c}\N{DEGREE SIGN}")

def to_fahrenheit():
    c = int(input("Enter temperature in celsius: "))
    f = c * 9/5 + 32
    print(f"This converts to {f}\N{DEGREE SIGN}")

def main():
    print("MENU")
    print("1: Fahrenheit to celsius")
    print("2: Celsius to fahrenheit")
    print("")

    option = int(input("Enter a menu option: "))
    if option == 1:
        to_celsius()
    if option == 2:
        to_fahrenheit()

main()
