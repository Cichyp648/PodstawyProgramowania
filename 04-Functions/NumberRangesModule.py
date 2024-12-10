def IsInRange(RangeA, RangeB, NumberToCheck):
    if RangeB < RangeA:
        RangeA, RangeB = RangeB, RangeA
    if NumberToCheck in range(RangeA, RangeB): return True
    else: return False