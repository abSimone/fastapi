from dao.utility.db import MySql

class FilmDAO:

  @classmethod
  def findAllFilms(cls):
    MySql.openConnection()
    MySql.query(
      "SELECT title \
       FROM film"
    )
    data = MySql.getResults()
    MySql.closeConnection()
    return data
    