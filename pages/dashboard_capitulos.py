import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(
                table='capitulos',
                context='capitulos',
                actions={'ver': True, 'editar': True, 'eliminar': False}
            )
        ],
        className='capitulos'
    )
