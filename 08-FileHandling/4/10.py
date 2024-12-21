import csv

def filter_products(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
                print(f"{row['Product_Name']}, {row['Price']}, {row['Stock_Quantity']}")

filter_products('clothing.csv')
