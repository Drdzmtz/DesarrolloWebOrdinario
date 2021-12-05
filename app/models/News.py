class News():
    
     def __init__(self, **kwargs):
        self.id:int            = kwargs.get("id",            -1)
        self.title:str         = kwargs.get("title",         "")
        self.description:str   = kwargs.get("description",   "")