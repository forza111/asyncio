

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlablaException(Exception):
    pass


#@coroutine
# yield from содержит инициализацию подгенератора
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            #print("Ky-Ky!!")
            break
        else:
            print(".......", message)

    return "Returned from subgen() "


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlablaException as e:
    #             g.throw(e)
    result = yield from g
    print(result)

