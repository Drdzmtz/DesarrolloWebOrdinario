from app.models.House_dal import House_dal

def update_properties(form:dict):
    db = House_dal()

    res = db.update_info_house(form)

    if not res.isnumeric():
        res = {"Error": res}
        return res
    
    return {"Success": f"Successfully updated house {res}"}

def patch_properties(form:dict):
    db = House_dal()

    id = form.get("id", -1)
    status = form.get("status", "")

    res = db.update_status_house(id, status)

    if not res.isnumeric():
        res = {"Error": res}
        return res
    
    return {"Success": f"Successfully changed status from house {res}"}

