from fastapi import FastAPI
from numberDTO import NumberService

from numberDTO import NumberService

app = FastAPI()


@app.get("/")
async def getNumbers():
  return NumberService.getNumbers()