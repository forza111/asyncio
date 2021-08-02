import time
import queue
from elapsedtimer import ElapsedTimer

'''Многозадачность с блокирующим кодом. Пример демонстрирует синхронное выполнение 
task-ов.'''


def task(name, queue):
    while not queue.empty():
        delay = queue.get()
        et = ElapsedTimer()
        et.start()
        print(f"Task {name} running")
        time.sleep(delay)
        et.stop()
        print(f"Task {name} total elapsed time: {et.elapsed:.1f}")
        yield


def main():
    """
    This is the main entry point for the program.
    """
    # Create the queue of 'work'
    work_queue = queue.Queue()

    # Put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [
        task("One", work_queue),
        task("Two", work_queue)
    ]

    # Run the tasks
    et = ElapsedTimer()
    et.start()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True
    et.stop()
    print(f"\nTotal elapsed time: {et.elapsed:.1f}")


if __name__ == "__main__":
    main()