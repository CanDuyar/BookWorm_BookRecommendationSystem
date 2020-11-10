from src.interface1 import a


def test_a():
    assert a("MEET MY STAFF", "HORROR") == 0
    assert a("unknown_book", "unknown_book") == -1
    assert a("MEET MY STAFF", "unknown_type") == -1
    assert a("unknown_book", "HORROR") == 0
    assert a("unknown_book", "TRAVEL") == 0
    assert a("unknown_book", "CRIME") == 0
