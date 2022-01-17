
class Bicyclette:

    def __init__(self, buyDate: str, brandName: str, model: str, price: float, type: str, color: str,
                    bikeFrameSize: float, wheelSize: float, maintenance: list):
        self.buyDate = buyDate
        self.brandName = brandName
        self.model = model
        self.price = price
        self.type = type
        self.color = color
        self.bikeFrameSize = bikeFrameSize
        self.wheelSize = wheelSize
        self.maintenance = maintenance