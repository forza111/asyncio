import socket
import selectors


selector = selectors.KqueueSelector()
# используется для ожидания готовности события ввода- вывода для нескольких файловых объектов.
# Он поддерживает регистрацию и отмену регистрации файлового потока, а также метод ожидания событий ввода-
# вывода в этих потоках с необязательным тайм-аутом.



def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ, #Доступно для чтения
        data=accept_connection
    )
    # Зарегистрировать файловый объект для выбора, отслеживая его на предмет событий ввода-вывода.
    # fileobj — файловый объект для мониторинга. Может быть целочисленным файловым дескриптором или объектом с методом fileno().
    # events — События, которые необходимо дождаться для данного файлового объекта
    # data — связвнные данные



def accept_connection(server_socket):
    client_socket,addr = server_socket.accept()
    print('Connection from', addr)

    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_massage
    )


def send_massage(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world \n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select() #(key,events)
        #Подождать, пока не будут готовы некоторые зарегистрированные файловые объекты или истечёт время ожидания

        for key, _ in events:
            callback = key.data #accept connection
            callback(key.fileobj) #socket

if __name__ == "__main__":
    server()
    event_loop()
    #accept_connection(server_socket)