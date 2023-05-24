import dash
from dash import html, dcc
from components import logo, navigate, footer
from pages import (
    dashboard_inicio,
    dashboard_unidades,
    dashboard_insumos,
    dashboard_items,
    dashboard_subcapitulos,
    dashboard_capitulos,
    dashboard_presupuestos
)

app = dash.Dash(__name__)
dash.register_page(
    __name__,
    path_template='/dashboard/<view>',
    title='Gespreso - Dashboard'
)


def layout(view=None):
    """
    Genera el layout del dashboard.

    Args:
        view (str): Vista actual del dashboard.

    Returns:
        html.Div: El layout del dashboard.
    """
    lyD = []

    if view == "inicio" or view is None or view == '':
        lyD = dashboard_inicio.layout()
    elif view == "insumos":
        lyD = dashboard_insumos.layout()
    elif view == "unidades":
        lyD = dashboard_unidades.layout()
    elif view == "items":
        lyD = dashboard_items.layout()
    elif view == "subcapitulos":
        lyD = dashboard_subcapitulos.layout()
    elif view == "capitulos":
        lyD = dashboard_capitulos.layout()
    elif view == "presupuestos":
        lyD = dashboard_presupuestos.layout()

    str_view_title = f" - {view}" if view is not None else ""

    header = html.Header([
        html.Div(
            [
                logo.layout(2, secondary="#e0e0e0"),
                html.H2(children=["Dashboard" + str_view_title],
                        className="header_title"),
            ],
            className="header"
        )
    ])

    main = html.Main([
        navigate.layout(),
        dcc.Location(id="urlDash", refresh=True),
        html.Div(lyD, className="main_content")
    ])

    return html.Div(
        [
            html.Link(href="./assets/icon/bootstrap-icons.css"),
            header,
            main,
            html.Footer(footer.layout(), className="footer")
        ],
        className="dashboard"
    )
