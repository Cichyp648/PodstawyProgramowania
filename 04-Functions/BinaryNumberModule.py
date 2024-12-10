def IsBinary(number):
    if all(char in '01' for char in number): return True
    else: return False