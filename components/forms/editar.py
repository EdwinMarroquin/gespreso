import dash
from dash import html, dcc
from db import database


def insumos(record_id):
    db = database.DB()
    insumos = db.custom_read('insumos', '*', f'id={record_id}')
    unidades = db.read_all('unidades')
    grupos = db.read_all('grupos')
    insumo = insumos["records"][0]
    rows = []
    rows.append(dcc.Location(id='url', refresh=True))
    rows.append(
        html.H1(
            f'Edicion del insumo {insumo[1]}',
            className='form-title'
        )
    )

    for input_index, input_value in enumerate(insumos["columns"]):
        if input_value == 'id':
            rows.append(
                html.P([
                    html.Label(
                        input_value,
                        className='form-group-label',
                    ),
                    html.Div([
                        dcc.Input(
                            value=insumo[input_index],
                            disabled=True,
                            className='form-group-label',
                            id=input_value
                        )
                    ], className="dash-input")
                ], className='form-group')
            )
        else:
            if input_value == 'unidad_id':
                rows.append(
                    html.P([
                        html.Label(
                            'unidad',
                            className='form-group-label'
                        ),
                        dcc.Dropdown(
                            options=[
                                {'label': v[1], 'value': v[0]}
                                for v in unidades
                            ],
                            value=insumo[2],
                            className='form-group-input',
                            id=input_value
                        )

                    ], className='form-group')
                )
            elif input_value == 'grupo_id':
                rows.append(
                    html.P([
                        html.Label(
                            'grupo',
                            className='form-group-label'
                        ),
                        dcc.Dropdown(
                            options=[
                                {'label': v[1], 'value': v[0]}
                                for v in grupos
                            ],
                            value=insumo[3],
                            className='form-group-input',
                            id=input_value
                        )
                    ], className='form-group')
                )
            else:
                rows.append(
                    html.P([
                        html.Label(
                            input_value,
                            className='form-group-label'
                        ),
                        html.Div([
                            dcc.Input(
                                value=insumo[input_index],
                                className='form-group-input',
                                id=input_value
                            )
                        ], className="dash")
                    ], className='form-group')
                )
    rows.append(
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Actualizar", id="buttonLabel")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonUpdate'
            ),
            className="form-group d-flex"

        )
    )
    return html.Article(rows, className="d-flex middle col form")


def unidades(record_id):
    db = database.DB()
    info = db.read_all('sqlite_sequence')
    unidades = db.custom_read('unidades', '*', f'id={record_id}')
    unidad = unidades["records"][0]
    rows = [
        dcc.Location(id='url', refresh=True),
        html.H1(
            f'Editar unidad',
            className='form-title'
        ),
        html.P([
            html.Label(
                'id',
                className='form-group-label',
            ),
            html.Div([
                dcc.Input(
                    id='id',
                    value=f'{unidad[0]}',
                    disabled=True,
                    className='form-group-label',
                )
            ], className="dash-input")
        ], className='form-group'),
        html.P([
            html.Label(
                'unidad',
                className='form-group-label'
            ),
            html.Div([
                dcc.Input(
                    className='form-group-input',
                    id='nombre',
                    value=f'{unidad[1]}',
                )
            ], className="dash")
        ], className='form-group'),
        html.P([
            html.Label(
                'abreviatura',
                className='form-group-label'
            ),
            html.Div([
                dcc.Input(
                    className='form-group-input',
                    id='abreviatura',
                    value=f'{unidad[2]}',
                )
            ], className="dash")
        ], className='form-group'),
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Actualizar unidad")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonUpdateunidades'
            ),
            className="form-group d-flex"

        )
    ]

    return html.Article(rows, className="d-flex middle col form")


