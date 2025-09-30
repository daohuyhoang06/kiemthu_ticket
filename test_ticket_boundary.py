import pytest
from ticket import calculate_ticket_price

# Biên khoảng cách
def test_TC1():
    assert calculate_ticket_price(500, 25) == 500*1000 + 25*20000

def test_TC2():
    assert calculate_ticket_price(501, 25) == 501*900 + 25*20000

def test_TC3():
    assert calculate_ticket_price(1500, 25) == 1500*900 + 25*20000

def test_TC4():
    assert calculate_ticket_price(1501, 25) == 1501*800 + 25*20000

# Biên hành lý
def test_TC5():
    assert calculate_ticket_price(1000, 20) == 1000*900 + 0

def test_TC6():
    assert calculate_ticket_price(1000, 21) == 1000*900 + 21*20000

def test_TC7():
    assert calculate_ticket_price(1000, 40) == 1000*900 + 40*20000

def test_TC8():
    assert calculate_ticket_price(1000, 41) == 1000*900 + 41*30000

def test_TC9():
    assert calculate_ticket_price(1000, 50) == 1000*900 + 50*30000

def test_TC10():
    assert calculate_ticket_price(1000, 51) == 1000*900 + 51*30000
