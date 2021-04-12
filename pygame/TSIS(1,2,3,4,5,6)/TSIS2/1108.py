# 1108. Defanging an IP Address
s = input()
a1 = s.index('"')
a2 = s.rindex('"')
new_s = ''
for i in range (a1, a2+1):
    new_s += s[i]
print(new_s.replace('.', '[.]', 3))
