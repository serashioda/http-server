# # -*- coding: utf-8 -*-
"""Test client socket with various messages."""

from __future__ import unicode_literals
import os

body_content = 'I am a body content.'
content_type = 'text/plain'


def test_response_ok():
    """Test response_ok when request is valid."""
    from server import response_ok
    result = response_ok(body_content, content_type)
    assert result == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 20\r\n\r\nI am a body content.'


def test_response_error():
    """Test response_error when request is invalid."""
    from server import response_error
    result = response_error('406')
    assert result == 'HTTP/1.1 406 Not Acceptable\r\n\r\n'


def test_parse_request():
    """Test that uri is returned if request is valid."""
    from server import parse_request
    result = parse_request('GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
    assert result == '/index.html'


def test_parse_request_405():
    """Test that uri is returned if request is valid."""
    from server import parse_request
    result = parse_request('GT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
    assert result == '405'


def test_parse_request_406():
    """Test that uri is returned if request is valid."""
    from server import parse_request
    result = parse_request('GET /index.html HTTP/1.0\r\nHost: www.example.com\r\n\r\n')
    assert result == '406'


def test_parse_request_400():
    """Test that uri is returned if request is valid."""
    from server import parse_request
    result = parse_request('GET /index.html HTTP/1.1\r\nHst: www.example.com\r\n\r\n')
    assert result == '400'


# def test_resolve_uri_not_supported():
#     """Test exception when audio file requested."""
#     from server import resolve_uri
#     file = 'transferfiles/testdir/testme.aiff'

#     print("CURRENT DIRECTORY: " + os.getcwd())
#     print("FILE EXISTS: " + str(os.path.isfile(file)))

#     try:
#         resolve_uri(file)
#     except Exception as ex:
#         assert str(ex) == 'Filetype not supported.'


def test_resolve_uri_not_found():
    """Test exception when audio file requested."""
    from server import resolve_uri
    file = 'transferfiles/testdir/testme2.aiff'

    # print("CURRENT DIRECTORY: " + os.getcwd())
    # print("FILE EXISTS: " + str(os.path.isfile(file)))

    try:
        resolve_uri(file)
    except Exception as ex:
        assert str(ex) == 'File not found.'


def test_client_for_text_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET transferfiles/webroot/sample.txt HTTP/1.1\r\nHost: www.example.com\\r\\n\\r\\n")
    assert response == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 95\r\n\r\nThis is a very simple text file.\nJust to show that we can serve it up.\nIt is three lines long.\n'


def test_client_for_img_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET transferfiles/webroot/images/sample_1.png HTTP/1.1\r\nHost: www.example.com\\r\\n\\r\\n")
    assert response[:100] == 'HTTP/1.1 200 OK\r\nContent-Type: image/png; charset=utf-8\r\nContent-Length: 11680\r\n\r\niVBORw0KGgoAAAANSU'


def test_client_for_405_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GOT /index.html HTTP/1.1\r\nHost: www.example.com\\r\\n\\r\\n")
    assert response == 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'


def test_client_for_400_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET /index.html HTTP/1.1\r\nPost: www.example.com\\r\\n\\r\\n")
    assert response == 'HTTP/1.1 400 Bad Request\r\n\r\n'


def test_client_for_406_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET /index.html HTTP/1.0\r\nHost: www.example.com\\r\\n\\r\\n")
    assert response == 'HTTP/1.1 406 Not Acceptable\r\n\r\n'
