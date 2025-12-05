from app import greet, add, mul

def test_greet():
    assert greet("Stas") == "hi - Stas"

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(2, 5) == 10

def test_summ():
    assert summ(6, 3) == 2