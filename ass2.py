#Count and display the total number of words in a text file "ABC.txt"
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_words_in_file("ABC.txt")
