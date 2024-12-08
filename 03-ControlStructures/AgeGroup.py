age = int(input("How old are you: "))
group = ''

if age < 13:
    group = "child"
elif age >= 13 and age <= 19:
    group = "teen"
elif age >= 20 and age <= 64:
    group = "adult"
else:
    group = "Senior"

print(f'You are in the {group} age group')