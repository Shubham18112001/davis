def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
filename = input("Enter the filename to open: ")
open_file(filename)
