import dash
from dash import dcc, html, Input, Output
from db import database as ddb

app = dash.Dash(__name__)


def layout():
    tb = "ver_grupos_insumos"
    db = ddb.DB()
    info = db.info_table(tb)
    records = db.custom_read(table_name=tb)

    insumos_dict = {}

    for insumo in records:
        key = insumo[1]
        value = {
            'id': insumo[2],
            'nombre': insumo[3],
            'unidad': insumo[4]
        }
        if key in insumos_dict:
            insumos_dict[key].append(value)
        else:
            insumos_dict[key] = [value]

    table_data = []
    table_ids = [f'tableBody{i}' for i in range(
        1, 1 + len(insumos_dict.items()))]
    kit = 0
    for key, value in insumos_dict.items():
        kit = kit + 1
        rows = []
        for item in value:
            row = [
                html.Td(item['id']),
                html.Td(item['nombre']),
                html.Td(item['unidad']),
                html.Td(html.A([html.I(className="bi-eye-fill"), html.Span('Ver')], className="btn btn-success",
                               href=f"/dashboard/insumos/ver/{item['id']}"), className="d-flex middle")
            ]
            rows.append(html.Tr(row))
        table_data.append(html.Div(children=[
            html.Table([
                html.Caption([
                    html.Span(key, className="caption-title"),
                    html.Button(
                        id=f'buttonTable{kit}',
                        n_clicks=0,
                        **{'aria-label': 'showBody'},
                        className="bi bi-list-nested caption-action"
                    )
                ]),
                html.Thead(html.Tr([
                    html.Th('ID'),
                    html.Th('Nombre'),
                    html.Th('Unidad'),
                    html.Th('Acciones')
                ]), id=f"tableHead{kit}"),
                html.Tbody(rows, id=f"tableBody{kit}", style={
                           'color': 'black'})
            ], id=f"table{kit}", className="tableId")], className="table"))

    return html.Article(table_data, className="insumos informe")
