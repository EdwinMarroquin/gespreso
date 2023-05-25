import dash
import flask
from flask import redirect, request
from dash import dcc, Input, Output, State
from db import database


def redirect_after_delete():
    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input('deleteItem', 'n_clicks'),
        [State('deleteItem', 'data-database'),
         State('deleteItem', 'data-code')],
        prevent_initial_call=True
    )
    def eliminar_registro(n_clicks, table_name, record_id):
        if n_clicks is not None:
            db = database.DB()
            db.delete(table_name, record_id)
            return f'/dashboard/{table_name}'


def redirect_after_update():
    db = database.DB()
    data = db.custom_read('insumos')
    columns = data["columns"]

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input('buttonUpdate', 'n_clicks'),
        [State(f'{col}', 'value') for col in columns],
        prevent_initial_call=True
    )
    def actualizar_registro(n_clicks, id, descripcion, unidad_id, grupo_id):
        if n_clicks is not None:
            data = {
                'id': id,
                'descripcion': descripcion,
                'unidad_id': unidad_id,
                'grupo_id': grupo_id
            }

            db.update(
                table_name='insumos',
                record_id=id,
                data=data
            )
        return f'/dashboard/insumos/'


def redirect_after_update_unidades():
    db = database.DB()
    data = db.custom_read('unidades')
    columns = data["columns"]

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input(f'buttonUpdateunidades', 'n_clicks'),
        [State(f'{col}', 'value') for col in columns],
        prevent_initial_call=True
    )
    def crear_registro(n_clicks, id, nombre, abreviatura):
        data = {
            'id': id,
            'nombre': nombre,
            'abreviatura': abreviatura,
        }

        if n_clicks is not None:
            if data["nombre"] or data["abreviatura"]:
                db.update(
                    table_name='unidades',
                    record_id=id,
                    data=data
                )
            else:
                print('Error en la informacion')

        return f'/dashboard/unidades/'


def redirect_after_save():
    db = database.DB()
    data = db.custom_read('insumos')

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input('buttonSave', 'n_clicks'),
        [State(f'{col}', 'value') for col in data["columns"]],
        prevent_initial_call=True
    )
    def crear_registro(n_clicks, id, descripcion, unidad_id, grupo_id):
        data = {
            'id': id,
            'descripcion': descripcion,
            'unidad_id': unidad_id,
            'grupo_id': grupo_id
        }

        if n_clicks is not None:

            if data["descripcion"] or data["unidad_id"] or data["grupo_id"]:
                db.create(
                    table_name='insumos',
                    data=data
                )
            else:

                print('Error en la informacion')
        return f'/dashboard/insumos/'


def redirect_after_save_custom(table_name):
    db = database.DB()
    data = db.custom_read(table_name)

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input(f'buttonSave{table_name}', 'n_clicks'),
        [State(f'{col}', 'value') for col in data["columns"]],
        prevent_initial_call=True
    )
    def crear_registro(n_clicks, id, nombre, abreviatura):
        data = {
            'id': id,
            'nombre': nombre,
            'abreviatura': abreviatura,
        }

        if n_clicks is not None:

            if data["nombre"] or data["abreviatura"]:
                db.create(
                    table_name=table_name,
                    data=data
                )
            else:

                print('Error en la informacion')
        return f'/dashboard/unidades/'


def update_after_change_select():
    db = database.DB()
    data = db.read_all('insumos')

    @dash.callback(
        Output('unidad', 'value', allow_duplicate=True),
        Input('insumo_id', "value"),
        prevent_initial_call=True
    )
    def update_units(insumo_id):
        if insumo_id is not None:
            insumo = next((i for i in data if i[0] == insumo_id), None)
            unidad = db.read_one('unidades', insumo[2])
            return unidad[2]
        else:
            return ''


def redirect_after_add():
    db = database.DB()
    data = db.custom_read('insumos')

    @dash.callback(
        Output('urlAdd', 'pathname', allow_duplicate=True),
        Input('buttonAdd', 'n_clicks'),
        [
            State('id_presupuesto', 'value'),
            State('apu_id', 'value'),
            State('insumo_id', 'value'),
            State('cantidad', 'value'),
            State('rendimiento', 'value'),
            State('precio', 'value'),
        ],
        prevent_initial_call=True
    )
    def nuevo_insumo_item(
            n_clicks,
            id_presupuesto,
            apu_id,
            insumo_id,
            cantidad,
            rendimiento,
            precio
    ):
        data = {
            'id_presupuesto': id_presupuesto,
            'apu_id': apu_id,
            'insumo_id': insumo_id,
            'cantidad': cantidad,
            'rendimiento': rendimiento,
            'precio': precio,
        }
        if n_clicks is not None:
            db.create('insumos_presupuesto', data)
            return f'accion/guardando:dashboard/items/editar/{apu_id}'


