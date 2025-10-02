
# Đầu vào:
# distance (số km bay)
# luggage (trọng lượng hành lý ký gửi, kg)


# Quy tắc tính giá vé:
# Giá vé theo khoảng cách (áp dụng một mức giá duy nhất cho toàn bộ chặng bay):


# 0≤ distance ≤ 500 km → 1000 VND/km
# 50< distance ≤1500 km → 900 VND/km
# 1500 < distance ≤ 1663 km  → 800 VND/km
# Phí hành lý:


# 0≤ luggage ≤20 kg → miễn phí
# 20< luggage ≤40 kg → 20,000 VND/kg
# 40< luggage ≤50 kg→ 30,000 VND/kg
# >50 kg→ không chấp nhận

# Đầu ra: Tổng tiền vé = tiền khoảng cách + phí hành lý.


def calculate_ticket_price(distance, luggage):
    if distance < 0 or luggage < 0 or distance > 1663 or luggage > 50:
        return "Invalid"

    # Tính giá vé theo khoảng cách
    if distance <= 500:
        fare = distance * 1000
    elif distance <= 1500:
        fare = distance * 900
    elif distance <= 1663:
        fare = distance * 800
    
    # Tính phí hành lý
    if luggage <= 20:
        luggage_fee = 0
    elif luggage <= 40:
        luggage_fee = luggage * 20000
    elif luggage <= 50:
        luggage_fee = luggage * 30000

    return fare + luggage_fee



    