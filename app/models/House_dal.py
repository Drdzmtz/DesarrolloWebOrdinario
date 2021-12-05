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

        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        properties = []
        for row in res:
            properties.append(
                House(
                    id          = row["id"],
                    photo       = row["photo"],
                    city        = row["city"],
                    state       = row["state"],
                    zip_code    = row["zip_code"],
                    price       = row["price"],
                    rooms       = row["rooms"],
                    bathrooms   = row["bathrooms"],
                    longitude   = row["longitude"],
                    latitude    = row["latitude"],
                    description = row["description"],
                    status      = row["status"],
                    type        = row["type"],
                ).to_dict()
        )    

        res = {str(i):v for i,v in enumerate(properties)}

        return res

    def get_all(self):

        query = f'''
        SELECT *
        FROM houses;
        '''

        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        properties = []
        for row in res:
            properties.append(
                House(
                    id          = row["id"],
                    photo       = row["photo"],
                    city        = row["city"],
                    state       = row["state"],
                    zip_code    = row["zip_code"],
                    price       = row["price"],
                    rooms       = row["rooms"],
                    bathrooms   = row["bathrooms"],
                    longitude   = row["longitude"],
                    latitude    = row["latitude"],
                    description = row["description"],
                    status      = row["status"],
                    type        = row["type"],
                ).to_dict()
        )    

        res = {str(i):v for i,v in enumerate(properties)}

        return res

    def get_with_filters(self, args):

        query = f'''
        SELECT * 
        FROM houses
        WHERE  
             (city       IN       ("{args.get("city", "-1")}")      OR  "{args.get("city", "-1")}"      = "-1")  
        AND  (state      IN       ("{args.get("state", "-1")}")     OR  "{args.get("state", "-1")}"     = "-1") 
        AND  (zip_code   IN       ("{args.get("zip_code", "-1")}")  OR  "{args.get("zip_code", "-1")}"      = "-1")
        AND  (rooms      IN       ({args.get("rooms", 0)})          OR   {args.get("rooms", 0)}         =   0)
        AND  (bathrooms  IN       ({args.get("bathrooms", 0)})      OR   {args.get("bathrooms", 0)}     =   0)
        AND  (`type`     IN       ("{args.get("type", "-1")}")      OR  "{args.get("type", "-1")}"      = "-1")
        AND  (`status`   IN       ("{args.get("status", "-1")}")    OR  "{args.get("status", "-1")}"    = "-1")
        AND  (price      >=       {args.get("min_price", 0)}        OR   {args.get("min_price", 0)}     =   0) 
        AND  (price      <=       {args.get("max_price", 0)}        OR   {args.get("max_price", 0)}     =   0);
        '''
        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        properties = []
        for row in res:
            properties.append(
                House(
                    id          = row["id"],
                    photo       = row["photo"],
                    city        = row["city"],
                    state       = row["state"],
                    zip_code    = row["zip_code"],
                    price       = row["price"],
                    rooms       = row["rooms"],
                    bathrooms   = row["bathrooms"],
                    longitude   = row["longitude"],
                    latitude    = row["latitude"],
                    description = row["description"],
                    status      = row["status"],
                    type        = row["type"],
                ).to_dict()
        )    
        res = {str(i):v for i,v in enumerate(properties)}
        return res