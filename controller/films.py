from fastapi import APIRouter
from dto.filmDto import FilmDTO

router = APIRouter(prefix="/films", tags=["films"])


@router.get('')
def getAllFilms():
    return {"films": FilmDTO.getAllFilms()}
