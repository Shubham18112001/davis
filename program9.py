#write a prgram to display line having more than five words in the text file India.txt

with open("india.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    words = line.split()
    if len(words)>5:
        print(line.strip())