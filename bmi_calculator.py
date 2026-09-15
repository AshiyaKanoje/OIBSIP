"""Simple BMI calculator."""
print("----- BMI Calculator -----")

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))

if weight <= 0 or height <= 0:
    print("Please enter valid values.")
else:
    bmi = weight / (height * height)

    print("\nHello", name)
    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
        
