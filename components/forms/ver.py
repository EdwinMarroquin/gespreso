import dash
from dash import html
from db import database
from components import table, table_where


def insumos(record_id):
    """
    Obtiene información sobre los insumos y los insumos consumidos de un ID específico.

    Args:
        record_id (int): ID del insumo.

    Returns:
        list: Lista de elementos HTML con la información de los insumos y los insumos consumidos.
    """
    rows = []

    db = database.DB()

    rows.append(
        table.list(
            title='insumo',
            data=db.custom_read(
                table_name=f'ver_insumos',
                where=f'id={record_id}'
            )
        )
    )
    rows.append(
        table.info(
            title='insumo consumido',
            data=db.custom_read(
                table_name=f'ver_insumos_presupuesto',
                columns='id, item, subcapitulo, capitulo, cantidad, rendimiento, precio, subtotal',
                where=f'id={record_id}'
            )
        )
    )

    return rows


def items(record_id):
    """
    Genera una estructura HTML para mostrar los detalles de un item.

    Args:
        record_id (int): ID del item.

    Returns:
        dash.html.Article: Estructura HTML con los detalles del item.
    """
    db = database.DB()
    data = db.custom_read(table_name='ver_uso_insumos',
                          where=f"id_item = {record_id}")

    info = data["columns"]
    insumos = data["records"]

    item = db.read_one('items', record_id)
    subcapitulo = db.read_one('subcapitulos', item[2])
    capitulo = db.read_one('capitulos', subcapitulo[2])

    titulo = item[1]
    unidad = db.read_one('unidades', item[3])[2]
    cantidad = item[4]

    total = 0

    body = []
    thead = []
    tbody = []

    head = []
    columns = [0, 1, 9, 10, 11, 12]

    for i, k in enumerate(info):
        if i in columns:
            head.append(html.Th(k))

    thead.append(html.Tr(head))

    for insumo in insumos:
        trow = []
        for i, k in enumerate(info):
            if i in columns:
                if i == 12 or i == 11:
                    trow.append(
                        html.Td(
                            "$ {:,.2f}".format(insumo[i]),
                            style={'text-align': 'right'}
                        )
                    )
                    if i == 12:
                        total += insumo[i]
                else:
                    trow.append(html.Td(insumo[i]))

        tbody.append(html.Tr(trow))
    tbody.append(
        html.Tr(
            children=[
                html.Td(html.H3('TOTAL'), colSpan=5),
                html.Td(html.H3("$ {:,.2f}".format(total)))
            ],
            className="bg-text-dark"
        )
    )
    info_item = []
    info_item.append(
        html.H2(
            [
                html.Span('Capitulo'),
                html.Span(f'{capitulo[0]}'),
                html.Span(f'{capitulo[1]}'),
            ],
            className="head-item title"
        )
    )
    info_item.append(
        html.H3(
            [
                html.Span('Subcapitulo'),
                html.Span(f'{subcapitulo[0]}'),
                html.Span(f'{subcapitulo[1]}'),
            ],
            className="head-item title"
        )
    )

    info_item.append(
        html.P('Analisis de precio unitario',
               className="bg-text-dark d-flex middle padding-s margin-bottom-s")
    )

    info_item_descripcion = []

    info_item_descripcion.append(
        html.H4(
            [
                html.Span('ITEM', className="text-left"),
                html.Span('CANTIDAD', className="text-center"),
                html.Span('UNIDAD', className="text-center"),
                html.Span('VR UNITARIO', className="text-right"),
                html.Span('VR TOTAL', className="text-right")
            ], className="head-item-desc-title"
        )
    )
    info_item_descripcion.append(
        html.H4(
            [
                html.Span(
                    [
                        html.A(
                            [
                                html.I(className="bi bi-pencil-fill"),
                            ],
                            className="btn btn-s btn-info text-left",
                            style={"margin-right": ".5rem"},
                            href=f'/dashboard/items/editar/{record_id}'
                        ),
                        titulo
                    ],
                    style={"display": "inline-flex", 'align-items': 'center'}
                ),
                html.Span(cantidad, className="text-center"),
                html.Span(unidad, className="text-center"),
                html.Span(
                    "$ {:,.2f}".format(total),
                    className="text-right"
                ),
                html.Span(
                    "$ {:,.2f}".format(total * cantidad),
                    className="text-right"
                ),
            ], className="head-item-desc-info"
        )
    )

    info_item.append(html.Div(info_item_descripcion,
                              className="head-item-desc"))

    body.append(html.Div(info_item, className="head"))

    if len(insumos) > 0:
        body.append(
            html.Div(
                html.Table([
                    html.Thead(thead),
                    html.Tbody(tbody)
                ]
                ), className="table"
            )
        )
    else:
        body.append(
            html.H1(
                'No hay insumos registrados',
                className="head-item title d-flex middle padding-s bg-text-dark"
            )
        )

    return html.Article(body, className="informes items")
