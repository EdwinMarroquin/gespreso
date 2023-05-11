import dash
from dash import dcc, Input, Output, State


def show_body_tables(app):
    for i in range(1, 6):
        @app.callback(
            Output(f'bodyTable{i}', 'style'),
            Output(f'headTable{i}', 'style'),
            Output(f'buttonTable{i}', 'className'),
            Input(f'buttonTable{i}', 'n_clicks')
        )
        def show_hide(n_clicks):
            try:
                if n_clicks is None:
                    raise PreventUpdate
                else:
                    d = 'none' if (n_clicks %
                                   2) == 0 else 'table-row-group'
                    c = 'bi-list' if (n_clicks %
                                      2) == 0 else 'bi-view-list'

                return {'display': d}, {'display': d}, f"caption-action bi {c} "
            except:
                print("Error en el callback")
