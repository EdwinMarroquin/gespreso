import dash
from dash import html
from components import logo

dash.register_page(
    __name__,
    path_template='/',
    title='Gespreso'
)


def layout():
    """
    Genera el layout de la página principal.

    Returns:
        html.Main: El layout de la página principal.
    """
    return html.Main(
        [
            logo.layout(5),
            html.Br(),
            html.A('INGRESAR', href='/dashboard/inicio', className="button")
        ],
        className="home_main"
    )
