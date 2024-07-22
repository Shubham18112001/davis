def count_vowels_and_consonants(file_path):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0

    with open(file_path, 'r') as file:
        text = file.read()
        for char in text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
    
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

count_vowels_and_consonants('india.txt')
