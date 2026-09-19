import socket

# crear un socket que usa IPv4 (AF_INET) y el protocolo TCP (SOCK_STREAM)
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# asignarle a este socket una IP y puerto fijos donde va a "vivir"
socket1.bind(("localhost", 8080))

# preparar el socket para poder aceptar conexiones entrantes
socket1.listen()
print("Está escuchando!")

# pausar el programa hasta que un cliente se conecte;
# accept() regresa un socket nuevo (para esta conexión) y la dirección del cliente
socket_conexion, direccion = socket1.accept()
print(direccion)

# leer hasta 1024 bytes del request que mandó el cliente
receive = socket_conexion.recv(1024)
print(receive)  # bytes crudos del request HTTP (método, path, headers)

# construir la respuesta HTTP: status line + headers + línea vacía + body
mensaje_string = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nHola mundo"

# convertir el string a bytes, porque los sockets solo mandan/reciben bytes
mansaje_bytes = mensaje_string.encode()

# enviar la respuesta al cliente por la misma conexión que usamos para leer su request
socket_conexion.send(mansaje_bytes)