def ExtremesDifference(number1, number2, number3):
    biggest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return biggest - smallest

print(ExtremesDifference(7, 4, 9)) 
print(ExtremesDifference(2, 12, 8))  