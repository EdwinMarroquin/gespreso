import dash
from dash import html
from db import database


def generate(
    table=None, context=None,
    actions={
        'ver': False,
        'editar': False,
        'eliminar': False
    },
    style=None
):
    db = database.DB()
    info = db.info_table(table)
    records = db.read_all(table)
    rows = []
    heads = []

    for i, p in enumerate(info):
        heads.append(html.Th(info[i][1]))
    if actions["ver"] == True or actions["editar"] == True or actions["eliminar"] == True:
        heads.append(html.Th("Acciones"))

    for record in records:
        cells = []
        for i, p in enumerate(info):
            cells.append(html.Td(record[i]))
        if actions["ver"] == True or actions["editar"] == True or actions["eliminar"] == True:
            cells.append(html.Td([
                html.A([html.I(className="bi-eye-fill"), html.Span('Ver')], className="btn btn-success",
                       href=f"/dashboard/{context}/ver/{record[0]}") if actions["ver"] == True else None,
                html.A([html.I(className="bi-pencil-fill"), html.Span('Editar')], className="btn btn-info",
                       href=f"/dashboard/{context}/editar/{record[0]}") if actions["editar"] == True else None,
                html.A([html.I(className="bi-trash3-fill"), html.Span('Eliminar')], className="btn btn-danger",
                       href=f"/dashboard/{context}/eliminar/{record[0]}") if actions["eliminar"] == True else None,
            ], className="actions"))
        rows.append(html.Tr(cells))

    return html.Article([html.Div(html.Table([
        html.Thead(html.Tr(heads)),
        html.Tbody(rows)
    ]), className="table"),
        html.A(href=f"/dashboard/{context}/nuevo/{len(records) + 1}", children=[
            html.I(className="bi-node-plus-fill"),
            html.Span(f"NUEVO {context}", style={
                      'text-transform': 'uppercase'})
        ], className="btn btn-large btn-dark text-bold", style={'margin-top': '1rem', 'min-height': '2.5rem'})], className=context)


def list(title=None,  data=None):
    """
    Genera una lista vertical del tipo clave - valor
    """

    rows = []
    rows.append(html.H1(f'tabla {title}', className=f'ver_titulo'))
    for i, p in enumerate(data["columns"]):
        rows.append(
            html.P([
                html.Span(f'{p}:',
                          className=f'ver_info_clave'),
                html.Span(data["records"][0][i], className=f'ver_info_valor')
            ], className=f'ver_info')
        )

    return html.Article(children=rows)


def info(title=None, data=None):
    """
    retorna una estructura en forma de tabla
    """
    rows = []
    heads = []
    for i, p in enumerate(data["columns"]):
        heads.append(html.Th(p))

    for record in data["records"]:
        cells = []
        for i, p in enumerate(data["columns"]):
            cells.append(html.Td(record[i]))
        rows.append(html.Tr(cells))

    return html.Article([
        html.H1(f'tabla {title}', className=f'ver_titulo'),
        html.Div(
            children=[
                html.Table([
                    html.Thead(html.Tr(heads)),
                    html.Tbody(rows)
                ])
            ], className='table')
    ], className="informes")
