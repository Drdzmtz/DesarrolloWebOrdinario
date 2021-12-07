from certifi import where
import ssl

from functools import lru_cache
from geopy.geocoders import Nominatim, options


ctx = ssl.create_default_context(cafile=where())
options.default_ssl_context = ctx

geolocator = Nominatim(user_agent="ordinario_desarrollo_web", scheme= "http")

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

   @property
   @lru_cache(maxsize= 5, typed=False)
   def address(self) -> str:
      return geolocator.reverse(f"{self.longitude}, {self.latitude}").address

   def to_dict(self):
      return {
         "id":          self.id,
         "photo":       self.photo,
         "city":        self.city,
         "state":       self.state,
         "zip_code":    self.zip_code,
         "price":       self.price,
         "rooms":       self.rooms,
         "bathrooms":   self.bathrooms,
         "longitude":   self.longitude,
         "latitude":    self.latitude,
         "description": self.description,
         "status":      self.status,
         "type":        self.type,
      }