
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