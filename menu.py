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

def input_new_apartment():
    # ... (ваша текущая реализация без изменений)
    try:
        print("\n--- Добавление новой квартиры ---")
        address = input("Адрес: ").strip()
        if not address:
            print("Адрес не может быть пустым.")
            return None
        rooms = input("Количество комнат: ").strip()
        total_area = input("Общая площадь (м²): ").strip()
        living_area = input("Жилая площадь (м²): ").strip()
        floor = input("Этаж: ").strip()
        total_floors = input("Всего этажей в доме: ").strip()
        owner = input("Собственник: ").strip()
        price = input("Цена (руб.): ").strip()

        fields = [rooms, total_area, living_area, floor, total_floors, owner, price]
        if any(not f for f in fields):
            print("Все поля обязательны для заполнения!")
            return None

        int(rooms)
        float(total_area)
        float(living_area)
        int(floor)
        int(total_floors)
        int(price)

        return {
            'address': address,
            'rooms': rooms,
            'total_area': total_area,
            'living_area': living_area,
            'floor': floor,
            'total_floors': total_floors,
            'owner': owner,
            'price': price
        }
    except ValueError:
        print("Ошибка: числовые поля должны содержать корректные числа.")
        return None

def select_apartment_to_delete(apartments):
    # ... (ваша текущая реализация без изменений)
    if not apartments:
        print("Нет квартир для удаления.")
        return None

    print("\n--- Удаление квартиры ---")
    for i, apt in enumerate(apartments, start=1):
        print(f"{i}. {apt}")

    try:
        choice = input("\nВведите номер квартиры для удаления (или 0 — отмена): ").strip()
        if choice == '0':
            return None
        idx = int(choice) - 1
        if 0 <= idx < len(apartments):
            return idx
        else:
            print("Неверный номер.")
            return None
    except ValueError:
        print("Введите число.")
        return None

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
            try:
                room_count = int(input("Количество комнат: "))
                result = report_by_room_count(apartments, room_count)
                print_apartments(result, f"Отчёт 2: {room_count}-комнатные")
            except ValueError:
                print('Ошибка: введите число.')

        elif choice == '4':
            try:
                min_p = int(input('Мин. цена: '))
                max_p = int(input('Макс. цена: '))
                if min_p < 0:
                    print()
                    print('===ОШИБКА===')
                    print('Цена не может быть отрицательной')
                    continue
                if min_p > max_p:
                    print()
                    print('===ОШИБКА===')
                    print('Мин. цена не может быть больше макс.')
                    continue
                result = report_by_price_range(apartments, min_p, max_p)
                print_apartments(result, f"Отчёт 3: от {min_p} до {max_p}")
            except ValueError:
                print("Ошибка: введите целые числа.")

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
                print(f"Удалена: {removed}")

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