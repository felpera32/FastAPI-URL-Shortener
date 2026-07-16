from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
from App.Validators.LinkValidator import linkValidator
from App.Service.Service import generateShortUrl, saveDataService, locateDataOnDb, updateClicksOnDb


routeApp = APIRouter()


@routeApp.post("/links")
def createLinks(body: linkValidator):
    dictBody = body.model_dump(mode="json")
    uncurtedLink = dictBody.get("link")
    encurtedUrl, code = generateShortUrl()
    saveDataService(code, uncurtedLink, encurtedUrl)
    return JSONResponse(status_code=201, content={
        "message": "Link Encurtado com sucesso",
        "Link": f"{encurtedUrl}",
        "att": dictBody
    })


@routeApp.get("/redirect/{code}")
def redirect(code: str):
    updateClicksOnDb(code)
    return RedirectResponse(url=locateDataOnDb(code))