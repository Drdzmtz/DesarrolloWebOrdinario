from app.models.News_dal import News_dal

def news_get_properties(db:News_dal):
    res = db.get_last_3
    
    if isinstance(res, str):
        res = {"Error": res}
        return res
    
    return res