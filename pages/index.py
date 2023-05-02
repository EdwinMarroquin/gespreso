import dash
from dash import html
from components import logo

dash.register_page(__name__, path_template='/')


def layout():
    return html.Main([
        logo.layout(5),
        html.Br(),
        html.A('INGRESAR', href='/dashboard/inicio', className="button")
    ], className="home_main")
