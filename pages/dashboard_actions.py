import dash
from dash import html, dcc
from components import logo, navigate
from components.forms import nuevo, ver, editar, eliminar

dash.register_page(
    __name__, path_template='/dashboard/<database>/<action>/<code>')


def layout(database=None, action=None, code=None):
    lyI = []
    if database == 'insumos':
        if action == 'nuevo':
            lyI = html.Article(nuevo.layout(
                database, 'ver_insumos', code), className=f'action {action}')
        if action == 'ver':
            lyI = html.Article(ver.layout(
                database, 'insumos', code), className=f'action {action}')
        if action == 'editar':
            lyI = html.Article(editar.layout(
                database, 'ver_insumos', code), className=f'action {action}')
        if action == 'eliminar':
            lyI = html.Article(eliminar.layout(
                database, 'ver_insumos', code), className=f'action {action}')

    str_view_title = f" - {database}" if database != None else ""
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
    ],)

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
