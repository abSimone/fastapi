import json
import numbers


class NumberService:

    @classmethod
    def getNumbers(cls):
        return { "numbers": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] }
