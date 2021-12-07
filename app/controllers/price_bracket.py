from app.models.House_dal import House_dal

def price_bracket():
    db = House_dal()

    res = db.price_bracket()
    
    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    res = res['0']

    labels = {f"price_label{i+1}": f'"{v}"' for i, v in enumerate(res.keys())}
    prices = {f"price_data{i+1}": [v] for i, v in enumerate(res.values())}

    data = dict(labels, **prices)

    print(data)

    return {"data": data}    
