###
# A program that prints your height both in cm and in feet and inches.
#
cm = 182
inches = cm / 2.54
feet = inches // 12
inches = inches % 12

print(f'{cm}cm is equal to {feet:.0f} feet and {inches:.0f} inches')