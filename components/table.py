import dash
from dash import html
from db import database


def generate(table=None, context=None, actions=None, style=None):
    """
    Genera una tabla HTML con registros de una tabla de la base de datos y acciones opcionales.

    Args:
        table (str): Nombre de la tabla de la base de datos.
        context (str): Clase CSS para dar estilo al contenedor de la tabla.
        actions (dict): Acciones opcionales a mostrar en cada registro.
        style: Estilo adicional para aplicar al contenedor de la tabla.

    Returns:
        dash.html.Article: Estructura HTML de la tabla generada.
    """
    db = database.DB()
    info = db.info_table(table)
    records = db.read_all(table)
    rows = []
    heads = []

    for i, p in enumerate(info):
        heads.append(html.Th(info[i][1]))

    if any(actions.values()):
        heads.append(html.Th("Acciones"))

    for record in records:
        cells = []
        for i, p in enumerate(info):
            cells.append(html.Td(record[i]))

        if any(actions.values()):
            action_buttons = []

            if actions["ver"]:
                action_buttons.append(html.A([
                    html.I(className="bi-eye-fill"),
                    html.Span('Ver')
                ], className="btn btn-success", href=f"/dashboard/{context}/ver/{record[0]}"))

            if actions["editar"]:
                action_buttons.append(html.A([
                    html.I(className="bi-pencil-fill"),
                    html.Span('Editar')
                ], className="btn btn-info", href=f"/dashboard/{context}/editar/{record[0]}"))

            if actions["eliminar"]:
                action_buttons.append(html.A([
                    html.I(className="bi-trash3-fill"),
                    html.Span('Eliminar')
                ], className="btn btn-danger", href=f"/dashboard/{context}/eliminar/{record[0]}"))

            cells.append(html.Td(action_buttons, className="actions"))

        rows.append(html.Tr(cells))

    article_content = html.Article([
        html.Div(html.Table([
            html.Thead(html.Tr(heads)),
            html.Tbody(rows)
        ]), className="table"),
        html.A(href=f"/dashboard/{context}/nuevo/{len(records) + 1}", children=[
            html.I(className="bi-node-plus-fill"),
            html.Span(f"NUEVO {context}", style={
                      'text-transform': 'uppercase'})
        ], className="btn btn-large btn-dark text-bold", style={'margin-top': '1rem', 'min-height': '2.5rem'})
    ], className=context)

    return article_content


def list(title=None, data=None):
    """
    Genera una lista vertical del tipo clave - valor.

    Args:
        title (str): Título de la lista.
        data (dict): Datos en forma de diccionario con claves y valores.

    Returns:
        dash.html.Article: Estructura HTML de la lista generada.
    """
    rows = []
    rows.append(html.H1(f'tabla {title}', className=f'ver_titulo'))

    for i, p in enumerate(data["columns"]):
        rows.append(
            html.P([
                html.Span(f'{p}:', className=f'ver_info_clave'),
                html.Span(data["records"][0][i], className=f'ver_info_valor')
            ], className=f'ver_info')
        )

    return html.Article(children=rows)


def info(title=None, data=None):
    """
    Genera una estructura en forma de tabla con los datos proporcionados.

    Args:
        title (str): Título de la tabla.
        data (dict): Datos en forma de diccionario con claves "columns" y "records".

    Returns:
        dash.html.Article: Estructura HTML de la tabla generada.
    """
    rows = []
    heads = [html.Th(column) for column in data["columns"]]

    for record in data["records"]:
        cells = [html.Td(record[i]) for i in range(len(data["columns"]))]
        rows.append(html.Tr(cells))

    return html.Article([
        html.H1(f'tabla {title}', className='ver_titulo'),
        html.Div(children=[
            html.Table([
                html.Thead(html.Tr(heads)),
                html.Tbody(rows)
            ])
        ], className='table')
    ], className='informes')
