#write a prgram to count the occurrences of word "India" in the text file India.txt

word_to_search = "india"
word_count=0
with open("india.txt", "r") as file:
    content=file.read()
    print(content)
    content_lower=content.lower()
    words=content_lower.split()
    word_count=words.count(word_to_search)
print("\n**********************\n")
print(f'the word " {word_to_search}" occurs { word_count} times in the file.\n')


                                    