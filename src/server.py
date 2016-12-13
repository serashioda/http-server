"""This is the echo server."""

import socket

server = socket.socket()
address = ('127.0.0.1', 4000)
server.bind(address)
conn, addr = server.accept()

# def create_server_socket():
#     """Function builds server socket."""


def server_listen():
    """Function listens for client messages."""
    buffer_length = 8
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            break

server_listen()
