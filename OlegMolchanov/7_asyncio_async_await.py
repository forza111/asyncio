import asyncio
from time import time

'''OLD VERSION PYTHON'''
# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(1)
#
# @asyncio.coroutine
# def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} second have passed".format(count))
#         count += 1
#         yield from asyncio.sleep(1)
#
# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())
#
#     yield from asyncio.gather(task1,task2)


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()

"""NEW VERSION PYTHON"""

async def print_nums():
    num = 0
    while True:
        print(f"print nums {num}")
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} second have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task2,task1)





if __name__ == "__main__":
    asyncio.run(main())