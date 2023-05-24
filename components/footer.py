import dash
from dash import html
from db import database


def layout():
    db = database.DB()
    info = db.read_all("ver_tablas")

    resp = [
        html.A([
            html.I(i[1]),
            html.Span(i[0].replace("_", " "))
        ], href=f"/dashboard/{i[0]}",
            className="btn btn-small btn-info")
        for i in info]
    return resp
