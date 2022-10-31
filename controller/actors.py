from fastapi import APIRouter
from dto.actorDto import ActorDTO


router = APIRouter(prefix="/actors")


@router.get('')
def getAllActors():
    return {"actors": ActorDTO.getAllActors()}


@router.get('/{titolo_film}')
def getActorsForFilm(titolo_film: str):
    return {"actors": ActorDTO.getActorsForFilm(titolo_film)}
