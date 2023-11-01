a = input().split()
b = a[0]
c = len(a) - 1
n = 0
while n != c:
    if len(b) > len(a[n]): b = a[n]
    else: pass
    n += 1
print(b)

