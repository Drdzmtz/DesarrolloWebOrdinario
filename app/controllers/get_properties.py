from app.models.House_dal import House_dal

def get_by_id(db:House_dal, id:int):
    res = db.get_by_id(id)

    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return res

def get_all(db:House_dal):
    res = db.get_all()
    
    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return res

def get_with_filter(db:House_dal, args:dict):
    res = db.get_with_filters(args)
    
    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return res    

def get_properties(id:int = -1, args:dict = {}):
    db = House_dal()
    
    if id != -1:
        return get_by_id(db, id)

    if len(args) != 0:
        return get_with_filter(db, args)

    return get_all(db)