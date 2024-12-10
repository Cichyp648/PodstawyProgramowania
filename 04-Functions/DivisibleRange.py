def CheckAndSum(x, y):
    total_sum = 0

    for num in range(x, y + 1):
        # Check if the number is divisible by both 2 and 3, but not by 4
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total_sum += num
    
    return total_sum

print(CheckAndSum(1, 20))
print(CheckAndSum(10, 30))