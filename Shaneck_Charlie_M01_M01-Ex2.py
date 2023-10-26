docs = """
Author: Charli Shaneck
Program: Food cost calculator
Version:
1.0 Full Release Version
    Changelog:
    - Added program functionality


Date Modified: 10/26/2023
Description: This program takes in a user input of food charge and returns a breakdown of the charges on the bill
    Total Charge, Sales Tax, Tip of 18% and Food Cost

***** Documentation *****

Calculator:
    takes in user defined number and returns total, sales tax, and tip
    :param charge: (float), the money that the food costs
    :return: 
    a string that displays all values


Menu()
Runs the main menu directory interface

intakes a string input from the user
runs one of three actions based on that input:
1 - runs main program with run()
2 - prints documentation
3 - quits program

Run()
Main program runner
Intakes user input and returns a breakdown
"""


def calculator(charge):
    """
    takes in user defined number and returns total, sales tax, and tip
    :param charge: (float), the money that the food costs
    :return:
    a string that displays all values
    """
    charge = round(charge, 2)
    sales_tax = round(charge * 0.07, 2)
    tip = round(charge * 0.18, 2)

    print(f"""
    total charge is ${charge + sales_tax + tip}
    food charge is ${charge}
    sales tax is ${sales_tax}
    tip is ${tip}""")


def Menu():
    print("*" * 10)
    print("""Welcome to the food cost calculator!
    enter one of the following numbers to proceed:
    > 1 : Run program
    > 2 : About
    > 3 : Quit""")

    selection = input("> ")

    while selection != '3':
        while selection not in ['1', '2', '3']:
            print(f"Sorry, {selection} is not a valid menu option")
            selection = input("> ")

        if selection == '1':
            charge = float(input("Please enter the total food charge:"))

            if charge < 0:
                charge = -1 * charge
                print("Negative charge is not supported, we have converted to positive charge for you")

            calculator(charge)
            input("Press any key to continue:")
            print("""Select new menu item"
            > 1 : Run program 
            > 2 : About 
            > 3 : Quit""")
            selection = input("> ")

        elif selection == '2':
            print(docs)
            input("Press any key to continue:")
            print("""Select new menu item"
            > 1 : Run program 
            > 2 : About 
            > 3 : Quit""")
            selection = input("> ")

    else:
        quit()


Menu()
