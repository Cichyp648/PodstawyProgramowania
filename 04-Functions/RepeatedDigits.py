def repetitions(number):
    num_str = str(number)
    digit_count = {}
    total_sum = 0
    
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    for digit, count in digit_count.items():
        if count > 1:
            total_sum += int(digit) * (count - 1)

    return total_sum


print(repetitions(1027))
print(repetitions(230335))
print(repetitions(513553007))
