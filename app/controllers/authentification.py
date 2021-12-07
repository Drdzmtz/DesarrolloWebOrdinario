from app.models.User import User
from app.models.User_dal import User_dal


def auth(form:dict):
    db = User_dal()

    res = db.login(form)

    if isinstance(res, str):
        res = {"Error": res}
        return res

    return {"Success": True, "username": res["username"]}