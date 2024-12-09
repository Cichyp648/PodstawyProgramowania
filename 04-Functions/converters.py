def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    # 1 inch = 2.54 cm
    inches = n / 2.54
    return round(inches, 2)

def feet_and_inch_to_cm(feet, inches):
    # 1 foot = 30.48 cm, 1 inch = 2.54 cm
    total_cm = (feet * 30.48) + (inches * 2.54)
    return round(total_cm, 2)



if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'3cm = {cm_to_in(3)}in')
    print(f'3ft 5in = {feet_and_inch_to_cm(3, 5)}')