from strings import hello


def test_hello():
    assert hello("Bostone") == "hello, Bostone"


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Ochieng") == "hello, Ochieng"
    for name in ["Kevin", "Victor", "Rhemney"]:
        assert hello(name) == f"hello, {name}"
