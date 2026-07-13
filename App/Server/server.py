from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.Routes.routes import routeApp
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =["*"],
    allow_methods =["*"],
    allow_credentials=True,
    allow_headers =["*"],

)

app.include_router(routeApp)