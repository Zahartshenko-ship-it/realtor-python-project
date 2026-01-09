from models import Apartment


def load_apartments(filename: str) -> list:
    apartments = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Будет создан при первом сохранении.")
        return []
    for line_num, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) != 8:
            print(f"Пропущена строка {line_num}: неверное количество полей ({len(parts)} вместо 8)")
            continue

        try:
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
        except (ValueError, TypeError) as e:
            print(f"Пропущена строка {line_num}: ошибка данных — {e}")
            continue

    print(f"Загружено {len(apartments)} квартир из '{filename}'.")
    return apartments
