#Read the content of a text file "ABC.txt" line by line and display it on the screen

def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_file_line_by_line("abc.txt")
