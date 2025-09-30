
# Bài toán: Tính giá vé máy bay
# - Đầu vào:
#     + distance: số km bay
#     + luggage: trọng lượng hành lý ký gửi (kg), tối đa 50kg
# - Quy tắc:
#     + Giá vé theo khoảng cách (toàn chặng 1 mức giá duy nhất):
#         <= 500 km       -> 1000 VND/km
#         501–1500 km     -> 900 VND/km
#         > 1500          -> 800 VND/km
#     + Phí hành lý:
#         <= 20 kg        -> miễn phí
#         21–40 kg        -> 20,000 VND/kg
#         41–50 kg        -> 30,000 VND/kg
#         > 50 kg         -> không chấp nhận
# - Đầu ra:
#     + Tổng giá vé = giá theo khoảng cách + phí hành lý

def calculate_ticket_price(distance, luggage):
    if distance < 0 or luggage < 0 or luggage > 50:
        raise ValueError("Invalid input values")

    # Tính giá vé theo khoảng cách
    if distance <= 500:
        fare = distance * 1000
    elif distance <= 1500:
        fare = distance * 900
    else:
        fare = distance * 800

    # Tính phí hành lý
    if luggage <= 20:
        luggage_fee = 0
    elif luggage <= 40:
        luggage_fee = luggage * 20000
    else:  # 41–50 kg
        luggage_fee = luggage * 30000

    return fare + luggage_fee



    