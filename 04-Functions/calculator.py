def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2

print(calculate(2, 3, "+"))
print(calculate(2, 3, "%"))
print(calculate(2, 3, "**"))
print(calculate(2, 3, "*"))
print(calculate(2, 3, "-"))