def redirect_previously():
    @dash.callback(
        Output('urlRedirect', 'pathname'),
        Input('inputRedirect', "value")
    )
    def update_units(inputRedirect):
        if inputRedirect:
            return f'/{inputRedirect}'


def eliminar_insumo_item():
    db = database.DB()
    data = db.custom_read('insumos')
    insumos = data["records"]
    for i in insumos:
        @dash.callback(
            Output('urlAdd', 'pathname', allow_duplicate=True),
            Input(f'eliminar_insumo_item_{i[0]}', 'n_clicks'),
            [
                State(f'eliminar_insumo_item_{i[0]}', 'data-apu'),
                State(f'eliminar_insumo_item_{i[0]}', 'data-insumo')
            ],
            prevent_initial_call=True
        )
        def eliminar_insumo(n_clicks, data_apu, data_insumo):
            if n_clicks:
                db.delete_with_conditions(
                    'insumos_presupuesto',
                    {
                        'insumo_id': data_insumo,
                        'apu_id': data_apu
                    }
                )
            return f'/accion/eliminar:dashboard/items/editar/{data_apu}'


def redirect_after_update_subcapitulos():
    db = database.DB()
    data = db.custom_read('subcapitulos')
    columns = data["columns"]

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input(f'buttonUpdatesubcapitulo', 'n_clicks'),
        [State(f'{col}', 'value') for col in columns],
        prevent_initial_call=True
    )
    def actualizar_registro(n_clicks, id, nombre, capitulo_id):
        data = {
            'id': id,
            'nombre': nombre,
            'capitulo_id': capitulo_id,
        }

        if n_clicks is not None:
            if data["nombre"] or data["capitulo_id"]:
                db.update(
                    table_name='subcapitulos',
                    record_id=id,
                    data=data
                )
            else:
                print('Error en la informacion')

        return f'/dashboard/subcapitulos/'


def redirect_after_update_capitulos():
    db = database.DB()
    data = db.custom_read('capitulos')
    columns = data["columns"]

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input(f'buttonUpdatecapitulo', 'n_clicks'),
        [State(f'{col}', 'value') for col in columns],
        prevent_initial_call=True
    )
    def actualizar_registro(n_clicks, id, nombre):
        data = {
            'id': id,
            'nombre': nombre,
        }

        if n_clicks is not None:
            if data["nombre"] or data["capitulo_id"]:
                db.update(
                    table_name='capitulos',
                    record_id=id,
                    data=data
                )
            else:
                print('Error en la informacion')

        return f'/dashboard/capitulos/'


def redirect_after_save_capitulo():
    db = database.DB()
    data = db.custom_read('capitulos')

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input('buttonSavecapitulo', 'n_clicks'),
        [State(f'{col}', 'value') for col in data["columns"]],
        prevent_initial_call=True
    )
    def crear_registro(n_clicks, id, nombre):
        data = {
            'id': id,
            'nombre': nombre,
        }

        if n_clicks is not None:

            if data["id"] or data["nombre"]:
                db.create(
                    table_name='capitulos',
                    data=data
                )
            else:

                print('Error en la informacion')
        return f'/dashboard/capitulos/'


def redirect_after_save_subcapitulo():
    db = database.DB()
    data = db.custom_read('subcapitulos')

    @dash.callback(
        Output('url', 'pathname', allow_duplicate=True),
        Input('buttonSavesubcapitulo', 'n_clicks'),
        [State(f'{col}', 'value') for col in data["columns"]],
        prevent_initial_call=True
    )
    def crear_registro(n_clicks, id, nombre, capitulo_id):
        data = {
            'id': id,
            'nombre': nombre,
            'capitulo_id': capitulo_id,
        }

        if n_clicks is not None:

            if data["id"] or data["nombre"] or data["capitulo_id"]:
                db.create(
                    table_name='subcapitulos',
                    data=data
                )
            else:

                print('Error en la informacion')
        return f'/dashboard/subcapitulos/'
