from hello import print_hello_world 


def test_print_hello_world():
    expected = "hello world!"
    result = print_hello_world()
    
    assert expected == result
