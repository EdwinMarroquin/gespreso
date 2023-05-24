import dash
from dash import html
from components import table


def layout():
    """
    Genera el layout de la sección de items.

    Returns:
        html.Article: El layout de la sección de items.
    """
    return html.Article(
        [
            table.generate(
                table='ver_items',
                context='items',
                actions={'ver': True, 'editar': True, 'eliminar': True}
            )
        ],
        className='items'
    )
