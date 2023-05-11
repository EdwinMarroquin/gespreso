import dash
from dash import html


def layout():
    links = [
        {
            "icon": "bi-columns-gap",
            "label": "UNIDADES",
            "url": "./unidades"
        },
        {
            "icon": "bi-box-seam",
            "label": "INSUMOS",
            "url": "./insumos"
        },
        {
            "icon": "bi-boxes",
            "label": "ITEMS",
            "url": "./items"
        },
        {
            "icon": "bi-bricks",
            "label": "SUBCAPÍTULOS",
            "url": "./subcapitulos"
        },
        {
            "icon": "bi-bricks",
            "label": "CAPÍTULOS",
            "url": "./capitulos"
        },
        {
            "icon": "bi-building",
            "label": "PRESUPUESTOS",
            "url": "./presupuestos"
        }
    ]

    paths = [html.A([html.I(className="card-icon " + link["icon"]), html.Span(link["label"],
                    className="card-label"), ], href=link["url"], className="card") for link in links]

    return html.Article(
        children=paths,
        className="welcome"
    )
