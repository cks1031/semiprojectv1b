from http.client import responses

from pydantic import BaseModel


class NewGallery(BaseModel):
    userid: str
    title: str
    contents: str
    captcha : str