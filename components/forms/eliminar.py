import dash
from dash import html
from db import database


def layout(title, table_name, record_id):
    db = database.DB()
    info = db.info_table(table_name)
    return html.Div(children=[
        html.H1('Eliminar')
    ])
