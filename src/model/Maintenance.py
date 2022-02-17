from src.model.Category import Category

class Maintenance:

    def __init__(self, date: str, price: float, description: str, category: Category):
        self.date = date
        self.price = price
        self.description = description
        self.category = category

    def __str__(self):
        return  f"Fecha: {self.date}\nPrecio: {self.price}\nDescripcion: {self.description}\nCategoria: {self.category}"

    def parseToJSON(self): 
            c = ''
            if(self.category == Category.WHEELS): c = 'wheels'

            elif(self.category == Category.BRAKES): c = 'brakes'

            elif(self.category == Category.SEAT): c = 'seat'

            elif(self.category == Category.BIKEFRAME): c = 'bikeframe'

            elif(self.category == Category.FRONT): c = 'front'

            elif(self.category == Category.BACK): c = 'back'

            elif(self.category == Category.OTHERS): c = 'others'

            jsonObject = {
                'date': self.date,
                'price': self.price,
                'description': self.description,
                'category': c,
            }
            return jsonObject