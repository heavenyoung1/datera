import random

def generate_id(
        hotel_id: str,
        room_id: str,
        check_in_date: tuple[int, int, int],
) -> str:
    
    YYYY, MM, DD = check_in_date
    random_digits = random.randrange(0, 99999)
    generated_id = f'{hotel_id}{room_id}AFX{YYYY}{MM:02}{DD:02}BTR{random_digits}'

    return  generated_id

print(generate_id('345', '32', (2025, 12, 1)))