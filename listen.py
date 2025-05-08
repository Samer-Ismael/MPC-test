import socket

host = '0.0.0.0'  # Listen on all available interfaces
port = 7070

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Listening on port {port}...")

# Accept an incoming connection
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Close the connection once it's accepted
    client_socket.close()

