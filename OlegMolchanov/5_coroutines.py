

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

def subgen():
    while True:
        x = 'Ready to accept message'
        message = yield x
        print("Subgen received:", message)

class BlablaException(Exception):
    pass




@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Done")
            break
        except BlablaException:
            print('........')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count,2)

    return average