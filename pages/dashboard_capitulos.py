import dash
from dash import html
from components import table


def layout():
    """
    Genera el layout de la sección de capítulos.

    Returns:
        html.Article: El layout de la sección de capítulos.
    """
    return html.Article(
        [
            table.generate(
                table='capitulos',
                context='capitulos',
                actions={'ver': False, 'editar': True, 'eliminar': True}
            )
        ],
        className='capitulos'
    )
