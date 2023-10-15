from Classes.bill import Bill
from Classes.booking import Booking
import mysql.connector

DELETE_SUCCESS = {"message": "eliminacion completa"}
class DatabaseControllerBokings():

    """
    This class is used to connect to the database and execute queries
    """
    def __init__(self):
        """
        Constructor
        """
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
    def insert_booking(self, booking: Booking):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        if booking.type_flight =="standart class":
            self.cursor.execute("""SELECT * FROM data_base.standart_class WHERE ID= %s""", (booking.id_flight,))
            flight = self.cursor.fetchone()
            if flight and flight[4]>=booking.cant_positions:
                if booking.type_client == "standart client":
                    self.cursor.execute("""SELECT * FROM data_base.Offers WHERE Id_flight= %s AND 
                    Type_client = 'standart client'""", (booking.id_flight,))
                    offer = self.cursor.fetchone()
                    if not offer:
                        discount = 0.0 
                    else:
                        discount = float(offer[2])
                    self.cursor.execute("""SELECT * FROM data_base.standart_client WHERE ID= %s""", (booking.id_client,))
                    client = self.cursor.fetchone()
                    if client:                      
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        self.cursor.execute(
                        """UPDATE data_base.standart_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        self.connection.commit()
                        client_new_bookings = client[3] + 1 
                        self.cursor.execute(
                        """UPDATE data_base.standart_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        self.connection.commit()
                        new_cost_position = price_position - (price_position * discount/100)
                        self.cursor.execute('''INSERT INTO data_base.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))
                        self.connection.commit()
                        bookingj = {
                        "cant_position":booking.cant_positions,
                        "Id_flight": booking.id_flight,
                        "Id_client": booking.id_client,
                        "Type_flight": booking.type_flight,
                        "Type_client": booking.type_client,
                        "Cost_position": new_cost_position,
                        }     
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                    
                elif booking.type_client == "premium client":
                    self.cursor.execute("""SELECT * FROM data_base.Offers WHERE Id_flight= %s AND 
                                Type_client = 'premium client'""", (booking.id_flight,))
                    offer = self.cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    self.cursor.execute("""SELECT * FROM data_base.premium_client WHERE ID= %s""", (booking.id_client,))
                    client = self.cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        self.cursor.execute(
                        """UPDATE data_base.standart_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        self.connection.commit()
                        client_new_bookings =client[3]+ 1
                        self.cursor.execute(
                        """UPDATE data_base.premium_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        self.connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        self.cursor.execute('''INSERT INTO data_base.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        )) 
                        self.connection.commit()  
                        bookingj = {
                        "cant_position":booking.cant_positions,
                        "Id_flight": booking.id_flight,
                        "Id_client": booking.id_client,
                        "Type_flight": booking.type_flight,
                        "Type_client": booking.type_client,
                        "Cost_position":new_cost_position,
                        }  
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                else:
                    return{"error":"tipo de cliente no encontrado"}               
            else:
                return{"error":"vuelo no disponible"} 
              
        elif(booking.type_flight =="firts class"):
            self.cursor.execute("""SELECT * FROM data_base.firts_class WHERE ID= %s""", (booking.id_flight,))
            flight = self.cursor.fetchone()
            if flight and flight[4]>=booking.cant_positions:
                if booking.type_client == "standart client":
                    self.cursor.execute("""SELECT * FROM data_base.Offers WHERE Id_flight= %s AND 
                    Type_client = 'standart client'""", (booking.id_flight,))
                    offer = self.cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    self.cursor.execute("""SELECT * FROM data_base.standart_client WHERE ID= %s""", (booking.id_client,))
                    client = self.cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions= flight[4] - booking.cant_positions
                        self.cursor.execute(
                        """UPDATE data_base.firts_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        self.connection.commit()
                        client_new_bookings = client[3] + 1
                        self.cursor.execute(
                        """UPDATE data_base.standart_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        self.connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        self.cursor.execute('''INSERT INTO data_base.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))   
                        self.connection.commit()
                        bookingj = {
                        "cant_position":booking.cant_positions,
                        "Id_flight": booking.id_flight,
                        "Id_client": booking.id_client,
                        "Type_flight": booking.type_flight,
                        "Type_client": booking.type_client,
                        "Cost_position":new_cost_position,
                        }        
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                    
                elif booking.type_client == "premium client":
                    self.cursor.execute("""SELECT * FROM data_base.Offers WHERE Id_flight= %s AND 
                                Type_client = 'premium client'""", (booking.id_flight,))
                    offer = self.cursor.fetchone()
                    if not offer:
                        discount = 0 
                    else:
                        discount = offer[2]
                    self.cursor.execute("""SELECT * FROM data_base.premium_client WHERE ID= %s""", (booking.id_client,))
                    client = self.cursor.fetchone()
                    if client:                    
                        price_position = flight[7]
                        flight_new_positions = flight[4] - booking.cant_positions
                        self.cursor.execute(
                        """UPDATE data_base.firts_class SET
                        Positions=%s
                        WHERE id = %s""",
                        (
                        flight_new_positions,
                        flight[0],
                        ),
                        )
                        self.connection.commit()
                        client_new_bookings= client[3] + 1
                        self.cursor.execute(
                        """UPDATE data_base.premium_client SET
                        Bookings=%s
                        WHERE id = %s""",
                        (
                        client_new_bookings,
                        client[0],
                        ),
                        )
                        self.connection.commit()
                        new_cost_position = price_position - price_position * (discount/100)
                        self.cursor.execute('''INSERT INTO data_base.bookings(
                        Cant_positions,
                        Id_flight,
                        Id_client,
                        Type_flight,
                        Type_client,
                        Cost_position
                        ) VALUES (%s, %s, %s, %s, %s, %s )''',
                        (   
                        booking.cant_positions,
                        booking.id_flight,
                        booking.id_client,
                        booking.type_flight,
                        booking.type_client,
                        new_cost_position,
                        ))
                        self.connection.commit()                        
                        bookingj = {
                        "cant_position":booking.cant_positions,
                        "Id_flight": booking.id_flight,
                        "Id_client": booking.id_client,
                        "Type_flight": booking.type_flight,
                        "Type_client": booking.type_client,
                        "Cost_position":new_cost_position,
                        }  
                        return bookingj
                    else:
                        return{"error":"el cliente que realiza la reserva no se ha encontrado"}
                else:
                    return{"error":"tipo de cliente no encontrado"}               
            else:
                return{"error":"vuelo no disponible"} 
        
        else:
            return{"error":"tipo de vuelo no encontrado"}
          
    def edit_booking(self, cant_position:int, id_booking:int):
        self.cursor.execute("""SELECT * FROM data_base.Bookings WHERE ID= %s""", (id_booking,))
        booking = self.cursor.fetchone()
        if booking:
            if booking[4] == "standart class":
                self.cursor.execute("""SELECT * FROM data_base.standart_class  WHERE ID= %s""", (booking[2],))
                flight = self.cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                if flight_old_position > cant_position:
                    flight_new_position = flight_old_position - cant_position
                    self.cursor.execute(
                    """UPDATE data_base.standart_class SET
                    Positions=%s
                    WHERE id = %s""",
                    (
                    flight_new_position,
                    flight[0],
                    ),
                    )
                    print(cant_position)
                    self.connection.commit()
                    self.cursor.execute(
                    """UPDATE data_base.bookings SET
                    Cant_positions=%s
                    WHERE id = %s""",
                    (
                    cant_position,
                    booking[0],
                    ),
                    )
                    self.connection.commit()
                    bookingj = {
                    "Cant_position": cant_position,
                    "Id_flight": booking[2],
                    "Id_client": booking[3],
                    "Type_flight": booking[4],
                    "Type_client": booking[5],
                    "Cost_position": booking[6]
                    }  
                    return bookingj
                else:
                    return {"error": "cantidad de puestos no disponibles" }
            else:
                self.cursor.execute("""SELECT * FROM data_base.firts_class  WHERE ID= %s""", (booking[2],))
                flight = self.cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                if flight_old_position > cant_position:
                    flight_new_position = flight_old_position - cant_position
                    self.cursor.execute(
                    """UPDATE data_base.firts_class SET
                    Positions=%s
                    WHERE id = %s""",
                    (
                    flight_new_position,
                    flight[0],
                    ),
                    )
                    self.connection.commit()
                    self.cursor.execute(
                    """UPDATE data_base.bookings SET
                    Cant_positions=%s
                    WHERE id = %s""",
                    (
                    cant_position,
                    booking[0],
                    ),
                    )
                    self.connection.commit()
                    bookingj = {
                    "Cant_position": cant_position,
                    "Id_flight": booking[2],
                    "Id_client": booking[3],
                    "Type_flight": booking[4],
                    "Type_client": booking[5],
                    "Cost_position": booking[6]
                    }  
                    return bookingj
                else:
                    return {"error": "cantidad de puestos no disponibles" }
        else:
            return{"error":"reserva no encontrada"}
    
    def delete_booking(self, id:int):
        self.cursor.execute("""SELECT * FROM data_base.Bookings WHERE ID= %s""", (id,))
        booking = self.cursor.fetchone()
        if booking:
            if booking[4] == "standart class":
                self.cursor.execute("""SELECT * FROM data_base.standart_class WHERE ID= %s""", (booking[2],))
                flight = self.cursor.fetchone()
                flight_new_position = flight[4] + booking[1]
                self.cursor.execute(
                """UPDATE data_base.standart_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                self.connection.commit()
                if booking[5] == "standart client":
                    self.cursor.execute("""SELECT * FROM data_base.standart_client WHERE ID= %s""", (booking[3],))
                    client = self.cursor.fetchone()
                    client_new_booking = client[3] - 1
                    self.cursor.execute(
                    """UPDATE data_base.standart_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    self.connection.commit()
                else:
                    self.cursor.execute("""SELECT * FROM data_base.firts_client WHERE ID= %s""", (booking[3],))
                    client = self.cursor.fetchone()
                    client_new_booking = client[3] - 1
                    self.cursor.execute(
                    """UPDATE data_base.premium_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    self.connection.commit()
            else:
                self.cursor.execute("""SELECT * FROM data_base.firts_class WHERE ID= %s""", (booking[2],))
                flight = self.cursor.fetchone()
                flight_old_position = flight[4] + booking[1]
                flight_new_position = flight_old_position - booking[1]
                self.cursor.execute(
                """UPDATE data_base.firts_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                self.connection.commit()
                self.cursor.execute(
                """UPDATE data_base.firts_class SET
                Positions=%s
                WHERE id = %s""",
                (
                flight_new_position,
                flight[0],
                ),
                )
                self.connection.commit()
                if booking[5] == "standart client":
                    self.cursor.execute("""SELECT * FROM data_base.standart_client WHERE ID= %s""", (booking[3],))
                    client = self.cursor.fetchone()
                    client_new_booking = client[3] - 1
                    self.cursor.execute(
                    """UPDATE data_base.standart_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    self.connection.commit()
                else:
                    self.cursor.execute("""SELECT * FROM data_base.firts_client WHERE ID= %s""", (booking[3],))
                    client = self.cursor.fetchone()
                    client_new_booking = client[3] - 1
                    self.cursor.execute(
                    """UPDATE data_base.premium_client SET
                    bookings=%s
                    WHERE id = %s""",
                    (
                    client_new_booking,
                    client[0],
                    ),
                    )
                    self.connection.commit()
                
            self.cursor.execute("""DELETE FROM data_base.Bookings WHERE ID= %s""", (id,))
            self.connection.commit()
            return DELETE_SUCCESS
        else:
            return{"error":"reserva no encontrada"}
                    
    def show_booking(self):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM data_base.bookings')
        rows = self.cursor.fetchall()      
        return rows 
    
    def show_bill(self, id_booking:int, payment_method:str):
        self.connection = mysql.connector.connect(user='ian', password='ian1234', host='localhost', database='data_base', port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""SELECT * FROM data_base.bookings WHERE ID= %s""", (id_booking,))
        booking = self.cursor.fetchone() 
        if booking:
            total_cost = booking[6] * booking[1]
            bill = Bill(id_booking, total_cost, id_booking, payment_method)
            return bill.__str__()  
        else:
            return {"error": "Reserva no encontrada"}