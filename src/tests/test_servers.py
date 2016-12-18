# # -*- coding: utf-8 -*-
"""Test client socket with various messages."""

def test_response_ok(""):
    """Test response_ok."""
    from server import response_ok
    result = response_ok()
    assert result == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_client_for_ok_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
    assert response == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_client_for_405_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GOT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")
    assert response == 'HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_client_for_400_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET /index.html HTTP/1.1\r\nPost: www.example.com\r\n\r\n")
    assert response == 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_client_for_406_response():
    """Test for ok response from server with empty message."""
    from client import create_client_socket
    response = create_client_socket("GET /index.html HTTP/1.0\r\nHost: www.example.com\r\n\r\n")
    assert response == 'HTTP/1.1 406 Not Acceptable\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'

