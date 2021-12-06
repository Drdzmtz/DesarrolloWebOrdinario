from app.models.House_dal import House_dal
from app.models.House import House
from app.models.PDF import PDF

def generate_pdf(id:int):
    db = House_dal()
    res = db.get_by_id(id)

    if isinstance(res, str):
        res = {"Error": res}
        return res

    if len(res) == 0:
        return {"Error": f'Casa con id {id} no encontrada'}

    res = res["0"]
    house = House(
        id          = res["id"],
        photo       = res["photo"],
        city        = res["city"],
        state       = res["state"],
        zip_code    = res["zip_code"],
        price       = res["price"],
        rooms       = res["rooms"],
        bathrooms   = res["bathrooms"],
        longitude   = res["longitude"],
        latitude    = res["latitude"],
        description = res["description"],
        status      = res["status"],
        type        = res["type"],
    )
    
    pdf = PDF(house)
    res, err = pdf.generate_pdf()

    if err != "":
        return {"Success": False, "Error": err}

    return {"Success": True, "pdf": res}
        
