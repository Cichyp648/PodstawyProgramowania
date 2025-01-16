import json

# Dictionary describing Interstellar
interstellar_info = {
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014,
    "main_actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
    "genre": ["Science Fiction", "Adventure", "Drama"]
}


def main():
    # Write the dictionary to a JSON file
    with open('favourite.json', 'w') as file:
        json.dump(interstellar_info, file, indent=4)
    

if __name__ == '__main__':
    main()
