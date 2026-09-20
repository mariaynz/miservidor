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
print(f"direccion: {direccion}")

# leer hasta 1024 bytes del request que mandó el cliente
receive = socket_conexion.recv(1024)
print(f"receive(en bytes crudos): {receive}")  # bytes crudos del request HTTP (método, path, headers)

''' Esta parte se cambió abajo
# construir la respuesta HTTP: status line + headers + línea vacía + body
mensaje_string = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nHola mundo"

# convertir el string a bytes, porque los sockets solo mandan/reciben bytes
mensaje_bytes = mensaje_string.encode()

# enviar la respuesta al cliente por la misma conexión que usamos para leer su request
socket_conexion.send(mensaje_bytes)
'''

# para leer request, convertirlo de bytes a un string normal de Python
request = receive.decode()
# separar el string y guardarlo en una lista.
lineas = request.split("\r\n")
print(f"Receive convertido a string, y guardado por partes en un arreglo: {lineas}")

# guardar status line
status_line = lineas[0]
#separar status line
status_line_split = status_line.split()
metodo = status_line_split[0]
path = status_line_split[1]
print(f"status line: {status_line}")
print(f"metodo: {metodo}")
print(f"path: {path}")

if path == "/":
    mensaje_string = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 10\r\n\r\nHola mundo"

else:
    mensaje_string = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 9\r\n\r\nError 404"
    
mensaje_bytes = mensaje_string.encode()
socket_conexion.send(mensaje_bytes)