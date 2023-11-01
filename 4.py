a = input().split()
b = int(a[0])
c = len(a)
n = 0
while n != c:
    if int(b) > int(a[n]): b = int(a[n])
    else: pass
    n += 1
print(b)
