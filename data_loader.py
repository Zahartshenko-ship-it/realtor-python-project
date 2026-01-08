# data_loader.py
from models import Apartment

def load_apartments(filename: str) -> list:
    apartments = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Пропускаем заголовок
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 8:
            raise ValueError(f"Неверный формат строки: {line}")
        apartment = Apartment(
            address=parts[0],
            rooms=parts[1],
            total_area=parts[2],
            living_area=parts[3],
            floor=parts[4],
            total_floors=parts[5],
            owner=parts[6],
            price=parts[7]
        )
        apartments.append(apartment)
    return apartments