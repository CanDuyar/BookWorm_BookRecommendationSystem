from src.interface2 import a
def test_a():
    assert a("HORROR") == 0
    assert a("unknown_book") == -1
    assert a("CRIME") == 0
    assert a("TRAVEL") == 0