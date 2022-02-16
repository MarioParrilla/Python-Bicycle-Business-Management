from model import Category

class Maintenance:

    def __init__(self, date: str, price: float, description: str, category: Category):
        self.date = date
        self.price = price
        self.description = description
        self.category = category