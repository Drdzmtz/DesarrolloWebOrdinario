import re
from base64 import b64decode
from random import randint
from typing import List, Union
from datetime import datetime

from app.models.House_dal import House_dal
from app.config import UPLOADPATH

def extract_data(form:dict) -> List[Union[str, bytes]]:

    photo_data:str = form.get("photo", "")
    photo_data += "~"

    file_ending_pattern = '\/(\w*?)\;'
    content_pattern = '(?s),(.*?)~'

    file_re = re.search(file_ending_pattern, photo_data)
    content_re = re.search(content_pattern, photo_data)

    file_ending = file_re.group(1)
    photo_content = content_re.group(1)

    photo_bytes = b64decode(photo_content)
    
    return [file_ending, photo_bytes]

def unique_filename(file_ending:str) -> str:
    random_n_digits = lambda n: randint( 10**(n-1), 10**(n-1))
       
    filename = f"{datetime.now().date()}_{str(datetime.now().time()).replace(':', '.')}{random_n_digits(3)}"
    filename = f'{filename}.{file_ending}'

    return filename

def upload_photo(photo_bytes:bytes, filename:str) -> List[Union[bool, str]]:
    
    try:
        with open(f'{UPLOADPATH}{filename}', 'wb') as file:
            file.write(photo_bytes)
    except Exception as e:
        return [False, str(e)]

    return [True, ""]

def update_properties(form:dict):
    db = House_dal()

    file_ending, photo_bytes = extract_data(form)
    filename = unique_filename(file_ending)

    res = db.update_info_house(form, filename)

    if not res.isnumeric():
        res = {"Error": res}
        return res

    res, err = upload_photo(photo_bytes, filename)
    if not res:
        res = {"Error": err}
        return res
    
    return {"Success": f"Successfully updated house {res}"}

def patch_properties(form:dict):
    db = House_dal()

    id = form.get("id", -1)
    status = form.get("status", "")

    res = db.update_status_house(id, status)

    if not res.isnumeric():
        res = {"Error": res}
        return res
    
    return {"Success": f"Successfully changed status from house {res}"}

