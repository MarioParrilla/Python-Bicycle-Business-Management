
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

    def __str__(self):
        s = f"Organizador: {self.organizer}\nFecha: {self.date}\nFecha Maxima Inscripcion: {self.maxDate}\nLocalidad: {self.location}/{self.province}\nLongitud: {self.totalKM}\nPrecio: {self.price}\nSocios Apuntados:\n"
        if(self.eventPartners == None): s = s+"Nadie"
        else: 
            for p in self.eventPartners: s = s+p+'\n'
        
        return  s

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