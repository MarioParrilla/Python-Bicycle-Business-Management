
class Bicyclette:

    def __init__(self, buyDate: str, brandName: str, model: str, price: float, type: str, color: str,
                    bikeFrameSize: float, wheelSize: float, maintenance: list):
        self._buyDate = buyDate
        self._brandName = brandName
        self._model = model
        self._price = price
        self._type = type
        self._color = color
        self._bikeFrameSize = bikeFrameSize
        self._wheelSize = wheelSize
        self._maintenance = maintenance