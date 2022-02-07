
class Fee:
    def __init__(self, year: int, lastPayment: str, isPaid: bool, feePrice: float, discount: float):
        self.year = year
        self.lastPayment = lastPayment
        self.isPaid = isPaid
        self.feePrice = feePrice
        self.discount = discount

    def parseToJSON(self): 
        jsonObject = {
            'year': self.year,
            'lastPayment': self.lastPayment,
            'isPaid': self.isPaid,
            'feePrice': self.feePrice,
            'discount': self.discount,
        }
        return jsonObject

    def __str__(self):
        return f'Ultimo pago: {self.lastPayment}\nEstado: {self.isPaid}\nPrecio: {self.feePrice}\nDescuento: {self.discount}'