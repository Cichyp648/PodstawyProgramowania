try:
    #books.csv
    file_name = input("Enter the name of the file: ")
    
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        lineAmount = len(lines)
        charAmount = sum(len(line) for line in lines)
        wordAmount = sum(len(line.split()) for line in lines)
    
    # Print the results
    print(f"File name: {file_name}")
    print(f"Number of lines: {lineAmount}")
    print(f"Number of characters: {charAmount}")
    print(f"Number of words: {wordAmount}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except:
    print('An error occured')
