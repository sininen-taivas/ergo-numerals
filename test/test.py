import pytest

from vlq import encode


def test_encode11():
    res = encode(100000)
    assert res == '05c09a0c'


def test_encode12():
    res = encode(500)
    assert res == '05e807'


def test_encode13():
    res = encode(-666)
    assert res == '05b30a'
