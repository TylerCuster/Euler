import math
def smallestMultiple():
    n = 0
    while True:
        n += 20
        count = 0
        for c in reversed(range(11,21)):
            if n%c == 0:
                count += 1
            if count > 1:
                print n
            else:
                break
        if count == 10:
            return n

print smallestMultiple()
