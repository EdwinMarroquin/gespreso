import dash
from dash import html
from db import database as ddb


def layout():
    """
    Genera el layout de la página de informe de insumos.

    Returns:
        html.Article: El layout de la página de informe de insumos.
    """
    table_name = "ver_grupos_insumos"
    db = ddb.DB()
    records = db.custom_read(table_name=table_name)
    info = db.info_table(table_name)

    insumos_dict = {}

    for insumo in records["records"]:
        key = insumo[1]
        value = {
            'id': insumo[2],
            'nombre': insumo[3],
            'unidad': insumo[4]
        }
        insumos_dict.setdefault(key, []).append(value)

    table_data = []

    for kit, (key, value) in enumerate(insumos_dict.items(), start=1):
        rows = [
            html.Tr([
                html.Td(item['id']),
                html.Td(item['nombre']),
                html.Td(item['unidad']),
                html.Td(html.A([
                    html.I(className="bi-eye-fill"),
                    html.Span('Ver')],
                    className="btn btn-success",
                    href=f"/dashboard/insumos/ver/{item['id']}"),
                    className="d-flex middle")
            ]) for item in value
        ]

        buttonTable = f'buttonTable{kit}'
        bodyTable = f'bodyTable{kit}'
        headTable = f'headTable{kit}'

        table_data.append(
            html.Div(
                children=[
                    html.Table([
                        html.Caption([
                            html.Span(key, className="caption-title"),
                            html.Button(
                                id=buttonTable,
                                n_clicks=0,
                                className="bi bi-list-nested caption-action"
                            )
                        ]),
                        html.Thead(
                            html.Tr([
                                html.Th('ID'),
                                html.Th('Nombre'),
                                html.Th('Unidad'),
                                html.Th('Acciones')
                            ]),
                            id=headTable,
                            style={"display": "none"}
                        ),
                        html.Tbody(
                            rows,
                            id=bodyTable,
                            style={"display": "none"}
                        )
                    ], id=f"table{kit}", className="tableId")
                ],
                className="table"
            )
        )

    return html.Article(table_data, className="insumos informe")
