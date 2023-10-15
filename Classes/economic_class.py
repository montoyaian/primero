from Classes.flight import Flight
from datetime import date

class Economiclass(Flight):
    def __init__(self, id:int, origin:str, destination:str, date:date, positions:int, hour:int, id_agency:int, economic_cost:int):
        super().__init__(id, origin, destination, date, positions, hour, id_agency)
        self.__economic_cost = economic_cost
        
    @property
    def economic_cost(self):
        return self.__economic_cost
    @economic_cost.setter
    def economic_cost(self, new_economic_cost):
        self.__economic_cost = new_economic_cost
        
    def __str__(self):
        return {"id": self.id,
                "origin": self.origin,
                "destination": self.destination,
                "date": self.date,
                "positions": self.positions,
                "hour": self.hour,
                "id_agency": self.id_agency,
                "economic_cost": self.__economic_cost}