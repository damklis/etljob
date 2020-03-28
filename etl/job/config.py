from datetime import timedelta, date


class ETLConfig:

    PARSER = "lxml"

    TIMEDELTA = 30

    _departure = date.today().strftime("%d.%m.%Y")
    _arrival = (date.today() + timedelta(days=TIMEDELTA)).strftime("%d.%m.%Y")

    URL = "http://www.azair.com/azfin.php"
    
    PARAMS = {
        "tp" : 0,
        "searchtype" : "flexi",
        "srcAirport" : "Krakow+[KRK]+(%2BKTW)",
        "srcTypedText" : "krak",
        "srcFreeTypedText":"",
        "srcMC" : "",
        "srcap0" : "KTW",
        "srcFreeAirport" : "",
        "dstAirport" : "Anywhere+[XXX]",
        "dstTypedText" : "any",
        "dstFreeTypedText" : "",
        "dstMC" : "",
        "adults" : 1,
        "depdate" : f"{_departure}",
        "arrdate" : f"{_arrival}",
        "minDaysStay" : 3,
        "maxDaysStay" : 7,
        "currency" : "PLN",
        "maxChng" : 1,
        "isOneway" : "return"
    }

    CHUNK_SIZE = 20

    DB_NAME = "flights_db"
