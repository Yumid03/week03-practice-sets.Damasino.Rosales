#write.file.py
# Write to the source file
with open("source.txt", "w") as src_file:
    src_file.write("hello, world!\n")
    
# Append to the source file
with open("source.txt", "a") as src_file:
    src_file.write("this is appended text.\n") 

# Get content of src_file
with open("source.txt", "r") as src_file:
    file_content = src_file.read()

# Copy content to the destination file
with open("destination.txt", "w") as dest_file:
    dest_file.write(file_content)
  
  #Source.txt
  hello, world!
this is appended text.

#destination.txt
hello, world!
this is appended text.

#write_string.py
strings = ["This is the first string", "Second string", "Third string", "And so on..."]


with open("strings.txt", "w") as file:
    for string in strings:
        file.write(string + "\n")

        print(string)
      
#string.txt
This is the first string
Second string
Third string
And so on...


#write_numbers.py
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

  #numbers.txt
1
2
3
4
5
6
7
8
9
10
 
  
