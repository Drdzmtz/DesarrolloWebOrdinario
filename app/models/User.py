class User():

    def __init__(self, **kwargs):
        self.id:int         =   kwargs.get("id", -1)
        self.username:str   =   kwargs.get("username", "")
        self.password:str   =   kwargs.get("password", "")
        self.email:str      =   kwargs.get("email", "")

    def to_dict(self):
        return {
            "id":           self.id,
            "username":     self.username,
            "password":     self.password,
            "email":        self.email,
        }