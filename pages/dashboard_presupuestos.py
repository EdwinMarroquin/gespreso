import dash
from dash import html
from components import table
from backend import parse
from db import database


def layout():
    db = database.DB()
    info = ('id', 'insumo', 'item', 'subcapitulo', 'capitulo',
            'presupuesto', 'cantidad', 'rendimiento', 'precio', 'subtotal')
    data = db.read_all('ver_insumos_presupuesto')
    presupuesto = parse.jsonPresupuesto(info, data)
    pres = []
    total_presupuesto = 0
    for index_presupuesto, valor_presupuesto in enumerate(presupuesto):
        titles = []
        caps_presupuesto = []
        caps = presupuesto[valor_presupuesto]

        for indice_cap, valor_cap in enumerate(caps):
            subcaps_presupuesto = []
            subcaps = caps[valor_cap]

            for indice_subcap, valor_subcap in enumerate(subcaps):
                items_presupuesto = []
                items = subcaps[valor_subcap]

                headTable = []
                rowsTable = []
                insumo_agregado = False
                insumo_head_agregado = False
                totalItem = 0
                for indice_item, valor_item in enumerate(items):
                    insumos_presupuesto = []
                    insumos = items[valor_item]
                    rowTable = []
                    rowTable.append(
                        html.Td(
                            valor_item,
                            style={
                                'width': '100%',
                                'text-align': 'left'
                            }
                        )
                    )
                    for indice_insumo, valor_insumo in enumerate(insumos):
                        if valor_insumo != 'id':
                            if insumo_agregado == False:
                                if insumo_head_agregado == False:
                                    headTable.append(
                                        html.Th(
                                            'insumo',
                                            style={
                                                'width': '100%',
                                                'text-align': 'left'
                                            }
                                        )
                                    )
                                insumo_head_agregado = True
                                headTable.append(
                                    html.Th(valor_insumo)
                                )
                            if valor_insumo == 'valor_unitario' or valor_insumo == 'subtotal':
                                rowTable.append(
                                    html.Td(
                                        "$ {:,.0f}".format(
                                            insumos[valor_insumo]
                                        )
                                    )
                                )
                            else:
                                rowTable.append(
                                    html.Td(
                                        insumos[valor_insumo]
                                    )
                                )
                    total_presupuesto += insumos['subtotal']
                    totalItem += insumos['subtotal']
                    rowsTable.append(
                        html.Tr(rowTable)
                    )
                    insumo_agregado = True
                rowsTable.append(
                    html.Tr(
                        [
                            html.Td(
                                'TOTAL',
                                colSpan='4',
                                style={
                                        'text-align': 'right'
                                }
                            ),
                            html.Td(
                                "$ {:,.0f}".format(totalItem)
                            )
                        ], className="bg-text-dark border-top-dark"
                    )
                )
                totalItem = 0

                items_presupuesto.append(
                    html.Article(
                        html.Div(
                            html.Table(
                                [
                                    html.Thead(
                                        html.Tr(
                                            headTable
                                        )
                                    ),
                                    html.Tbody(rowsTable)
                                ],
                                style={'text-align': 'right'}),
                            className="table border-radius-less margin-bottom-l")
                    )
                )

                titles.insert(
                    0,
                    html.H4(
                        valor_subcap,
                        className="bg-text-dark padding-s",
                        style={'width': '50%'}
                    )
                )
                subcaps_presupuesto.append(
                    html.Div(
                        items_presupuesto
                    )
                )

            titles.insert(
                0,
                html.H4(
                    valor_cap,
                    className="bg-text-dark padding-s",
                    style={'width': '50%'}
                )
            )
            caps_presupuesto.append(
                html.Div(
                    subcaps_presupuesto
                )
            )
        titles.insert(
            0,
            html.H3(
                valor_presupuesto,
                className="bg-text-dark padding-m",
                style={'width': '100%'}
            )
        )
        pres.append(
            html.P(
                titles,
                style={
                    'display': 'flex',
                    'flex-flow': 'row wrap'
                }
            )
        )
        pres.append(
            html.Div(caps_presupuesto)
        )
    pres.append(
        html.Div(
            [
                html.Span('TOTAL PRESUPUESTO', style={"flex": "1"}),
                html.Span("$ {:,.0f}".format(total_presupuesto))
            ],
            className="d-flex row bg-text-dark padding-s text-bold",
            style={"font-size": "1.5rem"}
        )
    )

    return html.Article(pres)
