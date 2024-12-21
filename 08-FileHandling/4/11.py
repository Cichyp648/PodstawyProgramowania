def powers():
    with open("powers.txt", "a") as file:
        for i in range(1, 101):
            result = f"{i},{i ** 2},{i ** 3}"

            print(result)
            file.write(f'{result}\n')

powers()
