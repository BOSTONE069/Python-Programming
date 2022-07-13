from strings import hello


def test_hello():
    assert hello("Bostone") == "hello, Bostone"


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Ochieng") == "hello, Ochieng"
