import dash
from dash import html
from db import database
from components import table, table_where


def layout(title, table_name, id):

    rows = []

    db = database.DB()

    rows.append(
        table.list(
            title='insumo',
            data=db.custom_read(
                table_name=f'ver_{table_name}',
                where=f'id={id}'
            )
        )
    )
    rows.append(
        table.info(
            title='insumo consumido',
            data=db.custom_read(
                table_name=f'ver_{table_name}_presupuesto',
                columns='id, item, subcapitulo, capitulo, cantidad, rendimiento, precio, subtotal',
                where=f'id={id}'
            )
        )
    )
    return rows
