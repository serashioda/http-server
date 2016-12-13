"""This is the echo server."""

import socket

def build_server():
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 4000)
    server.bind(address)


# def create_server_socket():
#     """Function builds server socket."""

    """Function listens for client messages."""
    server.listen(1)
    conn, addr = server.accept()
    buffer_length = 8
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break

# server_listen()
build_server()

