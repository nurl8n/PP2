# 1512. Number of Good Pairs
s = input()
a1 = s.index('[')
a2 = s.rindex(']')
new_s = ''
for i in range(a1+1, a2):
    new_s += s[i]
a = new_s.split(',')
cnt = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
            cnt +=1
print(cnt)
