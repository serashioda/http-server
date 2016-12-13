"""This is the echo server."""

import socket


server = socket.socket()
address = ('127.0.0.1', 4000)
server.bind(address)
