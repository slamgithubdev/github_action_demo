#test
from app import greet

def test_greet():
    """Testing."""
    result = greet("Steven")
    assert result == "Hello, Steven!"

    result = greet("Blah")
    assert result == "Hello, Blah!"