def items(record_id):
    db = database.DB()
    data = db.custom_read(table_name='ver_uso_insumos',
                          where=f"id_item = {record_id}")
    insumos_disponibles = db.read_all('insumos')
    info = data["columns"]
    insumos = data["records"]

    item = db.read_one('items', record_id)

    titulo = item[1]
    unidad = db.read_one('unidades', item[3])[2]
    cantidad = item[4]

    total = 0

    body = []
    thead = []
    tbody = []

    head = []

    for i, k in enumerate(info):
        if i == 0 or i == 1 or i == 9 or i == 10 or i == 11 or i == 12:
            head.append(html.Th(k))

    thead.append(html.Tr(head))

    for insumo in insumos:
        trow = []
        for i, k in enumerate(info):
            btn = False
            if i == 0 or i == 1 or i == 9 or i == 10 or i == 11 or i == 12:
                if i == 12 or i == 11:
                    trow.append(
                        html.Td(
                            "$ {:,.2f}".format(insumo[i]),
                            className="text-right"
                        )
                    )
                    if i == 12:
                        total += insumo[i]
                else:
                    if i == 1:
                        trow.append(html.Td([
                            html.Div(
                                [
                                    html.I(className="bi bi-trash3"),
                                    # html.Span("Eliminar")
                                ],
                                className="btn btn-danger btn-small",
                                style={'margin-right': '1rem'},
                                **{
                                    'data-apu': record_id,
                                    'data-insumo': insumo[0]
                                },
                                id=f"eliminar_insumo_item_{insumo[0]}"
                            ),
                            insumo[i]
                        ], style={'display': 'inline-flex', 'align-items': 'center'}))

                    else:
                        trow.append(
                            html.Td(insumo[i], className="text-center"))

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
                html.Span(titulo, className="text-left"),
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

    addBody = html.Tr(
        [
            html.Td(
                [
                    dcc.Input(type="hidden", id="id_presupuesto", value=1),
                    dcc.Input(type="hidden", id="apu_id", value=record_id),
                    dcc.Dropdown(
                        options=[
                            {'label': v[1], 'value': v[0]}
                            for v in insumos_disponibles
                        ],
                        className='select',
                        id='insumo_id'
                    )
                ]
            ),
            html.Td(
                dcc.Input(
                    className='unit',
                    id='unidad',
                    disabled=True
                ),
            ),
            html.Td(
                dcc.Input(
                    className='text',
                    id='cantidad',
                ),
            ),
            html.Td(
                dcc.Input(
                    className='text',
                    id='rendimiento',
                ),
            ),
            html.Td(
                dcc.Input(
                    className='text',
                    id='precio',
                ),
            ),
            html.Td(
                html.Div(
                    [
                        html.I(className="bi bi-plus"),
                        html.Span('Agregar')
                    ],
                    className='btn btn-large btn-dark',
                    id='buttonAdd',
                )
            )
        ]
    )

    addHead = html.Tr(
        [
            html.Th('INSUMO', className='select'),
            html.Th('UN', className='unit'),
            html.Th('CANTIDAD', className='text'),
            html.Th('RENDIMIENTO', className='text'),
            html.Th('PRECIO', className='text'),
            html.Th(''),
        ]
    ),

    info_item.append(
        html.Div(
            html.Table([
                html.Thead(addHead),
                html.Tbody(addBody)
            ]), className="table form-add"
        )
    )

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

    body.append(dcc.Location(id='urlAdd', refresh=True))
    # body.append(html.Div(id='output'))
    return html.Article(body, className="informes items")


def subcapitulos(record_id):
    db = database.DB()

    subcapitulo = db.custom_read(table_name='subcapitulos',
                                 where=f"id = {record_id}")["records"][0]

    capitulos = db.read_all('capitulos')
    rows = [
        dcc.Location(id="url", refresh=True),
        html.H1('Editar subcapitulo', className="form-title"),
        html.P([
            html.Label('ID', className='form-group-label'),
            html.Div([
                dcc.Input(
                    id="id",
                    value=subcapitulo[0],
                    disabled=True,
                    className='form-group-input'
                )
            ], className="dash-input")
        ], className="form-group"),
        html.P([
            html.Label('Subcapitulo', className='form-group-label'),
            html.Div([
                dcc.Input(
                    id="nombre",
                    value=subcapitulo[1],
                    className='form-group-input'
                )
            ], className="dash-input")
        ], className="form-group"),
        html.P(
            [
                html.Label('Capitulo', className='form-group-label'),
                dcc.Dropdown(
                    id='capitulo_id',
                    className='form-group-label',
                    value=subcapitulo[2],
                    options=[
                        {'label': v[1], 'value': v[0]}
                        for v in capitulos
                    ]
                ),
            ], className="form-group"),
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Actualizar subcapitulo")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonUpdatesubcapitulo'
            ),
            className="form-group d-flex"

        )
    ]

    return html.Article(rows, className="d-flex middle col form")


def capitulos(record_id):
    db = database.DB()

    subcapitulo = db.custom_read(table_name='capitulos',
                                 where=f"id = {record_id}")["records"][0]

    rows = [
        dcc.Location(id="url", refresh=True),
        html.H1('Editar capitulo', className="form-title"),
        html.P([
            html.Label('ID', className='form-group-label'),
            html.Div([
                dcc.Input(
                    id="id",
                    value=subcapitulo[0],
                    disabled=True,
                    className='form-group-input'
                )
            ], className="dash-input")
        ], className="form-group"),
        html.P([
            html.Label('Subcapitulo', className='form-group-label'),
            html.Div([
                dcc.Input(
                    id="nombre",
                    value=subcapitulo[1],
                    className='form-group-input'
                )
            ], className="dash-input")
        ], className="form-group"),
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Actualizar capitulo")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonUpdatecapitulo'
            ),
            className="form-group d-flex"

        )
    ]

    return html.Article(rows, className="d-flex middle col form")
