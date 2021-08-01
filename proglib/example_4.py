import asyncio
import queue

async def task(name, work_queue):
    while not work_queue.empty():
        delay = await work_queue.get()
        # et  = ET()
        print(f"Task {name} running")
        await asyncio.sleep(delay)
        print(f"Task {name} total elapsed time:")


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