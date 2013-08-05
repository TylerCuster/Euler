sumlist = []
total = 0
for n in range(0,1000):
    if n%3==0 or n%5==0:
        sumlist.append(n)
for n in sumlist:
    total = total + n
print total
