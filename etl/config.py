import datetime
from datetime import timedelta

TODAY = datetime.date(2020, 4, 4)
N_DAYS_LATER = datetime.date(2020, 4, 4) + timedelta(days=30)


class ETLConfig:

    _departure = TODAY.strftime("%d.%m.%Y")
    _arrival = N_DAYS_LATER.strftime("%d.%m.%Y")

    URL = "http://www.azair.com/azfin.php"
    
    PARAMS = {"tp" : 0,
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
    "isOneway" : "return"}