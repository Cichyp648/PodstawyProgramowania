time = int(input("How long were you parked: "))
fee = 0

if time <= 2:
    fee = 5
elif time >= 2 and time <= 6:
    fee = 15
else :
    fee = 20


print(f'Parking fee is {fee} PLN')