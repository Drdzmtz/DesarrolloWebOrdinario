from typing import Dict

from app.database import Database
from app.models.User import User

class User_dal():

    def __init__(self):
        self.db = Database()
        self.cursor = self.db.cursor

    def get_all(self):

        query = f'''
        SELECT *
        FROM users;
        '''

        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        users:User = []
        for row in res:
            users.append(
                User(
                    id=         row["id"],
                    username=   row["username"],
                    password=   row["password"],
                    email=      row["email"],
                ).to_dict()
        )    

        res:Dict[str, User] = {str(i):v for i,v in enumerate(users)}

        return res

    def login(self, form:dict):

        user = form.get("username", "")
        pwd = form.get("password", "")

        query = f'''
        SELECT username
        FROM users
        WHERE username = "{user}"
        AND `password` = MD5("{pwd}");
        '''

        try:
            self.cursor.execute(query)
            res = self.db.process_query_result(self.cursor)
        except Exception as e: return str(e)

        if len(res) == 0:
            return "Usuario o contraseña incorrectos"

        res = res[0]

        return res