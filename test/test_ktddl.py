import pytest
from ticket import calculate_ticket_price

@pytest.mark.parametrize(
    "distance,luggage,expected",
    [
        # ---- DISTANCE ----
        (-100, 23, "Invalid"),     
        (300, 10, 300000),         
        (320, 11, 320000),           
        (1200, 10, 1080000),   
        (1100, 10, 990000),    
        (1600, 10, 1280000), 
        (400, 15, 400000),
        (1300, 10, 1170000),       
        (1610, 10, 1288000),      

        # ---- LUGGAGE ----
        (500, -10, "Invalid"),     
        (300, 10, 300000),        
        (200, 10, 200000),         
        (450, 35, 1150000),        
        (400, 30, 1000000),       
        (350, 46, 1730000),   
        (400, 30, 1000000),     
        (400, 47, 1810000),       

        # ---- FARE ----
        (300, 10, 300000),         
        (1200, 10, 1080000),       
        (1600, 10, 1280000),       

        # ---- LUGGAGE_FEE ----
        (300, 10, 300000),         
        (400, 30, 1000000),        
        (400, 45, 1750000),        

        # ---- TOTAL ----
        (300, 10, 300000),        
        (400, 30, 1000000),       
    ]
)
def test_calculate_ticket_price(distance, luggage, expected):
    assert calculate_ticket_price(distance, luggage) == expected
