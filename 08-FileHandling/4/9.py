import csv

with open('it_company.csv', mode='r') as file:
    reader = csv.DictReader(file)

    print("GRAPHIC DESIGNERS")
    print("=================")
    
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
