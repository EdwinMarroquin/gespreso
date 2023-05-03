import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from components import logo, navigate
from pages import informes, informe_grupos_insumos

# app = dash.Dash(__name__)
dash.register_page(
    __name__, path_template='/dashboard/informes/<view>')


def layout(view=None, filter=None):
    lyI = html.H1('Pagina no encontrada')
    lyI = informes.layout() if view == "inicio" or view == None else lyI
    lyI = informe_grupos_insumos.layout() if view == "grupos" else lyI
    str_view_title = f" - {view}" if view != None else ""
    header = html.Header([
        html.Header([
            logo.layout(2, secondary="#e0e0e0"),
            html.H2(children=["INFORMES" + str_view_title],
                    className="header_title"),
        ], className="header")
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
