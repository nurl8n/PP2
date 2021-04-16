# 1
with open('aaa.txt') as f:
    contents = f.read()
    print(contents)
    
# 2
with open("aaa.txt") as myfile:
    head = [next(myfile) for x in range(2)]         # 1,2,3, ..., n
print(head)

# 3 
with open('aaa.txt', 'w') as lol:
    lol.write('LOOOOOOOOOOOL')
txt = open('aaa.txt')
print(txt.read())

# 4
a = open('aaa.txt', 'r')
lines = a.readlines()
last_lines = lines[-5:]
print(last_lines)
a.close()

# 5
with open('aaa.txt') as f:
    content = f.readlines()
li = [x.strip() for x in content]
print(li)

# 6
with open('aaa.txt', 'r') as x:
    data = x.readlines()
    print(data)
    
# 7
with open('aaa.txt') as my_file:
    t = my_file.readlines()
print(t)

# 8
with open('aaa.txt', 'r') as infile:
    words = infile.read().split()
max_len = len(max(words, key=len))
print(max_len)

# 9
file = open("aaa.txt", "r")
cnt = 0
for line in file:
    if line != "\n":
        cnt += 1
file.close()
print(cnt)

# 10
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())
print(word_count("aaa.txt"))

# 11
import os
file_name = 'aaa.txt'
file_stats = os.stat(file_name)
print(f'File Size in Bytes is {file_stats.st_size}')

# 12
a_list = ["abc", "def", "ghi"]
textfile = open("aaa.txt", "w")
for element in a_list:
    textfile.write(element + "\n")
textfile.close()

# 13
with open("aaa.txt") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)
            
# 14
with open('aaa.txt') as f1,open('copy.txt') as f2:
	for l1,l2 in zip(f1,f2):
		# print(l1+l2)
		l1=l1.strip()
		l2=l2.strip()
		print(l1+l2)
    
# 15
import random
lines = open('aaa.txt').read().splitlines()
myline =random.choice(lines)
print(myline)

# 16
f = open('aaa.txt','r')
print(f.closed)   # if False then file is opened
f.close()
print(f.closed)

# 17
def n(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]
print(n("aaa.txt"))

# 18
def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("aaa.txt"))

# 19
file = open('aaa.txt', 'r')
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()

# 20
import string
alphabet= string.ascii_lowercase
for letter in alphabet:
    with open(letter+".txt",'w') as file:
        file.write(letter)
        
# 21
import string
def letters_file_line(n):
   with open("aaa.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)
