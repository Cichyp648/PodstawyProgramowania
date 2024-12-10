def detector(entries):
    count = 0
    for element in entries:
        if element == '+':
            count += 1
        elif element == '-':
            count -= 1
        if count >= 3:
            return True
    return False

print(detector("+-+++-+---"))  # Output: True
print(detector("+-+-+-+-"))    # Output: False
print(detector("+-++-+--"))    # Output: False
print(detector("+-++-++-+---")) # Output: True