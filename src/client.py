# -*- coding: utf-8 -*-
"""Client for echo server."""

import socket
import sys


def create_client_socket(message):
    """Function builds the client socket."""
    server_info = socket.getaddrinfo('127.0.0.1', 4006)
    stream_info = [i for i in server_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    try:
        client.connect(stream_info[-1])
        message += "DISCONNECT"
        client.sendall(message.encode('utf8'))
    except ConnectionRefusedError:
        print("Connection Refused")
    buffer_length = 8
    msg = b''
    while msg[-10:] != b"DISCONNECT":
        msg += client.recv(buffer_length)
    msg = msg.decode('utf8')
    print(msg[:-10])
    client.close()
    return msg[:-10]


def main():
    """Run create client socket from command line."""
    create_client_socket(sys.argv[1])


if __name__ == "__main__":
    """The script will execute from command line."""
    main()
