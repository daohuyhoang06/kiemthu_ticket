import pytest
from ticket import calculate_ticket_price

# R1: Distance ≤ 500, Luggage ≤ 20
def test_TC1():
    assert calculate_ticket_price(400, 15) == 400*1000 + 0

# R2: Distance ≤ 500, Luggage 21–40
def test_TC2():
    assert calculate_ticket_price(450, 30) == 450*1000 + 30*20000

# R3: Distance ≤ 500, Luggage 41–50
def test_TC3():
    assert calculate_ticket_price(480, 45) == 480*1000 + 45*30000

# R4: Distance ≤ 500, Luggage > 50 (Invalid)
def test_TC4():
    with pytest.raises(ValueError):
        calculate_ticket_price(300, 55)

# R5: Distance 501–1500, Luggage ≤ 20
def test_TC5():
    assert calculate_ticket_price(1000, 20) == 1000*900 + 0

# R6: Distance 501–1500, Luggage 21–40
def test_TC6():
    assert calculate_ticket_price(1200, 30) == 1200*900 + 30*20000

# R7: Distance 501–1500, Luggage 41–50
def test_TC7():
    assert calculate_ticket_price(1400, 45) == 1400*900 + 45*30000

# R8: Distance 501–1500, Luggage > 50 (Invalid)
def test_TC8():
    with pytest.raises(ValueError):
        calculate_ticket_price(1500, 55)

# R9: Distance > 1500, Luggage ≤ 20
def test_TC9():
    assert calculate_ticket_price(1600, 10) == 1600*800 + 0

# R10: Distance > 1500, Luggage 21–40
def test_TC10():
    assert calculate_ticket_price(1800, 25) == 1800*800 + 25*20000

# R11: Distance > 1500, Luggage 41–50
def test_TC11():
    assert calculate_ticket_price(2000, 50) == 2000*800 + 50*30000

# R12: Distance > 1500, Luggage > 50 (Invalid)
def test_TC12():
    with pytest.raises(ValueError):
        calculate_ticket_price(1700, 55)
