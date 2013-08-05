def Fibo(limit):
    fibo = []
    last = 1
    secondLast = 0
    new = 0
    while new < limit:
        new = last + secondLast
        if new%2==0:
            fibo.append(new)
            if new > limit:
                fibo.remove(new)
        secondLast = last
        last = new
    print fibo
    total = 0
    for n in fibo:
        total = total + n
    print total

Fibo(4000000)
