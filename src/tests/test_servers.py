# # -*- coding: utf-8 -*-
"""Test client socket with various messages."""


def test_response_ok():
    """Test response_ok."""
    from server import response_ok
    result = response_ok()
    assert result == 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


def test_response_error():
    """Test response error."""
    from server import response_error
    result = response_error()
    assert result == 'HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'


# def test_client():
#     """Test client with general message."""
#     import client
#     result = client.create_client_socket("apples are rotten.")
#     assert result == "apples are rotten."


# def test_client_send_empty():
#     """Test client with empty message."""
#     import client
#     result = client.create_client_socket("")
#     assert result == ""


# def test_client_send_eight():
#     """Test client with message of length 8."""
#     import client
#     result = client.create_client_socket("12345678")
#     assert result == "12345678"


# def test_client_send_mult_eight():
#     """Test client with message of length multiple of 8."""
#     import client
#     result = client.create_client_socket("thisissixteeeeen")
#     assert result == "thisissixteeeeen"


# def test_client_send_non_ascii():
#     """Test client with non ascii characters."""
#     import client
#     result = client.create_client_socket(u"non-ascii¡©")
#     assert result == u"non-ascii¡©"
