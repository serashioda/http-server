# -*- coding: utf-8 -*-
"""This is the echo server."""

import socket
import email.utils


def build_server():
    """Build server socket and listen for response."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 4001)
    server.bind(address)
    server.listen(1)

    while True:
        print("Server listening on port", address[1], "...")
        try:
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            msg = ""
            while not message_complete:
                part = conn.recv(buffer_length)
                msg += part.decode('utf8')
                if len(part) < buffer_length:
                    break
            print(msg)
            full_message = response_ok() + msg
            conn.sendall(full_message.encode('utf8'))

        except KeyboardInterrupt:
            conn.close()
            server.shutdown()
            server.close()


def response_ok():
    """Return 200 OK Response."""
    response = 'HTTP/1.1 200 OK\r\n'
    response += 'Content-Type: text/plain; charset=utf-8'
    # response += 'Date: ' + email.utils.formatdate(usegmt=True)
    response += '\r\n\r\n'
    return response


def response_error():
    """Return 404 Error Response."""
    response = 'HTTP/1.1 500 Internal Server Error\r\n'
    response += 'Content-Type: text/plain; charset=utf-8'
    # response += 'Date: ' + email.utils.formatdate(usegmt=True)
    response += '\r\n\r\n'
    return response


def parse_request(request):
    """."""
    request = request.replace('\r\n', ' ').split()
    if request[0] != 'GET':
        return '405'
    if request[2] != 'HTTP/1.1':
        return '406'
    if request[3] != 'HOST':
        return '400'
    return request[1]

if __name__ == "__main__":
    """"The script excutes from command line."""
    build_server()
