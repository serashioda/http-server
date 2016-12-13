"""Client for echo server."""

import socket


def create_client_socket():
    """Function builds the client socket."""
    server_info = socket.getaddrinfo('127.0.0.1', 4000)
    stream_info = [i for i in server_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

create_client_socket()
