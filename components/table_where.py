import dash
from dash import html
from db import database


def generate(table=None, context=None, record_id=None, style=None):
    # Inicializar la conexión a la base de datos
    db = database.DB()

    # Obtener la información de la tabla
    info = db.info_table(table)

    # Definir la condición para filtrar por record_id si está presente
    where_id = None
    if record_id is not None:
        where_id = f'id={record_id}'

    # Obtener los registros de la base de datos según la tabla y la condición
    records = db.custom_read(table_name=table, where=where_id)

    # Crear las listas para las filas y encabezados de la tabla
    rows = []
    heads = []

    # Generar los encabezados de la tabla basados en la información de la tabla
    for i, p in enumerate(info):
        heads.append(html.Th(info[i][1]))

    # Generar las filas de la tabla basadas en los registros de la base de datos
    for record in records:
        cells = []
        for i, p in enumerate(info):
            cells.append(html.Td(record[i]))
        rows.append(html.Tr(cells))

    # Construir la estructura HTML final con la tabla generada
    article_content = html.Article([
        html.Div(html.Table([
            html.Thead(html.Tr(heads)),
            html.Tbody(rows)
        ]), className="table")
    ], className=context)

    return article_content
