import dash
from dash import html


def layout():
    """
    Genera el layout de la barra de navegación.

    Returns:
        html.Nav: Un elemento Nav que contiene los elementos de la barra de navegación.
    """
    routes = [
        {
            'route': '/dashboard/inicio',
            'class_name': 'bg-text-dark',
            'label': 'Inicio',
            'icon': 'bi bi-house'
        },
        # {
        #     'route': '/dashboard/informes',
        #     'class_name': 'bg-text-dark',
        #     'label': 'Informes',
        #     'icon': 'bi bi-journal-richtext'
        # },
        {
            'route': 'https://github.com/EdwinMarroquin/gespreso/issues',
            'class_name': 'last bg-text-accent',
            'target': '_new',
            'label': 'Errores/Sugerencias',
            'icon': 'bi bi-bug'
        }
    ]

    return html.Nav(
        children=[
            html.Div(
                children=[
                    html.A(
                        children=[
                            html.I(className=route.get('icon')),
                            html.Span(route.get('label'))
                        ],
                        href=route.get('route'),
                        className=route.get('class_name'),
                        target=route.get('target')
                    ) for route in routes
                ]
            )
        ],
        className="nav"
    )
