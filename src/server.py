"""This is the echo server."""

import socket

def build_server():
    """Build server socket and listen for response"""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 4000)
    server.bind(address)
    server.listen(1)

    while True:
        try:
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            msg = ""
            while not message_complete:
                part = conn.recv(buffer_length)
                msg += part.decode('utf8')
                if len(part) < buffer_length:
                    print("end msg")
                    break
            print(msg)

        except KeyboardInterrupt:
            server.close()


build_server()
