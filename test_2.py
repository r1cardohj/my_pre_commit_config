from core import add_one, sub_one


def test_add_one():
    assert add_one(1) == 2


def test_sub_one():
    assert sub_one(2) == 1


def test_error():
    assert 1 == 2
