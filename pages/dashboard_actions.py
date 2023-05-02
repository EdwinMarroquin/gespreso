import dash

dash.register_page(
    __name__, path_template='/dashboard/<database>/<action>/<code>')


def layout(database=None, action=None, code=None, **other_unknown_query_strings):
    return dash.html.Div([
        dash.html.Div(
            f"Base de datos: {database} - Accion: {action} - Codigo: {code}")
    ])
