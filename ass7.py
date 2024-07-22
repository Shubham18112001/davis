# Open a file and handle a FileNotFoundError exception if the file does not exist
def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")


open_file("nonexistent.txt")
