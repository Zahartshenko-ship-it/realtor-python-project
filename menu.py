from models import Apartment
from data_loader import load_apartments
from data_saver import save_apartments
from reports import (
    report_all_by_rooms_and_price,
    report_by_room_count,
    report_by_price_range
)


def print_apartments(apartments, title):
    print(f"\n=== {title} ===")
    if not apartments:
        print("Нет данных.")
    else:
        for apt in apartments:
            print(apt)


def input_int(
        prompt: str,
        min_value: int = None,
        error_msg: str = "Введите целое число."
) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"===ОШИБКА===\n{error_msg}")
                print("============")
                continue
            return value
        except ValueError:
            print("===ОШИБКА===\nВведите корректное целое число.")
            print("============")


def input_float(
        prompt: str,
        min_value: float = None,
        error_msg: str = "Значение должно быть положительным."
) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value is not None and value <= min_value:
                print(f"===ОШИБКА===\n{error_msg}")
                print("============")
                continue
            return value
        except ValueError:
            print("===ОШИБКА===\nВведите корректное число.")
            print("============")


def input_new_apartment():
    print("\n--- Добавление новой квартиры ---")

    street_house = input("Улица и номер дома (например: Ленина 10): ").strip()
    while not street_house:
        print("===ОШИБКА===\nУлица и номер дома обязательны!")
        print("============")
        street_house = input("Улица и номер дома (например: Ленина 10): ").strip()

    apt_number = input("Номер квартиры (например: 45): ").strip()
    while not apt_number:
        print("===ОШИБКА===\nНомер квартиры обязателен!")
        print("============")
        apt_number = input("Номер квартиры (например: 45): ").strip()

    address = f"{street_house} кв{apt_number}"

    rooms = input_int(
        "Количество комнат: ",
        min_value=1,
        error_msg="Количество комнат должно быть положительным числом.")
    total_area = input_float(
        "Общая площадь (м²): ",
        min_value=0,
        error_msg="Общая площадь должна быть положительной.")

    while True:
        living_area = input_float(
            "Жилая площадь (м²): ",
            min_value=0,
            error_msg="Жилая площадь должна быть положительной.")
        if living_area > total_area:
            print("===ОШИБКА===\nЖилая площадь не может быть больше общей площади.")
            print("============")
            continue
        break

    while True:
        floor = input_int(
            "Этаж: ",
            min_value=1,
            error_msg="Этаж должен быть положительным числом.")
        total_floors = input_int(
            "Всего этажей в доме: ",
            min_value=1,
            error_msg="Количество этажей в доме должно быть положительным.")
        if floor > total_floors:
            print("===ОШИБКА===\nЭтаж квартиры не может быть выше общего количества этажей в доме.")
            print("============")
            continue
        break

    owner = input("Собственник: ").strip()
    while not owner:
        print("===ОШИБКА===\nСобственник обязателен!")
        print("============")
        owner = input("Собственник: ").strip()

    price = input_int(
        "Цена (руб.): ",
        min_value=0,
        error_msg="Цена не может быть отрицательной.")

    return {
        'address': address,
        'rooms': str(rooms),
        'total_area': str(total_area),
        'living_area': str(living_area),
        'floor': str(floor),
        'total_floors': str(total_floors),
        'owner': owner,
        'price': str(price)
    }


def select_apartment_to_delete(apartments):
    if not apartments:
        print("Нет квартир для удаления.")
        return None

    print("\n--- Удаление квартиры ---")
    for i, apt in enumerate(apartments, start=1):
        print(f"{i}. {apt}")
    while True:
        try:
            choice = input("\nВведите номер квартиры для удаления (или 0 — отмена): ").strip()
            if choice == '0':
                return None
            idx = int(choice) - 1
            if 0 <= idx < len(apartments):
                return idx
            else:
                print("\n===ОШИБКА===\nНеверный номер\n============")
                return None
        except ValueError:
            print("\n===ОШИБКА===\nЧисло введено некорректно\n============")


def run_menu(apartments, filename):
    """Основной цикл меню. Принимает список квартир и имя файла."""
    while True:
        print("\n=== Риэлтерское агентство ===")
        print("1. Показать все квартиры")
        print("2. Отчёт: все (комнаты ↓, цена ↑)")
        print("3. Отчёт: по количеству комнат")
        print("4. Отчёт: по диапазону цен")
        print("5. Добавить квартиру")
        print("6. Удалить квартиру")
        print("0. Сохранить и выйти")

        choice = input("\nВыберите пункт: ").strip()

        if choice == '1':
            print_apartments(apartments, "Все квартиры")

        elif choice == '2':
            result = report_all_by_rooms_and_price(apartments)
            print_apartments(result, "Отчёт 1: Все квартиры")

        elif choice == '3':
            while True:
                try:
                    room_count = int(input("Количество комнат: "))
                    while room_count <= 0:
                        print('===ОШИБКА===\nЧисло комнат не может быть <= 0')
                        print('============')
                        room_count = int(input("\nКоличество комнат: "))
                    result = report_by_room_count(apartments, room_count)
                    print_apartments(result, f"Отчёт 2: {room_count}-комнатные")
                    break
                except ValueError:
                    print('===ОШИБКА===\nЧисло введено некорректно')
                    print('============')

        elif choice == '4':
            while True:
                try:
                    min_p = int(input('Мин. цена: '))
                    while min_p < 0:
                        print('===ОШИБКА===\nЦена не может быть отрицательной')
                        print('============')
                        min_p = int(input('Мин. цена: '))
                        continue
                    max_p = int(input('Макс. цена: '))
                    if min_p > max_p:
                        print('===ОШИБКА===\nМин. цена не может быть больше макс.')
                        print('============')
                        continue
                    result = report_by_price_range(apartments, min_p, max_p)
                    print_apartments(result, f"Отчёт 3: от {min_p} до {max_p}")
                    break
                except ValueError:
                    print("===ОШИБКА===\nЧисло введено некорректно")
                    print('============')

        elif choice == '5':
            data = input_new_apartment()
            if data:
                new_apt = Apartment(**data)
                apartments.append(new_apt)
                print("Квартира добавлена.")

        elif choice == '6':
            idx = select_apartment_to_delete(apartments)
            if idx is not None:
                removed = apartments.pop(idx)
                print(f"\nУдалена: {removed}")

        elif choice == '0':
            try:
                save_apartments(apartments, filename)
                print("Данные сохранены. Выход.")
                break
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
                if input("Всё равно выйти без сохранения? (y/n): ").lower() == 'y':
                    break
        else:
            print("Неверный выбор.")
