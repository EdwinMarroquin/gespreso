import dash
from dash import html, Input, Output, State
from db import database as ddb


def layout():

    tb = "ver_grupos_insumos"
    db = ddb.DB()
    records = db.custom_read(table_name=tb)
    info = db.info_table(tb)

    insumos_dict = {}

    for insumo in records["records"]:
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
                html.Td(html.A([
                    html.I(className="bi-eye-fill"),
                    html.Span('Ver')], className="btn btn-success",
                    href=f"/dashboard/insumos/ver/{item['id']}"),
                    className="d-flex middle")]
            rows.append(html.Tr(row))
        buttonTable = f'buttonTable{kit}'
        bodyTable = f'bodyTable{kit}'
        headTable = f'headTable{kit}'
        table_data.append(html.Div(children=[
            html.Table([
                html.Caption([
                    html.Span(key, className="caption-title"),
                    html.Button(
                        id=buttonTable,
                        n_clicks=0,
                        className="bi bi-list-nested caption-action"
                    )
                ]),
                html.Thead(html.Tr([
                    html.Th('ID'),
                    html.Th('Nombre'),
                    html.Th('Unidad'),
                    html.Th('Acciones')
                ]), id=headTable, style={"display": "none"}),
                html.Tbody(
                    rows,
                    id=bodyTable,
                    style={"display": "none"})
            ], id=f"table{kit}", className="tableId")], className="table"))

        # @app.callback(
        #     [Output(bodyTable, 'style'),
        #         Output(headTable, 'style')],
        #     [Input(buttonTable, 'n_clicks')],
        #     [State(bodyTable, 'style')]
        # )
        # def toggle_table(n_clicks, style):
        #     style_display = 'none'
        #     if n_clicks % 2 == 0:
        #         style_display = 'table-row-group'
        #     else:
        #         style_display = 'none'

        #     return {'display': style_display}

    return html.Article(table_data, className="insumos informe")
