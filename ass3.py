#Count uppercase characters in a text file "ABC.txt"
def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            uppercase_count = sum(1 for char in text if char.isupper())
            print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_uppercase_characters("ABC.txt")
