from dash import html


def layout(size=2, primary="#43A047", secondary="#263238"):
    return html.Div([
        html.Span('G', style={'color': primary}),
        html.Span('es', style={'color': secondary}),
        html.Span('P', style={'color': primary}),
        html.Span('res', style={'color': secondary}),
        html.Span('O', style={'color': primary}),
    ], className="logo", style={'fontSize': str(16*size)+'px'})
