import socket
from select import select

tasks = []

to_read = {}
to_write = {}

#domain:5000
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:

        yield ("read", server_socket)
        #print('Before .accept()')
        client_socket,addr = server_socket.accept()
        print('Connection from', addr)
        tasks.append(client(client_socket))
        print(f"tasks append {client(client_socket)}")


def client(client_socket):
    while True:
        yield ('read', client_socket)
        print('Before .recv()')
        request = client_socket.recv(4096)
        #print(request.decode())

        if not request:
            print("not request")
            break
        else:
            response = 'Hello world \n'.encode()
            print('before yield')
            yield ('write', client_socket)
            print(f"after {client_socket}")

            client_socket.send(response)
    print(f"close client_socket")
    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            print('event loop <<while not task>> 1')
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            print('event loop <<while not task>> select << done >>')
            print(f"ready to read::: --> {ready_to_read} -\n to read::: --> {to_read}, \nready_to write::: --> {ready_to_write} - \nto write::: -->{to_write}")


            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
                print(f"tasks.append(sock) for sock in ready_to_read APPEND")
                print(tasks)

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
                print(f"tasks.append(sock) for sock in ready_to_write APPEND")
                print(tasks)


        try:
            task = tasks.pop(0)
            print(f"from try Event loop")

            reason, sock = next(task)  #('write', client_socket)
            print(f"reason ---> {reason}\nsock ----> {sock}")

            if reason == 'read':
                to_read[sock] = task
                print(f"dict << to_read >> !!!APPEND!!! {sock} :::::: {task} ")
                print(f"dict << to_read >>  {to_read} ")
                print(f"dict << to_write >>  {to_write} ")


            if reason == 'write':
                to_write[sock] = task
                print(f"dict << to_write >> !!!APPEND!!! {sock} :::::: {task} ")
                print(f"dict << to_read >>  {to_read} ")
                print(f"dict << to_write >>  {to_write} ")



        except StopIteration:
            print("Done!")

tasks.append(server())
event_loop()