from Classes.client import Client

class Standardclient(Client):
    def __init__(self, id:int, name:str, contact:int,bookings:int ,email:str):
        super().__init__(id, name, contact,bookings,email)
         
    def __str__(self):
        return {"id": self.__id,
                "name": self.__name,
                "contact": self.__contact,
                "bookings": self.__bookings,
                "email": self.__email}