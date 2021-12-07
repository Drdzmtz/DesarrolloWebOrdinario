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

    
    def update_info_house(self, form:dict):

        house = House(
            id=             form.get("id", -1),
            photo=          form.get("photo", ""),
            city=           form.get("city", ""),
            state=          form.get("state", ""),
            zip_code=       form.get("zip_code", ""),
            price=          form.get("price", ""),
            rooms=          form.get("rooms", -1),
            bathrooms=      form.get("bathrooms", -1),
            longitude=      form.get("longitude", -1.0),
            latitude=       form.get("latitude", -1.0),
            description=    form.get("description", ""),
            status=         form.get("status", ""),
            type=           form.get("type", ""),
        )

        query = f'''
        UPDATE houses 
        SET 
        photo        = '{house.photo}'        ,
        city         = '{house.city}'         ,
        state        = '{house.state}'        ,
        zip_code     = '{house.zip_code}'     ,
        price        =  {house.price}         ,
        rooms        =  {house.rooms}         ,
        bathrooms    =  {house.bathrooms}     ,
        longitude    =  {house.longitude}     ,
        latitude     =  {house.latitude}      ,
        description  = '{house.description}'  ,
        status       = '{house.status}'       ,
        type         = '{house.type}' 
        WHERE id = {house.id};
        '''

        try:
            self.cursor.execute(query)
        except Exception as e: return str(e)
       
        self.db.client.commit()
        res = house.id
        
        return res
    
    def update_status_house(self, id, status):

        query = f'''
        UPDATE houses SET 
        status = '{status}'
        WHERE id = {id};
        '''

        try:
            self.cursor.execute(query)
        except Exception as e: return str(e)

        self.db.client.commit()
        res = id

        return res
    
    def insert_house(self, form:dict, filename:str):

        house = House(
            photo=          filename,
            city=           form.get("city", ""),
            state=          form.get("state", ""),
            zip_code=       form.get("zip_code", ""),
            price=          form.get("price", ""),
            rooms=          form.get("rooms", -1),
            bathrooms=      form.get("bathrooms", -1),
            longitude=      form.get("longitude", -1.0),
            latitude=       form.get("latitude", -1.0),
            description=    form.get("description", ""),
            status=         form.get("status", ""),
            type=           form.get("type", ""),
        )

        query = f'''
        INSERT INTO houses 
        (photo, city, state, zip_code, price, rooms, bathrooms, 
        longitude, latitude, description, status, type) 
        VALUES (
            "{house.photo}", 
            "{house.city}", 
            "{house.state}", 
            "{house.zip_code}", 
            {house.price}, 
            {house.rooms}, 
            {house.bathrooms}, 
            {house.longitude}, 
            {house.latitude}, 
            "{house.description}", 
            "{house.status}", 
            "{house.type}"
            );
        '''

        try:
            self.cursor.execute(query)
        except Exception as e: return str(e)
       
        self.db.client.commit()
        res:int = self.cursor.rowcount
        
        return res