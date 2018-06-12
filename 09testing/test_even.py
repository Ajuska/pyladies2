from even import is_even

def test_even():
    assert is_even(2)
    assert is_even(4)
    assert is_even(0)
    assert is_even(2232986)

def test_odd():
    assert not is_even(3)
    assert not is_even(7)
    assert not is_even(-1)
    assert not is_even(398345)
