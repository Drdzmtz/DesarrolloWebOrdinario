import mysql.connector
from typing import List

from app.config import DBUSERNAME, DBPASSWORD, DBNAME, DBHOST

def singleton(class_):
    instances = {}

    def get_instance():
        if class_ not in instances:
            instances[class_] = class_()

        return instances[class_]

    return get_instance

@singleton
class Database():
    
    def __init__(self):
        self.client = mysql.connector.connect(
            host=      DBHOST,
            user=      DBUSERNAME,
            password=  DBPASSWORD,
            database=  DBNAME,
        )

        self.cursor = self.client.cursor()
    
    def process_query_result(self, cursor) -> List[dict]:        
        desc = cursor.description
        
        return [dict(zip([col[0] for col in desc], row)) 
                for row in cursor.fetchall()]