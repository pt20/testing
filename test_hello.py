import pytest
from hello import print_hello_world 


def test_print_hello_world(capsys):
    captured = capsys.readouterr()
    # expected = "hello world!"
    result = print_hello_world()
    
    assert captured.out == result
