from App.Generator.LinkGenerator import generateLink
from App.Database.Database import saveData, getData, updateClicks


def generateShortUrl():
    code = generateLink()
    short_link = f"http://localhost:8000/redirect/{code}"
    return short_link, code



def saveDataService(code, originalLink,encurtedLink):
    saveData(code, originalLink, 0, encurtedLink)




def locateDataOnDb(code):
    return getData(code)


def updateClicksOnDb(code):
    return updateClicks(code)