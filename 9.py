def PythTriplet():
    a = range(999)
    b = range(999)
    c = range(999)
    for i in a:
        for j in b:
            for k in c:
                if i + j + k == 1000:
                    poss = [i, j, k]
                    print poss
                    if poss[0]**2 + poss[1]**2 == poss[2]**2 and i!=j!=k:
                        return poss[0]*poss[1]*poss[2]

print PythTriplet()
