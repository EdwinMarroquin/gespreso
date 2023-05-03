import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(
                table='ver_insumos_presupuesto',
                context='presupuestos',
                actions={'ver': True, 'editar': True, 'eliminar': False}
            )
        ],
        className='presupuestos'
    )
