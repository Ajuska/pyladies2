# test_isholiday.py

##python -m pytest ==run test from the forlder
##python -m pytest -v ==extended log(verbous)
## -s == chova se jak v pythonu, bez toho se print vypise jen u FAILED TEST

import isholiday
import pytest

def test_xmas_2016():
    holidays = isholiday.getholidays(2016)
    assert (24, 12) in holidays

def test_no_holiday():
    holidays = isholiday.getholidays(2016)
    assert (3, 9) not in holidays

def test_xmas_2017():
    holidays = isholiday.getholidays(2017)
    assert (24, 12) in holidays

@pytest.mark.parametrize('year', range(2016, 2030))
def test_xmas(year):
    holidays = isholiday.getholidays(year)
    print('Rok je', year)
    assert (24, 12) in holidays

@pytest.mark.parametrize(['year', 'month', 'day'],
    [
        (2015, 12, 24),
        (2016, 12, 24),
        (2033, 1, 1),
        (2017, 7, 5),
        (2017, 7, 6),
    ]
)
def test_some_holidays(year, month, day):
    holidays = isholiday.getholidays(year)
    assert (day, month) in holidays
