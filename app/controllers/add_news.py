from app.models.News_dal import News_dal

def add_news(form:dict):
    db = News_dal()

    res = db.insert_news(form)

    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return {"Success": "Successfully added"}

