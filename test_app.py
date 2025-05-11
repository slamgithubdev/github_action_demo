#testing
from app import greet_user

def test_greet():
    result = greet_user("Steven")
    assert result == "Hello, Steven!"

    result = greet_user("Blah")
    assert result == "Hello, Blah!"

    result = greet_user("New Guy")
    assert result == "Hello, New Guy!"


    