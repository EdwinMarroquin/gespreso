import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(
                table='unidades',
                context='unidades',
                actions={'ver': False, 'editar': True, 'eliminar': False}
            )
        ],
        className='unidades'
    )
