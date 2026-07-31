from arithmetic_bcc4bd0e import add


def test_add_is_deliberately_wrong():
    """Fails on purpose: exercises the test-failure review path."""
    assert add(2, 2) == 5
