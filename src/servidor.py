import socket

# crear socket
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(("localhost", 8080))
socket1.listen()
print("Está escuchando!")
conexion, direccion = socket1.accept()
print(direccion)
recieve = conexion.recv(1024)
print(recieve)
mensaje_string = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nHola mundo"
mansaje_bytes = mensaje_string.encode()
conexion.send(mansaje_bytes)