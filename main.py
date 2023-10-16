from fastapi import Depends, FastAPI, Response, status  
from fastapi.security import HTTPBearer
from datetime import date  
from controller.bd_controller_flight import DatabaseControllerFlight
from controller.bd_controller_clients import DatabaseControllerClient
from Classes.first_class import Firtsclass
from Classes.economic_class import Economiclass
from Classes.standart_class import Standartclass
from Classes.standart_client import Standardclient
from Classes.premium_client import PremiumClient
from Classes.booking import Booking
from Classes.offers import Offer
from Classes.supplier import Supplier
from controller.db_controller_bookings import DatabaseControllerBokings
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
bd_object_flights = DatabaseControllerFlight() 
bd_object_client = DatabaseControllerClient() 
bd_object_booking = DatabaseControllerBokings()

@app.post("/api/ADD/firtsclass")
async def add_firtsclass(origin:str ="origin", destination:str="destination", date:str = date.today(), 
                                            positions:int=1, hour:float=1, id_agency:int=1, premium_cost:int=1):
    """
    Add a firtsclass to database
    """
    return bd_object_flights.insert_flight(Firtsclass(id=id,origin =origin, destination=destination, date= date, 
                                            positions=positions, hour=hour, id_agency=id_agency, premium_cost=premium_cost))
@app.post("/api/ADD/offers")
async def add_offers(id_flight:int=1, discount:int=1, customer_type:str="customer type",flight_type:str="flight type"):
    """
    Add a offer to database
    """
    return bd_object_client.insert_offer(Offer(id=id, id_flight=id_flight, discount=discount, customer_type=customer_type, flight_type=flight_type))

@app.post("/api/ADD/supplier")
async def add_supplier(name:str="name", contact:int=0,description:str="description"):
    """
    Add a offer to database
    """
    return bd_object_flights.insert_supplier(Supplier(id=id, name=name, contact=contact,description=description))
        
@app.post("/api/ADD/standartclass")
async def add_standartclass(origin:str ="origin", destination:str="destination", date:str = date.today(), 
                                            positions:int=1, hour:float=1, id_agency:int=1, standart_cost:int=1):
    """
    Add a standart class to database
    """
    return bd_object_flights.insert_flight(Standartclass(id=id,origin =origin, destination=destination, date= date, 
                                            positions=positions, hour=hour, id_agency=id_agency, standart_cost=standart_cost))
    
@app.post("/api/ADD/standartclient")
async def add_standartclient(name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    Add a standart client to database
    """
    return bd_object_client.insert_client(Standardclient(id =id, name=name, contact= contact,bookings = bookings ,email= email))
    
@app.post("/api/ADD/premiumclient")
async def add_premiumtclient(name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    Add a premium client to database
    """
    return bd_object_client.insert_client(PremiumClient(id =id, name=name, contact= contact,bookings = bookings ,email= email))

@app.post("/api/ADD/booking")
def add_booking(cant_positions:int=1, id_flight:int=1, id_client:int=1,type_client:str="type client",type_flight:str="type flight"):
    """
    edit a standart client to database
    """ 
    return bd_object_booking.insert_booking(Booking(id=1, cant_positions=cant_positions, id_flight=id_flight, id_client=id_client,
                                            type_client=type_client, type_flight=type_flight, cost_position=0))

@app.put("/edit/standartclient")
def edit_client(id:int = 0,name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_client(Standardclient(id= id,name=name, contact=contact, bookings=bookings,email=email))

@app.put("/edit/booking")
def edit_booking(cant_position:int = 1 , id_booking:int = 1):
    """
    edit a standart client to database
    """ 
    return bd_object_booking.edit_booking(cant_position, id_booking)
@app.put("/api/edit/supplier")
async def add_supplier(id:int=1,name:str="name", contact:int=0,description:str="description"):
    """
    edit supplier to database
    """
    return bd_object_flights.edit_supplier(Supplier(id=id, name=name, contact=contact,description=description))

@app.put("/edit/premiumclient")
def edit_client(id:int = 0,name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_client(PremiumClient(id= id,name=name, contact=contact, bookings=bookings,email=email))

@app.put("/edit/offer")
def edit_offer(id:int = 0,id_flight:int=1, discount:int=1, customer_type:str="customer type",flight_type:str="flight type"):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_offer(Offer(id= id,id_flight=id_flight, discount=discount, customer_type=customer_type,flight_type=flight_type))

@app.put("/edit/firtsclass")
def edit_flight(id:int=1, origin:str="origin", destination:str="destintation", date:str = date.today(), positions:int=1, hour:float=1, id_agency:int=1, premium_cost:int=1):
    """
    edit a firtsclass to database
    """ 
    return bd_object_flights.edit_flight(Firtsclass(id= id,origin=origin, destination= destination, date =date, positions=positions, hour=hour, id_agency=id_agency, premium_cost=premium_cost))


@app.put("/edit/standartclass")
def edit_flight(id:int=1, origin:str="origin", destination:str="destintation", date:date =date.today(), positions:int=1, hour:float=1, id_agency:int=1, standart_cost:int=1):
    """
    edit a standartclass to database
    """ 
    return bd_object_flights.edit_flight(Standartclass(id= id,origin=origin, destination= destination, date = date, positions=positions, hour=hour, id_agency=id_agency, standart_cost=standart_cost))

@app.delete("/delete/flight")
def delete_flight(id:int = 1 , class_type:str = "flght type"):
    """
    delete a standartclass to database
    """ 
    return bd_object_flights.delete_flight(id= id, class_type=class_type)

@app.delete("/delete/client")
def delete_client(id:int = 1 , client_type:str = "client type"):
    """
    delete a standartclient to database
    """ 
    return bd_object_client.delete_client(id= id, client_type=client_type)

@app.delete("/delete/supplier")
def delete_supplier(id:int = 1):
    """
    delete a supplier to database
    """ 
    return bd_object_flights.delete_supplier(id= id)

@app.delete("/delete/booking")
def delete_booking(id:int = 1):
    """
    delete a bookings to database
    """ 
    return bd_object_booking.delete_booking(id= id)

@app.delete("/delete/offer")
def delete_offer(id:int = 1 ):
    """
    delete a standartclient to database
    """ 
    return bd_object_client.delete_offer(id= id)

@app.get("/get/clients")
def show_client(table_name:str = "table name"):
    """
     show clients
    """ 
    return bd_object_client.show_client(table_name=table_name)

@app.get("/get/flights")
def show_flight(table_name:str = "table name"):
    """
    show flights
    """ 
    return bd_object_flights.show_flight(table_name=table_name)

@app.get("/get/offers")
def show_offers():
    """
    show offers
    """ 
    return bd_object_client.show_offer()

@app.get("/get/bookings")
def show_bookings():
    """
    show bookings
    """ 
    return bd_object_booking-show_bookings()

@app.get("/get/premiumclient")
def show_premiumclient():
    """
    show premiums clients
    """ 
    return bd_object_client.premium_clients()

@app.get("/get/bill")
def show_bill(id_booking:int = 1,payment_method:str = "payment_method"):
    """
    show bill
    """ 
    return bd_object_booking.show_bill(id_booking=id_booking,payment_method=payment_method)
