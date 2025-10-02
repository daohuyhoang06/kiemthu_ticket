import pytest
from ticket import calculate_ticket_price

@pytest.mark.parametrize(
    "distance,luggage,expected",
    [
        (0, 25, 500000),       # TC1
        (1, 25, 501000),       # TC2
        (1662, 25, 1829600),   # TC3
        (1663, 25, 1830400),   # TC4
        (1664, 25, "Invalid"), # TC5
        (1000, 25, 1400000),   # TC6
        (1000, 0, 900000),     # TC7
        (1000, 1, 900000),     # TC8
        (1000, 49, 2370000),   # TC9
        (1000, 50, 2400000),   # TC10
        (1000, 51, "Invalid"), # TC11
    ]
)
def test_calculate_fare(distance, luggage, expected):
    assert calculate_ticket_price(distance, luggage) == expected