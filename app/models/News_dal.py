from app.database import Database
from app.models.News import News

class News_dal():

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor
    
    def get_last_3(self):
        
        query = f'''
        SELECT *
        FROM news
        ORDER BY id DESC LIMIT 3;
        '''

        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        news = []
        for row in res:
            news.append(
                News(
                    id          = row["id"],
                    title       = row["title"],
                    description = row["description"],
                ).to_dict()
        )    

        if len(news) == 0:
            news.append(
                News(
                 title= "Sin Noticias",
                 description= "Lo mantendremos informado :)"   
                ).to_dict()
            )

        res = {str(i):v for i,v in enumerate(news)}

        return res
    
    def insert_news(self, form:dict):

        news = News(
            title=          form.get("title", ""),
            description=    form.get("description", ""),
        )

        query = f'''
        INSERT INTO news (title, description) 
        VALUES (
            "{news.title}", 
            "{news.description}"
            );
        '''
        try:
            self.cursor.execute(query)
        except Exception as e: return str(e)
       
        self.db.client.commit()
        res:int = self.cursor.rowcount
        
        return res
