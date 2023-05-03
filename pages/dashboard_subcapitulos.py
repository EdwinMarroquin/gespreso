import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(
                table='subcapitulos',
                context='subcapitulos',
                actions={'ver': True, 'editar': True, 'eliminar': True}
            )
        ],
        className='subcapitulos'
    )
