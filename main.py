from fastapi import FastAPI

from controller import actors, films

from fastapi.middleware.cors import CORSMiddleware

# In questa variabile ci sta l'istanza che tiene in piedi l'applicazione
app = FastAPI()

# Routers per gestire meglio l'esposizione dei servizi
app.include_router(films.router)
app.include_router(actors.router)


# CORSMiddleware, ci permette di effettuare chiamate a questo BE da altri sistemi
# app.add_middleware(
    # CORSMiddleware,
    # allow_origin_regex="http://.*",
    # allow_credentials=True,
    # allow_methods=["*"],
    # allow_headers=["*"],
# )
