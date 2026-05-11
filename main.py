def calculate_resistor():
    print ("LED Resistor Calculator")
    
# Keeps repeating until the user enters valid values
    while True:
        try:
            # Input
            supply_voltage = float(input("Enter supply voltage (V): "))
            led_voltage = float(input("Enter LED forward voltage (V): "))
            current = float(input("Enter current (A): "))

            # Validation
            if supply_voltage <= 0 or led_voltage <= 0 or current <= 0:
                print("Values must be greater than 0. Try again.\n")

            elif led_voltage >= supply_voltage:
                print("LED voltage must be less than supply voltage. Try again.\n")
            
            else:
                # Calculation (Ohm's law)
                resistance = (supply_voltage - led_voltage) / current 

                # Output 
                print(f"\nRequired resistor: {round(resistance, 2)} ohms")
                break # Stops loop when values are correct
               
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
        

    #-------------------Practice Question 1 --------------------------
    print("\n--- Ohm's law quiz ---")
    print("What is the formula for Ohm's Law?")
    print("A. V = I x R")
    print("B. V = I + R")
    print("B. V = I + R") 
    print("B. V = I ÷ R")

    answer = input("Enter A, B, or C: ").lower()

    if answer == "a":
        print("Correct! Ohm's law is V = I x R")
    else:
        print("Incorrect. The correct answer was V = I x R")



    #------------------- Practice Question 2 --------------------------
    print("\n--- Ohm's law quiz 2 ---")
    print("What does 'R' stand for in Ohm's Law?")
    print("A. Resistance")
    print("B. Rotation")
    print("C. Radiation")
            
    answer2 = input("Enter A, B, or C: ").lower()
        
    if answer2 == "a":
        print("Correct! R stands for Resistance")
    else:
        print ("Incorrect. The correct answer is A. Resistance")

           
    #------------------- Practice Question 3 --------------------------
    print("\n--- Ohm's law quiz 3 ---")
    print("What unit is resistance measured in?")
    print("A. Volts")
    print("B. Amps")
    print("C. Ohms")

    answer3 = input("Enter A, B, or C: ").lower()
    if answer3 == "c":
        print("Correct! Resistance is measured in ohms")
    else:
        print("Incorrect. The correct answer is C. Ohms")
            

# Run the program 
calculate_resistor() 
