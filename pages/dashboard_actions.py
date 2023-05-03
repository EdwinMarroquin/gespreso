import dash

dash.register_page(
    __name__, name="dashboard", path_template='/dashboard/<database>/<action>/<code>')


def layout(database=None, action=None, code=None, **other_unknown_query_strings):
    if database == 'insumos':
        tb = "ver_grupos_insumos"
        if action == 'ver':
            return
        if action == 'editar':
            return
        if action == 'eliminar':
            return
