import pytest
from ticket import calculate_ticket_price

import pytest
from ticket import calculate_ticket_price

@pytest.mark.parametrize(
    "distance,luggage,expected",
    [
        (400, 15, 400000),        # TC-R1
        (450, 30, 1050000),       # TC-R2
        (480, 45, 1830000),       # TC-R3
        (300, 55, "Invalid"),     # TC-R4
        (1000, 20, 900000),       # TC-R5
        (1200, 30, 1680000),      # TC-R6
        (1400, 45, 2610000),      # TC-R7
        (1500, 55, "Invalid"),    # TC-R8
        (1550, 10, 1240000),      # TC-R9
        (1600, 25, 1780000),      # TC-R10
        (1610, 50, 2788000),      # TC-R11
        (1660, 55, "Invalid"),    # TC-R12
    ]
)
def test_calculate_ticket_price(distance, luggage, expected):
    assert calculate_ticket_price(distance, luggage) == expected