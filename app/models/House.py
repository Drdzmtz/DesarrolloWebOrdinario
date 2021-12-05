class House():
    
     def __init__(self, **kwargs):
        self.id:int            = kwargs.get("id",            -1)
        self.photo:str         = kwargs.get("photo",         "")
        self.city:str          = kwargs.get("city",          "")
        self.state:str         = kwargs.get("state",         "")
        self.zip_code:str      = kwargs.get("zip_code",      "")
        self.price:int         = kwargs.get("price",         -1)
        self.rooms:int         = kwargs.get("rooms",         -1)
        self.bathrooms:int     = kwargs.get("bathrooms",     -1)
        self.longitude:str     = kwargs.get("longitude",     "")
        self.latitude:str      = kwargs.get("latitude",      "")
        self.description:str   = kwargs.get("description",   "")
        self.status:str        = kwargs.get("status",        "")
        self.type:str          = kwargs.get("type",          "")