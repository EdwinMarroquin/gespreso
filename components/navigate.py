import dash
from dash import html


def layout():
    return html.Nav(children=[
        html.Div(children=[
            html.A(children=[
                html.I(className="bi-house-fill"),
                html.Span("Inicio")
            ], href="/dashboard/inicio"),
            html.A(children=[
                html.I(className="bi-file-earmark-text-fill"),
                html.Span("Informes")
            ], href="/dashboard/informes/inicio"),
            # html.A(children=[
            #     html.I(className="bi-sliders2"),
            #     html.Span("Configuraciones")
            # ], href="./insumos/ver/10", className="last")

        ])
    ], className="nav")
