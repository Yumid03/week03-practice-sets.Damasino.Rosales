line_count = 0
word_count = 0
char_count = 0

with open("examples.txt", "r") as file:
    for line in file:
        print(line.strip()) 
        line_count += 1 
        word_count += len(line.split()) 
        char_count += len(line.strip()) 
        
print(f"\nTotal number of lines: {line_count}")
print(f"Total number of words: {word_count}")
print(f"Total number of characters: {char_count}")

#another text file
example.txt
example 01 
example 02 
example 03

xdxdxd
