# A coroutine that catches the close() operation


from DavidBeazleyACuriousCourseonCoroutinesandConcurrency.Part1.coroutine import coroutine

@coroutine
def grep(pattern):
    print(f"Looking for {pattern}")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye")


if __name__ == "__main__":
    g = grep("python")

    g.send("Yeah. but no, but yeah, but no\n")
    g.send("A series of tubes\n")
    g.send("python generators rock!\n")

    g.close()