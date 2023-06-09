from src.dbs import *
from fastapi import FastAPI

app = FastAPI()


############### TEST
@app.get("/")
def root():
    a = read_data("users")
    return a


@app.post("/add")
def proot(items: dict):
    collec = items["collec"]
    doc = items["doc"]
    data = items["data"]

    add_data(collec, doc, data)
    a = read_data("users", doc)
    return {"message": a}


@app.post("/delete")
def deletes(items: dict):
    collec = items["collec"]
    doc = items["doc"]

    delete_data(collec, doc)
    a = read_data("users")
    return {"message": a}


@app.post("/update")
def update(items: dict):
    collec = items["collec"]
    doc = items["doc"]
    field = items["field"]

    update_data(collec, doc, field)
    a = read_data(collec)
    return {"message": a}


###################### WORK

@app.get("/heatmap")
def heatmap():
    return


@app.get("/weather")
def weather():
    return


def fastapp():
    return app
