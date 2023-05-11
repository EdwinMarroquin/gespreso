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
    for index_presupuesto, valor_presupuesto in enumerate(presupuesto):
        caps_presupuesto = []
        caps = presupuesto[valor_presupuesto]

        for indice_cap, valor_cap in enumerate(caps):
            subcaps_presupuesto = []
            subcaps = caps[valor_cap]

            for indice_subcap, valor_subcap in enumerate(subcaps):
                items_presupuesto = []
                items = subcaps[valor_subcap]

                for indice_item, valor_item in enumerate(items):
                    insumos_presupuesto = []
                    insumos = items[valor_item]

                    for indice_insumo, valor_insumo in enumerate(insumos):
                        insumos_presupuesto.append(
                            html.Div(f'------ {valor_insumo} : {insumos[valor_insumo]}'))

                    items_presupuesto.append(html.Div(['----- ', valor_item]))
                    items_presupuesto.append(html.Div(insumos_presupuesto))

                subcaps_presupuesto.append(html.Div(['----', valor_subcap]))
                subcaps_presupuesto.append(html.Div(items_presupuesto))

            caps_presupuesto.append(html.Div(['---', valor_cap]))
            caps_presupuesto.append(html.Div(subcaps_presupuesto))

        pres.append(html.Div(['--', valor_presupuesto]))
        pres.append(html.Div(caps_presupuesto))

    return pres
    # return (html.Pre(html.Code(str(parse.jsonPresupuesto(info, presupuesto)))))
    # return html.Article(
    #     [
    #         table.generate(
    #             table='ver_insumos_presupuesto',
    #             context='presupuestos',
    #             actions={'ver': True, 'editar': True, 'eliminar': False}
    #         )
    #     ],
    #     className='presupuestos'
    # )
