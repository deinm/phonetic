f = open("word_list.txt",'r')
lines = f.readlines()
words = []
for line in lines:
    words.append(line.rstrip())
f.close()
print(words)

f = open("read_to_eng.txt","r")
lines = f.readlines()
reads = []
for line in lines:
    reads.append(line.rstrip())

f.close()
print(lines)

f = open("phonetic_words.txt","w")
phonetic = []

for real_word in words:
    for read_word in reads:
        if real_word == read_word :
            phonetic.append(real_word)

phonetic = '\n'.join(phonetic)
f.write(phonetic)
f.close()
