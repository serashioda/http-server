# # -*- coding: utf-8 -*-
"""Test client socket with various messages."""

body_content = 'I am a body content.'
content_type = 'text/plain'


def test_response_ok():
    """Test response_ok when request is valid."""
    from server import response_ok
    result = response_ok(body_content, content_type)
    assert result == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 20\r\n\r\n\r\nI am a body content.'


def test_response_error():
    """Test response_error when request is invalid."""
    from server import response_error
    result = response_error('406')
    assert result == 'HTTP/1.1 406 Not Acceptable\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_parse_request():
    """Test that uri is returned if request is valid."""
    from server import parse_request
    result = parse_request('GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
    assert result == '/index.html'

"""TODO:
** test response_error:
- test all error codes, and non-existing code (ie. 500), and when no error code passed in.

** test resolve_uri:
- 

**overall functionality tests

** parse_error convert to http
** client stops receiving @ end of message (when len(body_content) is reached)


# def test_client_for_405_response():
#     """Test for ok response from server with empty message."""
#     from client import create_client_socket
#     response = create_client_socket("GOT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
#     assert response == 'HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


# def test_client_for_400_response():
#     """Test for ok response from server with empty message."""
#     from client import create_client_socket
#     response = create_client_socket("GET /index.html HTTP/1.1\r\nPost: www.example.com\r\n\r\n")
#     assert response == 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


# def test_client_for_406_response():
#     """Test for ok response from server with empty message."""
#     from client import create_client_socket
#     response = create_client_socket("GET /index.html HTTP/1.0\r\nHost: www.example.com\r\n\r\n")
#     assert response == 'HTTP/1.1 406 Not Acceptable\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'
