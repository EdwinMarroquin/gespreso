import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(
                table='ver_insumos',
                context='insumos',
                actions={'ver': True, 'editar': True, 'eliminar': True}
                )
        ],
        className='insumos'
    )
