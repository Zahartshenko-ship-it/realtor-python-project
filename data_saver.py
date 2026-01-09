def save_apartments(apartments, filename):
    """Сохраняет список квартир в CSV-файл (без кавычек, без запятых в адресе)"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("address,rooms,total_area,living_area,floor,total_floors,owner,price\n")
        for apt in apartments:
            line = (f"{apt.address},"
                    f"{apt.rooms},"
                    f"{apt.total_area},{apt.living_area},"
                    f"{apt.floor},{apt.total_floors},"
                    f"{apt.owner},"
                    f"{apt.price}\n"
            )
            f.write(line)
