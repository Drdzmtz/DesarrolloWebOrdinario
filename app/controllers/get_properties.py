from app.database import Database
from app.models.House import House

db = Database()
cursor = db.cursor

def get_properties(id:int = -1):
    
    get_property = f'''
    SELECT *
    FROM houses
    WHERE id = {id};
    '''

    get_properties = f'''
    SELECT *
    FROM houses;
    '''

    query = get_properties if id == -1 else get_property
    cursor.execute(query)

    res = db.process_query_result(cursor)
    
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
                bathroom = row["bathrooms"],
                longitud = row["longitude"],
                latitude = row["latitude"],
                descript = row["description"],
                status   = row["status"],
                type     = row["type"],
            ).to_dict()
        )    

    res = {str(i):v for i,v in enumerate(properties)}

    return res