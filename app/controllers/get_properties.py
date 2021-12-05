import json

from app.database import Database


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

    return json.dumps(res)