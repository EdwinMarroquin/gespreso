import dash
from dash import html
from db import database


def layout():
    db = database.DB()
    info = db.read_all("sqlite_sequence")

    resp = [
        html.Div([
            html.I(i[1]),
            html.Span(i[0].replace("_", " "))
        ], className="btn btn-small btn-info")
        for i in info]
    return resp
