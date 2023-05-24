import dash
import flask
from flask import redirect, request
from dash import html, dcc

dash.register_page(
    __name__,
    path_template='/accion/<url>',
    title='Gespreso - Tablas'
)


def layout(url):

    accions = url.split(':')
    accion = accions[0]
    url = accions[1]

    color_map = {
        'guardar': ('success', 'save', 'guardando'),
        'editar': ('info', 'info-circle', 'editando'),
        'eliminar': ('danger', 'exclamation-circle', 'eliminando')
    }
    color_accion, icon_accion, text_accion = color_map.get(
        accion, ('accent', 'check-circle', 'leyendo'))

    return html.Div(
        [html.H1(
            [
                html.I(className=f'bi bi-{icon_accion}'),
                html.Span(f'{text_accion}', style={
                          'text-transform': 'uppercase'})
            ], className=f"btn btn-large btn-{color_accion}"),
            dcc.Location(id="urlRedirect", refresh=True),
            dcc.Input(id="inputRedirect", value=url, type="hidden")
         ]
    )
