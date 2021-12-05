from app.database import Database
from app.models.House import House

class House_dal():

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def get_by_id(self, id:int):

        query = f'''
        SELECT *
        FROM houses
        WHERE id = {id};
        '''

        self.cursor.execute(query)

        try:
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        properties = []
        for row in res:
            properties.append(
                House(
                    id       = row["id"],
                    photo    = row["photo"],
                    city     = row["city"],
                    state    = row["state"],
                    zip_code = row["zip_code"],
                    price    = row["price"],
                    rooms    = row["rooms"],
                    bathrooms = row["bathrooms"],
                    longitud = row["longitude"],
                    latitude = row["latitude"],
                    descript = row["description"],
                    status   = row["status"],
                    type     = row["type"],
                ).to_dict()
        )    

        res = {str(i):v for i,v in enumerate(properties)}

        return res

    def get_all(self):

        query = f'''
        SELECT *
        FROM houses;
        '''

        self.cursor.execute(query)

        try:
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        properties = []
        for row in res:
            properties.append(
                House(
                    id       = row["id"],
                    photo    = row["photo"],
                    city     = row["city"],
                    state    = row["state"],
                    zip_code = row["zip_code"],
                    price    = row["price"],
                    rooms    = row["rooms"],
                    bathrooms = row["bathrooms"],
                    longitud = row["longitude"],
                    latitude = row["latitude"],
                    descript = row["description"],
                    status   = row["status"],
                    type     = row["type"],
                ).to_dict()
        )    

        res = {str(i):v for i,v in enumerate(properties)}

        return res

