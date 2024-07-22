# write a program to count and display number of words starting with "i" in a file India.txt

print("\nLetter starting with  I \n")
letter_to_search = 'i'
word_counts = 0
with open("india.txt", "r") as file:
    content = file.read()
    words = content.split()
    for word in words:
        cleaned_word = word.strip().lower()
        if cleaned_word.startswith(letter_to_search):
            word_counts += 1
print(f'Number of words starting with "{letter_to_search}": {word_counts}')