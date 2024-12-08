age = float(input("Enter dogs age: "))
NewAge = 0,0
if age <= 2:
    age -= 2
    NewAge = 10,5
if age != 0:
    NewAge += age*4

print(f'Dogs age: {NewAge}')