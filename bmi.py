#!/usr/bin/env python3
# BMI = (weight in kg / height in meter squared)
# Imperial version: BMI * 703

def gather_info():
    height = float(input("What is your height? (inches or meters): "))
    weight = float(input("What is your weight? (pounds or kilograms): "))
    system = input("Are your measuremnts in metris or imperial units? (m or i): ").lower().strip()
    return (height, weight, system) # return tuple

def calculate_bmi(weight, height, system='metric'): #set default arguement by indicating the setup
    """
    Return the Body Mass Index (BMI) for the given
    weight, height and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height) #input variable can be jumble out but must be mentioned using =
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height, system)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measuremenet system. Please use imperial or metric.")