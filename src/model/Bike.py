
class Bike:

    def __init__(self, buyDate: str, brandName: str, model: str, price: float, typeBike: str, color: str,
                    bikeFrameSize: float, wheelSize: float):
        self.buyDate = buyDate
        self.brandName = brandName
        self.model = model
        self.price = price
        self.typeBike = typeBike
        self.color = color
        self.bikeFrameSize = bikeFrameSize
        self.wheelSize = wheelSize
        self.maintenance = None


    def __str__(self):
        return  f"Fecha de Compra: {self.buyDate}\nMarca: {self.brandName}\nModelo: {self.model}\nPrecio: {self.price}\nColor: {self.color}\nPrecio: {self.price}\nTamaño del Cuadro: {self.bikeFrameSize}\nTamaño de rueda: {self.wheelSize}"

    def parseToJSON(self): 
        jsonObject = {
            'buyDate': self.buyDate,
            'brandName': self.brandName,
            'model': self.model,
            'price': self.price,
            'typeBike': self.typeBike,
            'color': self.color,
            'bikeFrameSize': self.bikeFrameSize,
            'wheelSize': self.wheelSize,
            'maintenance': self.maintenance
        }
        return jsonObject