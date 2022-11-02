from pydantic import BaseModel


class FilmVO :
  def __init__(self, title) :
    self.title = title

class FilmModel(BaseModel):
  title : str
  length : int
  description : str
  rating: str
