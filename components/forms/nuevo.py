import dash
from dash import html, dcc
from db import database


def unidades(table_name):
    """
    Genera una estructura HTML para crear una nueva unidad.

    Args:
        table_name (str): Nombre de la tabla.

    Returns:
        dash.html.Article: Estructura HTML para la creación de la unidad.
    """
    db = database.DB()
    info = db.read_all('sqlite_sequence')
    last_id = int([i[1] for i in info if i[0] == table_name][0])

    rows = [
        dcc.Location(id='url', refresh=True),
        html.H1(
            'Creacion de nueva unidad',
            className='form-title'
        ),
        html.P([
            html.Label(
                'ID',
                className='form-group-label',
            ),
            html.Div([
                dcc.Input(
                    id='id',
                    value=f'{last_id + 1}',
                    disabled=True,
                    className='form-group-label',
                )
            ], className="dash-input")
        ], className='form-group'),
        html.P([
            html.Label(
                'Unidad',
                className='form-group-label'
            ),
            html.Div([
                dcc.Input(
                    className='form-group-input',
                    id='nombre'
                )
            ], className="dash")
        ], className='form-group'),
        html.P([
            html.Label(
                'Abreviatura',
                className='form-group-label'
            ),
            html.Div([
                dcc.Input(
                    className='form-group-input',
                    id='abreviatura'
                )
            ], className="dash")
        ], className='form-group'),
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Crear insumo")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonSaveunidades'
            ),
            className="form-group d-flex"
        )
    ]

    return html.Article(rows, className="d-flex middle col form")


def insumos(table_name):
    """
    Genera una estructura HTML para la creación de un nuevo insumo.

    Args:
        table_name (str): Nombre de la tabla de insumos.

    Returns:
        dash.html.Article: Estructura HTML para la creación del insumo.
    """
    db = database.DB()
    info = db.read_all('sqlite_sequence')
    insumos = db.custom_read(table_name, '*')
    unidades = db.read_all('unidades')
    grupos = db.read_all('grupos')
    last_id = int([i[1] for i in info if i[0] == table_name][0])
    rows = []

    rows.append(dcc.Location(id='url', refresh=True))
    rows.append(
        html.H1(
            f'Creacion de nuevo insumo',
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
                            id=input_value,
                            value=f'{last_id + 1}',
                            disabled=True,
                            className='form-group-label',
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
                            className='form-group-input',
                            id=f'{input_value}'
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
                            className='form-group-input',
                            id=f'{input_value}'
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
                                className='form-group-input',
                                id=f'{input_value}'
                            )
                        ], className="dash")
                    ], className='form-group')
                )

    rows.append(
        html.P(
            html.Div(
                [
                    html.I(className="bi bi-box"),
                    html.Span("Crear insumo")
                ],
                className="btn btn-large btn-dark",
                style={'margin': '2rem 0 1rem auto'},
                id='buttonSave'
            ),
            className="form-group d-flex"
        )
    )

    return html.Article(rows, className="d-flex middle col form")
