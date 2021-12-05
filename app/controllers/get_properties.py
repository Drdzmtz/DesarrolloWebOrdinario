# from app.database import Database
# from app.models.House import House

# db = Database()
# cursor = db.cursor

from app.models.House_dal import House_dal

def get_properties(id:int = -1):
    
    db = House_dal()

    if id != -1:
        res = db.get_by_id(id)
        if isinstance(res, str):
            res = {0: res}

        return res

    res = db.get_all()
    if isinstance(res, str):
        res = {0: res}

        return res

    return res