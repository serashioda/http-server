# -*- coding: utf-8 -*-
"""HTTP server receives requests and send back appropriate response."""

import socket

ERRORS = {
    '405': "Method Not Allowed",
    '406': "Not Acceptable",
    '400': "Bad Request"
}


def build_server():
    """Build server socket, listen for request, and return response."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 4020)
    server.bind(address)
    server.listen(1)

    while True:
        print("Server listening on port", address[1], "...")
        try:
            conn, addr = server.accept()
            buffer_length = 8
            msg = b''
            msg_complete = False
            while not msg_complete:
                part = conn.recv(buffer_length)
                msg += part
                if len(part) < buffer_length or not part:
                    break
            msg = msg.decode('utf8')
            uri_or_error = parse_request(msg)
            if uri_or_error in ERRORS:
                error_response = response_error(uri_or_error)
                conn.sendall(error_response.encode('utf8'))
                conn.close()
            else:
                full_message = response_ok()
                conn.sendall(full_message.encode('utf8'))
                conn.close()

        except KeyboardInterrupt:
            conn.close()
            server.close()


def response_ok():
    """Return 200 OK Response."""
    response = u'HTTP/1.1 200 OK\r\n'
    response += 'Content-Type: text/plain; charset=utf-8'
    response += '\r\n\r\n'
    return response


def response_error(error):
    """Return appropriate Error Response."""
    response = 'HTTP/1.1 ' + error + ' ' + ERRORS[error] + '\r\n'
    response += 'Content-Type: text/plain; charset=utf-8'
    response += '\r\n\r\n'
    print(response)
    return response


def parse_request(request):
    """Parse request and check for errors, if no errors, return the URI."""
    request = request.replace('\\r\\n', ' ')
    request = request.split()
    if request[0] != 'GET':
        return '405'
    if request[2] != 'HTTP/1.1':
        return '406'
    if request[3] != 'Host:':
        return '400'
    return request[1]

if __name__ == "__main__":
    """"The script excutes from command line."""
    build_server()
