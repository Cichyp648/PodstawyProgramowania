def MaskCreditNumber(number):
    masked = number[:2] + (len(number)-6)*'*' + number[-4:]
    return masked