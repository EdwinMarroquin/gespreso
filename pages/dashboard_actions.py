import dash
import inspect
import importlib
from dash import html, dcc
from components import logo, navigate
from components.forms import nuevo, ver, editar, eliminar
from db import database

db = database.DB()

dash.register_page(
    __name__,
    path_template='/dashboard/<table_name>/<action>/<record_id>',
    title='Gespreso - Tablas'
)


def valida_vista(module_name, function_name, argument):
    module = importlib.import_module(module_name)
    function = getattr(module, function_name, None)
    if inspect.isfunction(function):
        return function(argument)
    else:
        return None


def layout(table_name=None, action=None, record_id=None):
    lyI = []
    view = html.H1('oops!', className="d-flex middle margin-auto")

# Vistas CRUD del dashboarda
    # Vitas de insumos
    if table_name == 'insumos':
        if action == 'nuevo':
            view = nuevo.insumos(table_name)
        if action == 'ver':
            view = ver.insumos(record_id)
        if action == 'editar':
            view = editar.insumos(record_id)
        if action == 'eliminar':
            view = eliminar.layout(table_name, record_id)

    # Vitas de unidades
    if table_name == 'unidades':
        if action == 'nuevo':
            view = nuevo.unidades(table_name)
        if action == 'ver':
            view = ver.unidades(table_name)
        if action == 'editar':
            view = editar.unidades(record_id)
        if action == 'eliminar':
            view = eliminar.layout(table_name, record_id)

    # Vistas de items
    if table_name == 'items':
        if action == 'nuevo':
            view = nuevo.items(table_name)
        if action == 'ver':
            view = ver.items(record_id)
        if action == 'editar':
            view = editar.items(record_id)
        if action == 'eliminar':
            view = eliminar.layout(table_name, record_id)

    # Vistas de subcapitulos
    if table_name == 'subcapitulos':
        if action == 'nuevo':
            view = nuevo.subcapitulos(record_id)
        if action == 'editar':
            view = editar.subcapitulos(record_id)
        if action == 'eliminar':
            view = eliminar.layout(table_name, record_id)

    # Vistas de capitulos
    if table_name == 'capitulos':
        if action == 'nuevo':
            view = nuevo.capitulos(record_id)
        if action == 'editar':
            view = editar.capitulos(record_id)
        if action == 'eliminar':
            view = eliminar.layout(table_name, record_id)

    lyI = html.Article(view, className=f'action {action}')

    str_view_title = f" - {table_name}" if table_name != None else ""
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
