import dash
from dash import html
from components import table


def layout():
    """
    Genera el layout de la sección de unidades.

    Returns:
        html.Article: El layout de la sección de unidades.
    """
    return html.Article(
        [
            table.generate(
                table='unidades',
                context='unidades',
                actions={'ver': False, 'editar': True, 'eliminar': True}
            )
        ],
        className='unidades'
    )
