import CreditCardModule

# Sample number
CreditCardNumber = '5290312400019022'
# CreditCardNumber = input('Enter credit card number: ')

MaskedCreditNumber = CreditCardModule.MaskCreditNumber(CreditCardNumber)
print(f'Masked output: {MaskedCreditNumber}')