# data_saver.py

def save_apartments(apartments, filename):
    """Сохраняет список квартир в CSV-файл (без кавычек, без запятых в адресе)"""
    with open(filename, 'w', encoding='utf-8') as f:
        # Заголовок
        f.write("address,rooms,total_area,living_area,floor,total_floors,owner,price\n")
        for apt in apartments:
            line = f"{apt.address},{apt.rooms},{apt.total_area},{apt.living_area}," \
                   f"{apt.floor},{apt.total_floors},{apt.owner},{apt.price}\n"
            f.write(line)