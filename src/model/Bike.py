
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