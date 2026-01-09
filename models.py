class Apartment:
    """Представляет квартиру в базе риэлторского агентства."""

    def __init__(
            self, address, rooms, total_area, living_area,
            floor, total_floors, owner, price
    ):
        self.address = address
        self.rooms = int(rooms)
        self.total_area = float(total_area)
        self.living_area = float(living_area)
        self.floor = int(floor)
        self.total_floors = int(total_floors)
        self.owner = owner
        self.price = int(price)

    def __repr__(self):
        return (
            f"{self.address} | {self.rooms}к | "
            f"этаж {self.floor}/{self.total_floors} | "
            f"{self.price} руб."
        )
