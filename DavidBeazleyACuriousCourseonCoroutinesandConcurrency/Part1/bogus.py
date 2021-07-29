# Bogus example of a generator that produces and receives values

def countdown(n):
    print("Counting down from", n)
    while n > 0:
        newvalue = yield n
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


c = countdown(5)

for x in c:
    print(x)
    if x == 5:
        c.send(3)

