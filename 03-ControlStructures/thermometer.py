# Simulating the operation of an electronic thermometer
temperatures = [33, 30, 8, 0, -2]  # List of test temperatures

# Check each temperature in the list
for temperature in temperatures:
    if temperature > 35:
        print(f"{temperature}°C: It is extremely hot")
    elif temperature > 30:
        print(f"{temperature}°C: It is hot")
    elif temperature >= 15:
        print(f"{temperature}°C: It is warm")
    elif temperature >= 0:
        print(f"{temperature}°C: It is cold")
    else:  # temperature < 0
        print(f"{temperature}°C: Warning, frost")