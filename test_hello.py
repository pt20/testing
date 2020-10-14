from hello import print_hello_world 


def test_print_hello_world():
    expected_out = "hello damn world!"
    result = print_hello_world()
    
    assert expected_out == result
