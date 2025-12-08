from abramovapp import greet, add, mul, popsa

def test_greet():
    assert greet("Stas") == "hi - Stas"

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(2, 5) == 10

def test_sumb():
    assert popsa(6, 3) == 2