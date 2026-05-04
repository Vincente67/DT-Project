def calculate_resistor():
    print ("LED Resistor Calculator")

    try:
        # Input 
        supply_voltage = float(input(" Enter supply voltage (V): "))
        led_voltage = float(input("Enter LED foward voltage (V): "))
        current = float(input("Enter current (A): "))
      
        # Validation 
        if supply_voltage <= 0 or led_voltage <= 0 or current <=0:
        print(values must be greater than 0")
        return 

        if led_voltage >= supply_voltage:
        print ("LED Voltage must be less than supply voltage")
        return 
