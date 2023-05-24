import dash
from dash import html, dcc
from components import logo, navigate
from pages import informes, informe_grupos_insumos

dash.register_page(
    __name__,
    path_template='/dashboard/informes/<view>',
    title='Gespreso - Informes'
)


def layout(view=None, filter=None):
    """
    Genera el layout del dashboard de informes.

    Args:
        view (str): Vista actual del dashboard.
        filter: Filtro aplicado en los informes (no se utiliza actualmente).

    Returns:
        html.Div: El layout del dashboard de informes.
    """
    lyI = None

    if view == "inicio" or view is None:
        lyI = informes.layout()
    elif view == "grupos":
        lyI = informe_grupos_insumos.layout()

    if lyI is None:
        return None

    str_view_title = f" - {view}" if view is not None else ""
    header = html.Header([
        html.Div(
            [
                logo.layout(2, secondary="#e0e0e0"),
                html.H2(children=["INFORMES" + str_view_title],
                        className="header_title"),
            ],
            className="header"
        )
    ])

    main = html.Main([
        navigate.layout(),
        dcc.Location(id="urlDash", refresh=True),
        html.Div(lyI, className="main_content")
    ])

    footer = html.Footer()

    return html.Div(
        [
            html.Link(href="./assets/icon/bootstrap-icons.css"),
            header,
            main,
            footer
        ],
        className="dashboard"
    )
