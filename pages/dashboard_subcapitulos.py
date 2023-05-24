import dash
from dash import html
from components import table


def layout():
    """
    Genera el layout de la sección de subcapítulos.

    Returns:
        html.Article: El layout de la sección de subcapítulos.
    """
    return html.Article(
        [
            table.generate(
                table='subcapitulos',
                context='subcapitulos',
                actions={'ver': False, 'editar': True, 'eliminar': True}
            )
        ],
        className='subcapitulos'
    )
