from dao.filmDao import FilmDAO
from models.film import FilmVO


class FilmDTO:
    @classmethod
    def getAllFilms(cls):
        data = FilmDAO.findAllFilms()
        newList = []
        for lista in data:
            newList.append(FilmVO(lista[0].capitalize()))
        return newList
