
class Fee:
    def __init__(self, year: int, lastPayment: str, isPaid: bool, feePrice: float, discount: float):
        self.year = year
        self.lastPayment = lastPayment
        self.isPaid = isPaid
        self.feePrice = feePrice
        self.discount = discount