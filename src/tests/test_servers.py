"""Test client socket in with various messages."""


def test_client():
    """."""
    import client 
    result = client.create_client_socket("apples are rotten.")
    assert result == "apples are rotten."




# messages shorter than one buffer in length
# messages longer than several buffers in length
# messages that are an exact multiple of one buffer in length
# messages containing non-ascii charactersc