from model import Category

class Maintenance:

    def __init__(self, date: str, price: float, description: str, category: Category):
        self._date = date
        self._price = price
        self._description = description
        self._category = category