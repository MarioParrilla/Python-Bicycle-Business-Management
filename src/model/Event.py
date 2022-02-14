
class Event:
    def __init__(self, date: str, maxDate: str, location: str, province: str, organizer: str, totalKM: float, 
                price: float):
        self.date = date
        self.maxDate = maxDate
        self.location = location
        self.province = province
        self.organizer = organizer
        self.totalKM = totalKM
        self.price = price
        self.eventPartners = None

    def parseToJSON(self): 
        jsonObject = {
            'date': self.date,
            'maxDate': self.maxDate,
            'location': self.location,
            'province': self.province,
            'organizer': self.organizer,
            'totalKM': self.totalKM,
            'price': self.price,
            'eventPartners': self.eventPartners,
        }
        return jsonObject