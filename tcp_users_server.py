import socket

#Список для хранения всех сообщений
messages = []

#Создаем TCP-сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Привязываем сервер к localhost
server_socket.bind(("127.0.0.1", 12345))

#Разрешаем до 10 подключений
server_socket.listen(10)

print("Сервер запущен и ожидает подключения...")

while True:
    #Принимаем подключение клиента
    client_socket, client_address = server_socket.accept()

    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    #Получаем сообщение от клиента
    data = client_socket.recv(1024).decode()

    print(
        f"Пользователь с адресом: {client_address} отправил сообщение: {data}"
    )

    #Сохраняем сообщение в историю
    messages.append(data)

    #Отправляем клиенту всю историю сообщений
    history = "\n".join(messages)

    client_socket.send(history.encode())

    #Закрываем соединение
    client_socket.close()