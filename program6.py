def count_lines_starting_with_T(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('T'):
                count += 1
                print(line.strip())
    print(f"Total lines starting with 'T': {count}")

count_lines_starting_with_T('india.txt')
