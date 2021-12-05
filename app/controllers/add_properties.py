from app.models.House_dal import House_dal

def add_properties(form:dict):
    db = House_dal()

    res = db.insert_house(form)

    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return {"Success": f"Successfully added at row: {res}"}

