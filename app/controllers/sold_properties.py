from app.models.House_dal import House_dal

def sold_properties():
    db = House_dal()

    res = db.sold_properties()
    
    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    res = res['0']
    labels = [i for i in res.keys()]
    data   = [i for i in res.values()]

    return {"labels": labels, "data": data}    