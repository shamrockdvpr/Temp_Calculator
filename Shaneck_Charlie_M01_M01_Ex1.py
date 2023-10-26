docs = """
Author: Charli Shaneck
Program: Fahrenheit Celsius Convertor
Version:
    0.1 Pre Release Alpha
        Changelog:
        - Added Program Functionality, Celsius to Fahrenheit conversion

    1.0 Full Release Version
        Changelog:
        - Full documentation overhaul
        - Added docstrings for function
        - Added Input Sanitizer for temp model
        - Added Fahrenheit to Celsius conversion
        
    1.1 Final Version
        Changelog
        - Cleaned up code
        - Added input sanitizing for temperature inputs
        - Added main menu
        

Date Modified: 10/26/2023
Description: This program converts between two temperature measuring models based on user input.
Takes in a value to determine starting model and then a value for temperature to be converted.

Documentation:

Convertor:
    Converts starting temperature to alternate temperature model

    :parameter:
    start_model (str): Value representing what temperature model the temperature is in
    temp (float): Value representing the temperature a user wants to convert

    :return:
    new_temp (float): new temperature
    model (str): new temperature model

start_model : (str) user input for starting temp model, must be sanitized to be either C or F
temp : (float) user input for starting temp

Menu()
    Runs the main menu directory interface
    
    intakes a string input from the user
    runs one of three actions based on that input:
        1 - runs main program with run()
        2 - prints documentation
        3 - quits program

Run()
    Main program runner
    intakes two user inputs and passes them through the convertor module
    prints results to console
"""


def converter(start_model='C', temp=0.0):
    """Converts starting temperature to alternate temperature model

    :parameter:
    start_model (str): Value representing what temperature model the temperature is in
    temp (float): Value representing the temperature a user wants to convert

    :return:
    new_temp (float): new temperature
    model (str): new temperature model
    """
    if start_model == "C":
        new_temp = (9 / 5) * temp + 32
        model = "Fahrenheit"
        return [new_temp, model]

    elif start_model == "F":
        new_temp = (temp - 32) * 5 / 9
        model = "Celsius"
        return [new_temp, model]

    else:
        return None


def Menu():
    print("*" * 10)
    print("""Welcome to the temperature conversion Calulator!
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
            run()
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


def run():
    start_model = input("Enter the temperature model you would like to convert from (\"C or F\"): ").upper()

    while start_model not in ['C', 'c', 'F', 'f']:
        # makes sure start_model is a supported temperature model

        print(f"Sorry, {start_model} is not supported at this time or does not exist, please enter either Fahreheit ("
              f"F) or Celsius (C)")
        start_model = input("Enter the temperature model you would like to convert from (\"C or F\"): ").upper()

    temp = input("Enter the temperature you would like to convert: ")
    is_done = False
    while not is_done:
        try:
            temp = float(temp)
            is_done = True

        except ValueError:
            print(f"{temp} is not a valid input, please enter a new temperature:")
            temp = input("Enter the temperature you would like to convert: ")

    new_temp, model = converter(start_model, temp)[0], converter(start_model, temp)[1]

    print(f"{new_temp} in {model}")


Menu()  # runs program
