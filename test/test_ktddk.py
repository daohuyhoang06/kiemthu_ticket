import pytest
from ticket import calculate_ticket_price


@pytest.mark.parametrize(
    "distance,luggage,expected",
    [
        (500,   55, "Invalid"),
        (1700,   40, "Invalid"),
        (400,   10,  400_000),
        (400,   35, 1_100_000),
        (400,   45, 1_750_000),
        (1000,   15,  900_000),
        (1000,   35, 1_600_000),
        (1000,   45, 2_250_000),
        (1600,   10, 1_280_000),
        (1600,   30, 1_880_000),
        (1600,   50, 2_780_000),
    ]
)
def test_calculate_ticket_price(distance, luggage, expected):
    assert calculate_ticket_price(distance, luggage) == expected