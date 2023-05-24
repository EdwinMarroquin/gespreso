import dash
from dash import html
from components import table


def layout():
    """
    Genera el layout de la sección de insumos.

    Returns:
        html.Article: El layout de la sección de insumos.
    """
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
