from dash import html


def layout(size=2, primary="#43A047", secondary="#263238"):
    """
    Genera el layout del logotipo.

    Args:
        size (int): Tamaño del logotipo. Por defecto es 2.
        primary (str): Color primario del logotipo. Por defecto es "#43A047".
        secondary (str): Color secundario del logotipo. Por defecto es "#263238".

    Returns:
        html.Div: Un elemento Div que contiene los componentes Span del logotipo.
    """
    return html.Div(
        [
            html.Span('G', style={'color': primary}),
            html.Span('es', style={'color': secondary}),
            html.Span('P', style={'color': primary}),
            html.Span('res', style={'color': secondary}),
            html.Span('O', style={'color': primary}),
        ],
        className="logo",
        style={'fontSize': str(16*size)+'px'}
    )
