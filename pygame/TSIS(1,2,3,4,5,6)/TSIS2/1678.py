# 1678. Goal Parser Interpretation
s = input()
a1 = s.index('"')
a2 = s.rindex('"')
new_s = ''
for i in range(a1, a2+1):
    new_s += s[i]
n = new_s.replace('()','o', 100)
x = ''
for i in range(len(n)):
    if n[i]=='(' or n[i]==')':
        continue
    else:
        x += n[i]
print(x)
