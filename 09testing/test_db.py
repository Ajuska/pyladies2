# test_db.py
import pytest

def test_db(db):
    assert db.startswith('databaze')

##BEZ PARAMS
# def test_db2(db):
#     assert db == 'databaze ABC'

@pytest.fixture#(scope='module') --->zapne na zacaku, vypne na konci
def db(content):
    print('Zapinam databazi')
    yield 'databaze ' + content
    print('Vypinam databazi')

@pytest.fixture(params=['ABC', 'DEF'])
def content(request):
    return request.param
