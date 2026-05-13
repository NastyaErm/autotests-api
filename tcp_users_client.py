import socket

#Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Подключаемся к серверу
client_socket.connect(("127.0.0.1", 12345))

#Сообщение
message = "Привет, сервер!"

#Отправляем сообщение
client_socket.send(message.encode())

#Получаем ответ
response = client_socket.recv(1024).decode()

#Выводим ответ
print(response)

#Закрываем соединение
client_socket.close()