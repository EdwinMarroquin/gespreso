import dash
from dash import html
from db import database


def generate(
    table=None, context=None,
    record_id=None,
    style=None
):
    db = database.DB()
    info = db.info_table(table)

    if record_id != None:
        where_id = f'id={record_id}'

    records = db.custom_read(table_name=table, where=where_id)
    rows = []
    heads = []

    for i, p in enumerate(info):
        heads.append(html.Th(info[i][1]))

    for record in records:
        cells = []
        for i, p in enumerate(info):
            cells.append(html.Td(record[i]))
        rows.append(html.Tr(cells))

    return html.Article([html.Div(html.Table([
        html.Thead(html.Tr(heads)),
        html.Tbody(rows)
    ]), className="table")], className=context)
