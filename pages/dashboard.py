import dash
from dash import html, dcc
from components import logo, navigate, footer
from pages import dashboard_inicio, dashboard_unidades, dashboard_insumos, dashboard_items, dashboard_subcapitulos, dashboard_capitulos, dashboard_presupuestos

app = dash.Dash(__name__)
dash.register_page(__name__, path_template='/dashboard/<view>')


def layout(view=None):
    lyD = []
    lyD = dashboard_inicio.layout() if view == "inicio" or view == None or view == '' else lyD
    lyD = dashboard_insumos.layout() if view == "insumos" else lyD
    lyD = dashboard_unidades.layout() if view == "unidades" else lyD
    lyD = dashboard_items.layout() if view == "items" else lyD
    lyD = dashboard_subcapitulos.layout() if view == "subcapitulos" else lyD
    lyD = dashboard_capitulos.layout() if view == "capitulos" else lyD
    lyD = dashboard_presupuestos.layout() if view == "presupuestos" else lyD

    str_view_title = f" - {view}" if view != None else ""

    header = html.Header([
        html.Header([
            logo.layout(2, secondary="#e0e0e0"),
            html.H2(children=["Dashboard" + str_view_title],
                    className="header_title"),
        ], className="header")
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
