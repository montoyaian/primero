from Classes.standart_client import Standardclient
from Classes.premium_client import PremiumClient
from Classes.offers import Offer
import mysql.connector
from mysql.connector import Error

DELETE_SUCCESS = {"message": "eliminacion completa"}
class DatabaseControllerClient():
    """
    This class is used to connect to the database and execute queries
    """

    def __init__(self):
        """
        Constructor
        """
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        
    def insert_client(self, client: Standardclient or PremiumClient):
    
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
       
        if isinstance(client,Standardclient):
            self.cursor.execute('''INSERT INTO data_base.standart_client(
            Name,
            Contact,
            Bookings,
            Email
            ) VALUES (%s, %s, %s, %s )''',
            (   
            client.name,
            client.contact,
            client.bookings,
            client.email
            ))
            self.connection.commit()
            clientj = {
            "name": client.name,
            "contact": client.contact,
            "bookings": 0,
            "email": client.email,
            }
            return clientj

        elif isinstance(client,PremiumClient):
            self.cursor.execute('''INSERT INTO data_base.premium_client(
            Name,
            Contact,
            Bookings,
            Email
            ) VALUES (%s, %s, %s, %s )''',
            (   
            client.name,
            client.contact,
            client.bookings,
            client.email
            ))
            self.connection.commit()
            self.connection.close()
            clientj = {
            "name": client.name,
            "contact": client.contact,
            "bookings": client.bookings,
            "email": client.email,
            }
            return clientj

    def insert_offer(self, offer:Offer):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        if offer.flight_type == "standart class":
            self.cursor.execute(
            """SELECT * FROM data_base.standart_class WHERE id = %s""",
            (offer.id_flight,),
            )
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("""INSERT INTO data_base.Offers(
                Id_flight,
                Discount,
                Customer_type,
                Flight_type
                ) VALUES (%s, %s, %s, %s)""",
                (
                offer.id_flight,
                offer.discount,
                offer.customer_type,
                offer.flight_type
                ))
                self.connection.commit()
                self.connection.close()
                offerj = {
                    "Id_flight":offer.id_flight,
                    "Discount":offer.discount,
                    "Customer_type":offer.customer_type,
                    "Flight_type":offer.flight_type
                    }
                return offerj
            else:
                return{"error": "id de vuelo no encotrado"}
            
        elif offer.flight_type == "firts class":
            self.cursor.execute(
            """SELECT * FROM data_base.firts_class WHERE id = %s""",
            (offer.id_flight,),
            )
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute(      """INSERT INTO  data_base.Offers(
                Id_flight,
                Discount,
                Customer_type,
                Flight_type
                ) VALUES (%s, %s, %s, %s)""",
                (
                offer.id_flight,
                offer.discount,
                offer.customer_type,
                offer.flight_type
                ))
                self.connection.commit()
                self.connection.close()
                offerj = {
                    "Id_flight":offer.id_flight,
                    "Discount":offer.discount,
                    "Customer_type":offer.customer_type,
                    "Flight_type":offer.flight_type
                    }
                return offerj
            else:
                return{"error": "id de vuelo no encotrado"} 
        else:
            return{"error": "tipo de vuelo no encotrado"}       
        
    def edit_client(self, client):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        if isinstance(client, Standardclient):
            self.cursor.execute(
            """SELECT * FROM data_base.standart_client WHERE id = %s""",
            (client.id,),
        )
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("""UPDATE data_base.standart_client SET 
                Name = %s,
                Contact = %s,
                Bookings = %s,
                Email = %s
                WHERE ID = %s""",
                (
                client.name,
                client.contact,
                client.bookings,
                client.email,
                client.id
                ))
                self.connection.commit()
                self.connection.close()
                clientj = {
                "name": client.name,
                "contact": client.contact,
                "bookings": client.bookings,
                "email": client.email,
                }
                return clientj
            else:
                return{"error": "cliente no encontrado"}
        elif isinstance(client, PremiumClient):
            self.cursor.execute(
            """SELECT * FROM data_base.premium_client WHERE id = %s""",
            (client.id,),
        )
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("""UPDATE data_base.premium_client SET 
                Name = %s,
                Contact = %s,
                Bookings = %s,
                Email = %s
                WHERE ID = %s""",
                (
                client.name,
                client.contact,
                client.bookings,
                client.email,
                client.id
                ))
                self.connection.commit()
                self.connection.close()
                clientj = {
                "name": client.name,
                "contact": client.contact,
                "bookings": client.bookings,
                "email": client.email,
                }
                return clientj
            else:
                return{"error": "cliente no encontrado"}

    def edit_offer(self,offer:Offer):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
        """SELECT * FROM data_base.Offers WHERE id = %s""",
        (offer.id,),
        )
        result = self.cursor.fetchone()
        if result:
            if offer.flight_type == "standart class":
                self.cursor.execute(
                """SELECT * FROM data_base.standart_class WHERE id = %s""",
                (offer.id_flight,),
                )
                result = self.cursor.fetchone()
                if result:
                    self.cursor.execute("""UPDATE data_base.Offers SET
                    Id_flight = %s,
                    Discount = %s,
                    Customer_type = %s,
                    Flight_type = %s
                    WHERE id = %s""",
                    (
                    offer.id_flight,
                    offer.discount,
                    offer.customer_type,
                    offer.flight_type,
                    offer.id
                    ))
                    self.connection.commit()
                    self.connection.close()
                    offerj = {
                        "ID":offer.id,
                        "Id_flight":offer.id_flight,
                        "Discount":offer.discount,
                        "Customer_type":offer.customer_type,
                        "Flight_type":offer.flight_type
                        }
                    return offerj
                else:
                    return{"error": "id de vuelo no encotrado"}            
            elif offer.flight_type == "firts class":
                self.cursor.execute(
                """SELECT * FROM data_base.firts_class WHERE id = %s""",
                (offer.id_flight,),
                )
                result = self.cursor.fetchone()
                if result:
                    self.cursor.execute(      """UPDATE data_base.Offers SET
                    Id_flight = %s,
                    Discount = %s,
                    Customer_type = %s,
                    Flight_type = %s
                    WHERE id = %s""",
                    (
                    offer.id_flight,
                    offer.discount,
                    offer.customer_type,
                    offer.flight_type,
                    offer.id
                    ))
                    self.connection.commit()
                    self.connection.close()
                    offerj = {
                        "ID":offer.id,
                        "Id_flight":offer.id_flight,
                        "Discount":offer.discount,
                        "Customer_type":offer.customer_type,
                        "Flight_type":offer.flight_type
                        }
                    return offerj
                else:
                    return{"error": "id de vuelo no encotrado"} 
            else:
                return{"error": "tipo de vuelo no encotrado"}            
        else:
            return{"error": "reserva no encontrada"}  
                   
    def delete_client(self, id: int, client_type: str):
        """
        Delete a client from database
        """
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        client_type.lower()
        if (client_type == "premium client"):
            self.cursor.execute("""SELECT * FROM data_base.premium_client WHERE ID = %s """,(id,))
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("""DELETE FROM data_base.premium_client  WHERE id = %s""", (id,))
                self.connection.commit()
                self.cursor.execute("""SELECT * FROM data_base.bookings WHERE Id_client = %s AND Type_client = 'premium client' """,(id,))
                rows = self.cursor.fetchall()
                for  booking in rows:  
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
                    else:
                        self.cursor.execute("""SELECT * FROM data_base.firts_class WHERE ID= %s""", (booking[2],))
                        flight = self.cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]
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
                self.cursor.execute("""DELETE FROM data_base.bookings  WHERE id_client = %s AND Type_client = 'premium client'""", (id,))
                self.connection.commit()
                self.connection.close()
                return DELETE_SUCCESS
            else:
                return{"error":"cliente no encontrado"}
                            
        elif (client_type == "standart client"):
            self.cursor.execute("""SELECT * FROM data_base.standart_client WHERE ID = %s """,(id,))
            result = self.cursor.fetchone()
            if result:
                self.cursor.execute("""DELETE FROM data_base.standart_client WHERE id = %s""", (id,))
                self.connection.commit()
                self.cursor.execute("""SELECT * FROM data_base.bookings WHERE Id_client = %s AND Type_client = 'standart client' """,(id,))
                rows = self.cursor.fetchall()
                for  booking in rows:  
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
                    else:
                        self.cursor.execute("""SELECT * FROM data_base.firts_class WHERE ID= %s""", (booking[2],))
                        flight = self.cursor.fetchone()
                        flight_new_position = flight[4] + booking[1]
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
                self.cursor.execute("""DELETE FROM data_base.bookings  WHERE Id_client = %s AND Type_client = 'standart client'""", (id,))
                self.connection.commit()
                self.connection.close()
                return DELETE_SUCCESS
            else:
                return{"error":"cliente no encontrado"}
        else:
            return {"error":"cliente no encontrado"}
        
    def delete_offer(self, id:int):
        """
        Delete a offer from database
        """
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
        """SELECT * FROM data_base.Offers WHERE id = %s""",
        (id,),
        )
        result = self.cursor.fetchone()
        if result:
            self.cursor.execute("""DELETE FROM data_base.Offers  WHERE id = %s""", (id,))
            self.connection.commit()
            self.connection.close()
            return DELETE_SUCCESS   
        else:
            return {"error":"oferta no encontrada"} 
    
    def show_client(self, table_name:str):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        try:
            if table_name == "all":
                self.cursor.execute('SELECT * FROM data_base.standart_client')
                rows = self.cursor.fetchall()
                self.cursor.execute('SELECT * data_base.FROM premium_client')
                rows += self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return rows 
            else:
                self.cursor.execute(
                    '''SELECT * FROM data_base.{}'''.format(table_name))
                rows = self.cursor.fetchall()
                self.connection.commit()
                self.connection.close()
                return rows
        except Error as e:
            return{"error":"tabla no valida"}      

    def show_offer(self):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM data_base.Offers')
        rows = self.cursor.fetchall()      
        return rows         
    
    def premium_clients(self):
        self.connection = mysql.connector.connect(user='ian',password='ian1234',host='localhost',database='data_base',port='3306')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
        """SELECT * FROM data_base.standart_client WHERE Bookings >= %s""",
        (4,),
        )
        for row in self.cursor.fetchall():
            self.cursor.execute(
            """INSERT INTO  data_base.premium_client(
            Name,
            Contact,
            Bookings,
            Email
            ) VALUES (%s, %s, %s, %s )""",
            (
            row[1], # Name
            row[2], # Contact
            row[3], # Bookings
            row[4], # Email
            ))
            self.cursor.execute("""DELETE FROM data_base.standart_client WHERE id = %s""", (row[0],))
            self.connection.commit()
        self.cursor.execute(
        """SELECT * FROM data_base.premium_client WHERE Bookings  < %s""",
        (4,),
        )
        for row in self.cursor.fetchall():
            self.cursor.execute(
            """INSERT INTO  data_base.standart_client(
            Name,
            Contact,
            Bookings,
            Email
            ) VALUES (%s, %s, %s, %s )""",
            (
            row[1], # Name
            row[2], # Contact
            row[3], # Bookings
            row[4], # Email
            ))
            self.cursor.execute("""DELETE FROM data_base.premium_client WHERE id = %s""", (row[0],))
            self.connection.commit()
        self.cursor.execute('SELECT * FROM data_base.premium_client')
        rows = self.cursor.fetchall()
        self.connection.close()
        return(rows)            

 
        