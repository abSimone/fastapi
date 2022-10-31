from dao.actorDao import ActorDao


class Actor:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


class ActorDTO:

    @classmethod
    def getAllActors(cls):
        data = ActorDao.findAllActors()
        newList = []
        for lista in data:
            newList.append(Actor(lista[0].capitalize(), lista[1].capitalize()))
        return newList

    @classmethod
    def getActorsForFilm(cls, titolo_film: str):
        data = ActorDao.findFirstNameAndLastnameByFilmTitle(titolo_film)
        newList = []
        for lista in data:
            newList.append(Actor(lista[0].capitalize(), lista[1].capitalize()))
        return newList
