basic_data = {
    "name": "Barbara",
    "age": 21
}

additional_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

person = basic_data.copy()
person.update(additional_data)

print(person)
