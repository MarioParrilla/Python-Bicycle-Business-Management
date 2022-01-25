
#SE PUEDEN REALIZAR DOS EVENTOS O MAS EN EL MISMO DIA SI EL ORGANIZADOR NO TIENE UN EVENTO ORGANIZADO ESE MISMO DIA
class Event:
    def __init__(self, date: str, maxDate: str, location: str, province: str, organizer: str, totalKM: float, 
                price: float, eventPartners: list):
        self._date = date
        self._maxDate = maxDate
        self._location = location
        self._province = province
        self._organizer = organizer
        self._totalKM = totalKM
        self._price = price
        self._eventPartners = eventPartners