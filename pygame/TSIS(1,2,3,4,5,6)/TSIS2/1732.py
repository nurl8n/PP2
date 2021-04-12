# 1732. Find the Highest Altitude
s = input()
a1, a2 = s.index('['), s.rindex(']')
new_s = ''
for i in range(a1+1, a2):
    new_s += s[i]
x = new_s.split(',')
b = []
for i in range(len(x)):
    b.append(int(x[i]))
a = [0]
for j in range(len(b)):
    a.append(b[j])
c = []
lol = 0
for k in range(len(a)):
    lol += a[k]
    c.append(lol)
tt = max(c)
print(tt)
