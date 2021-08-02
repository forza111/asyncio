import asyncio
import queue
from elapsedtimer import ElapsedTimer

async def task(name, work_queue):
    while not work_queue.empty():
        print("before await delay")
        delay = await work_queue.get()
        print(f"await delay {delay}")
        et = ElapsedTimer()
        et.start()
        print(f"Task {name} running")
        await asyncio.sleep(delay)
        et.stop()
        print(f"Task {name} total elapsed time: {et.elapsed:.1f}")


async def main():
    work_queue = asyncio.Queue()

    for work in [15,10,5,2]:
        await work_queue.put(work)

    await asyncio.gather(
        asyncio.create_task(task("One",work_queue)),
        asyncio.create_task(task("Two", work_queue)),
    )

if __name__ == "__main__":
    asyncio.run(main())