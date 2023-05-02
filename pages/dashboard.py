import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from components import logo
from pages import dashboard_inicio, dashboard_insumos, dashboard_items, dashboard_subcapitulos, dashboard_capitulos, dashboard_presupuestos

app = dash.Dash(__name__)
dash.register_page(__name__, path_template='/dashboard/<view>')


def layout(view=None):
    lyD = html.H1('Pagina no encontrada')
    lyD = dashboard_inicio.layout() if view == "inicio" else lyD
    lyD = dashboard_insumos.layout() if view == "insumos" else lyD
    lyD = dashboard_items.layout() if view == "items" else lyD
    lyD = dashboard_subcapitulos.layout() if view == "subcapitulos" else lyD
    lyD = dashboard_capitulos.layout() if view == "capitulos" else lyD
    lyD = dashboard_presupuestos.layout() if view == "presupuestos" else lyD

    header = html.Header([
        html.Header([
            logo.layout(2, secondary="#e0e0e0"),
            html.H2(children=["Dashboard - " + view],
                    className="header_title"),
        ], className="header")
    ])

    main = html.Main([
        html.Nav(children=[
            html.Div(children=[
                html.A(children=[
                    html.I(className="bi-house-fill"),
                    html.Span("Inicio")
                ], href="./inicio", className="nav"),
                html.A(children=[
                    html.I(className="bi-file-earmark-text-fill"),
                    html.Span("Reportes")
                ], href="./reportes", className="nav"),
                html.A(children=[
                    html.I(className="bi-sliders2"),
                    html.Span("Configuraciones")
                ], href="./insumos/ver/10", className="nav")

            ])
        ], className="nav"),
        dcc.Location(id="urlDash", refresh=True),
        html.Div(lyD, className="main_content")
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
