
#SE PUEDEN REALIZAR DOS EVENTOS O MAS EN EL MISMO DIA SI EL ORGANIZADOR NO TIENE UN EVENTO ORGANIZADO ESE MISMO DIA
class Event:
    def __init__(self, date: str, maxDate: str, location: str, province: str, organizer: str, totalKM: float, 
                price: float, eventPartners: list):
        self.date = date
        self.maxDate = maxDate
        self.location = location
        self.province = province
        self.organizer = organizer
        self.totalKM = totalKM
        self.price = price
        self.eventPartners = eventPartners