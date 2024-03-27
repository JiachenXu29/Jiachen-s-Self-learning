from hello import hello



def test_argument():
    assert hello("Jason") == "hello, Jason"

def test_default():
    for name in ["Jason", "Jack", "Dick"]:
        assert hello(name) == f"hello, {name}"
