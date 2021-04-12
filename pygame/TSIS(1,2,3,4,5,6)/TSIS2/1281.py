# 1281. Subtract the Product and Sum of Digits of an Integer
# Solution 1
n = int(input())
summ = 0
prod = 1
while n:
    d = n%10
    summ += d
    prod *= d
    n //= 10
print(prod-summ)

# Solution 2
s = input()
x = ''
for i in range (len(s)):
    if s[i]=='=' or s[i]=='n' or s[i]==' ':
        continue
    else:
        x += s[i]
n = int(x)
summ = 0
prod = 1
while n:
    d = n%10
    summ += d
    prod *= d
    n //= 10
print(prod-summ)
