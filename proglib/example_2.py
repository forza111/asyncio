import  queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main():
    '''Это основная точка входа в программу'''

    #создание очереди работы
    work_queue = queue.Queue()

    #Размещение работы в очереди
    for work in [15,10,5,2]:
        work_queue.put(work)

    #создание задач
    tasks = [task("One",work_queue), task("Two", work_queue)]

    #запуск задач
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

if __name__ == "__main__":
    main()