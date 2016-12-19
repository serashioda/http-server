# -*- coding: utf-8 -*-
"""HTTP server receives requests and send back appropriate response."""

import socket
import os
import base64

ERRORS = {
    '500': "Internal Server Error",
    '405': "Method Not Allowed",
    '406': "Not Acceptable",
    '400': "Bad Request",
    '404': "File Not Found",
    '401': "Unauthorized"
}

FILETYPE = {
    'jpg': 'image/jpg',
    'jpeg': 'image/jpeg',
    'txt': 'text/plain',
    'gif': 'image/gif',
    'png': 'image/png',
    'py': 'text/plain',
    'html': 'text/html'
}


def build_server():
    """Build server socket, listen for request, and return response."""
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 4025)
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
                try:
                    print("uri_or_error", uri_or_error)
                    body_content, content_type = resolve_uri(uri_or_error)
                    print("body_content:", body_content)
                    full_message = response_ok(body_content, content_type)
                except Exception as ex:
                    # Pick an error code based on the exception type
                    error_code = detect_error_code(ex)
                    full_message = response_error(error_code)
                conn.sendall(full_message.encode('utf8'))
                conn.close()
        except KeyboardInterrupt:
            conn.close()
            server.close()


def detect_error_code(ex):
    """Detect error message (value of ERRORS) and id's error code(key of ERRORS)."""
    if str(ex) == 'Filetype not supported.':
        return '404'
    elif str(ex) == 'File not found.':
        return '404'
    elif str(ex) == 'Unauthorized.':
        return '401'
    else:
        return '500'


def resolve_uri(uri_or_error):
    """Resolve the URI and return the appropriate message."""
    if '..' in uri_or_error:
        raise Exception('Unauthorized.')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), uri_or_error)
    print("LOOKING FOR FILE AT " + file_path)
    if os.path.isdir(file_path):
        file_list = os.listdir(file_path)
        files = ''
        for file in file_list:
            files += '<li>' + file + '</li>'
        body_content = '<html><body><ul>{}</ul></body></html>'.format(files)
        content_type = 'text/html'

    elif os.path.isfile(file_path):
        file_extension = file_path.split('.')[-1]
        print('File Type:', file_extension)

        if file_extension not in FILETYPE:
            raise Exception('Filetype not supported.')

        if FILETYPE[file_extension].split('/')[0] == 'text':
            with open(file_path, 'r') as myfile:
                body_content = myfile.read()
            content_type = FILETYPE[file_extension]
        elif FILETYPE[file_extension].split('/')[0] == 'image':
            print('image')
            with open(file_path, 'rb') as imageFile:
                body_content = base64.b64encode(imageFile.read())
            content_type = FILETYPE[file_extension]
        # else:
        #     raise Exception('Filetype not supported.')
    else:
        raise Exception('File not found.')
    return (body_content, content_type)


def response_ok(body_content, content_type):
    """Return 200 OK Response."""
    response = u'HTTP/1.1 200 OK\r\n'
    response += 'Content-Type: ' + content_type + '; charset=utf-8\r\n'
    response += 'Content-Length: ' + str(len(body_content)) + '\r\n'
    response += '\r\n\r\n'
    response += body_content
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
