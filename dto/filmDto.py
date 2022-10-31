from dao.filmDao import FilmDAO


class Film:
    def __init__(self, title):
        self.title = title


class FilmDTO:
    @classmethod
    def getAllFilms(cls):
        data = FilmDAO.findAllFilms()
        newList = []
        for lista in data:
            newList.append(Film(lista[0].capitalize()))
        return newList
