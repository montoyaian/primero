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
from Security.SSO import *

app = FastAPI()
bd_object_flights = DatabaseControllerFlight() 
bd_object_client = DatabaseControllerClient() 
bd_object_booking = DatabaseControllerBokings()

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/api/ADD/firtsclass")
async def add_firtsclass(current_user: Annotated[User, Depends(get_current_active_user)],origin:str ="origin", destination:str="destination", date:str = date.today(), 
                                            positions:int=1, hour:float=1, id_agency:int=1, premium_cost:int=1):
    """
    Add a firtsclass to database
    """
    return bd_object_flights.insert_flight(Firtsclass(id=id,origin =origin, destination=destination, date= date, 
                                            positions=positions, hour=hour, id_agency=id_agency, premium_cost=premium_cost))

@app.post("/api/ADD/supplier")
async def add_supplier(current_user: Annotated[User, Depends(get_current_active_user)],name:str="name", contact:int=0,description:str="description"):
    """
    Add a offer to database
    """
    return bd_object_flights.insert_supplier(Supplier(id=id, name=name, contact=contact,description=description))
        
@app.post("/api/ADD/standartclass")
async def add_standartclass(current_user: Annotated[User, Depends(get_current_active_user)],origin:str ="origin", destination:str="destination", date:str = date.today(), 
                                            positions:int=1, hour:float=1, id_agency:int=1, standart_cost:int=1):
    """
    Add a standart class to database
    """
    return bd_object_flights.insert_flight(Standartclass(id=id,origin =origin, destination=destination, date= date, 
                                            positions=positions, hour=hour, id_agency=id_agency, standart_cost=standart_cost))
    
@app.post("/api/ADD/standartclient")
async def add_standartclient(current_user: Annotated[User, Depends(get_current_active_user)],name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    Add a standart client to database
    """
    return bd_object_client.insert_client(Standardclient(id =id, name=name, contact= contact,bookings = bookings ,email= email))
    
@app.post("/api/ADD/premiumclient")
async def add_premiumtclient(current_user: Annotated[User, Depends(get_current_active_user)],name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    Add a premium client to database
    """
    return bd_object_client.insert_client(PremiumClient(id =id, name=name, contact= contact,bookings = bookings ,email= email))

@app.put("/edit/standartclient")
def edit_client(current_user: Annotated[User, Depends(get_current_active_user)],id:int = 0,name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_client(Standardclient(id= id,name=name, contact=contact, bookings=bookings,email=email))

@app.put("/api/edit/supplier")
async def add_supplier(current_user: Annotated[User, Depends(get_current_active_user)],id:int=1,name:str="name", contact:int=0,description:str="description"):
    """
    edit supplier to database
    """
    return bd_object_flights.edit_supplier(Supplier(id=id, name=name, contact=contact,description=description))

@app.put("/edit/premiumclient")
def edit_client(current_user: Annotated[User, Depends(get_current_active_user)],id:int = 0,name:str="name", contact:int=0, bookings:int=0,email:str="email"):
    """
    edit a standart client to database
    """ 
    return bd_object_client.edit_client(PremiumClient(id= id,name=name, contact=contact, bookings=bookings,email=email))


@app.put("/edit/firtsclass")
def edit_flight(current_user: Annotated[User, Depends(get_current_active_user)],id:int=1, origin:str="origin", destination:str="destintation", date:str = date.today(), positions:int=1, hour:float=1, id_agency:int=1, premium_cost:int=1):
    """
    edit a firtsclass to database
    """ 
    return bd_object_flights.edit_flight(Firtsclass(id= id,origin=origin, destination= destination, date =date, positions=positions, hour=hour, id_agency=id_agency, premium_cost=premium_cost))


@app.put("/edit/standartclass")
def edit_flight(current_user: Annotated[User, Depends(get_current_active_user)],id:int=1, origin:str="origin", destination:str="destintation", date:date =date.today(), positions:int=1, hour:float=1, id_agency:int=1, standart_cost:int=1):
    """
    edit a standartclass to database
    """ 
    return bd_object_flights.edit_flight(Standartclass(id= id,origin=origin, destination= destination, date = date, positions=positions, hour=hour, id_agency=id_agency, standart_cost=standart_cost))

@app.delete("/delete/flight")
def delete_flight(current_user: Annotated[User, Depends(get_current_active_user)],id:int = 1 , class_type:str = "flght type"):
    """
    delete a standartclass to database
    """ 
    return bd_object_flights.delete_flight(id= id, class_type=class_type)

@app.delete("/delete/client")
def delete_client(current_user: Annotated[User, Depends(get_current_active_user)],id:int = 1 , client_type:str = "client type"):
    """
    delete a standartclient to database
    """ 
    return bd_object_client.delete_client(id= id, client_type=client_type)

@app.delete("/delete/supplier")
def delete_supplier(current_user: Annotated[User, Depends(get_current_active_user)],id:int = 1):
    """
    delete a supplier to database
    """ 
    return bd_object_flights.delete_supplier(id= id)



@app.get("/get/clients")
def show_client(current_user: Annotated[User, Depends(get_current_active_user)], table_name:str = "table name"):
    """
     show clients
    """ 
    return bd_object_client.show_client(table_name=table_name)

@app.get("/get/flights")
def show_flight(current_user: Annotated[User, Depends(get_current_active_user)],table_name:str = "table name"):
    """
    show flights
    """ 
    return bd_object_flights.show_flight(table_name=table_name)

@app.get("/get/premiumclient")
def show_premiumclient(current_user: Annotated[User, Depends(get_current_active_user)],):
    """
    show premiums clients
    """ 
    return bd_object_client.premium_clients()


