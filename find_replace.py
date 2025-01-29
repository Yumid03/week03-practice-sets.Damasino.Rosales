with open("find_replace.txt", "r") as file:
    content = file.read()

new_word = content.replace("old", "new")


with open("find_replace.txt", "w") as file:
    file.write(new_word)
  
#another textfile/txt
this boat is old

the house next to ours is old

the old woman ran like a cheetah

youre old!

#Word_frequencies.py
with open('words.txt', 'r') as file:
    text = file.read()


words = text.split()
word_count = {}


for word in words:
    word = word.lower()  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


with open('word_frequencies.txt', 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")
      
#word_frequency.txt
the_word: 2
sentence_word: 1
"the_word: 2
young_word: 3
boy_word: 1
jumped_word: 1
like_word: 2
a_word: 1
rabbit_word: 1
looks_word: 1
funny_word: 1
kids_word: 1
can't_word: 1
fly_word: 1
that_word: 1
adults_word: 1
feel_word: 2
strong_word: 1
arms_word: 1
and_word: 1
have_word: 1
less_word: 1
stamina_word: 1
to_word: 2
do_word: 1
amazing_word: 1
feats_word: 1
like_word: 1
jumping_word: 1
not_word: 1
even_word: 1
think_word: 1
fly_word_exclamation: 1
wow_word_exclamation: 1

#word content
the word young boy jumped like a rabbit looks funny kids can't 
fly that adults feel strong arms and have less stamina to do amazing
feats like jumping not even think fly wow

#merged.py
with open('file1.txt', 'r') as file1:
    content1 = file1.read()


with open('file2.txt', 'r') as file2:
    content2 = file2.read()


merged_content = content1 + '\n' + content2


with open('merged.txt', 'w') as merged_file:
    merged_file.write(merged_content)

#merged.txt
file 1
file 2

#file1.txt
file 1


#file2.txt
file 2


