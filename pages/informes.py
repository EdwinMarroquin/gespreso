import dash
from dash import html


def layout():
    links = [
        {
            "icon": "bi-box-seam",
            "label": "GRUPO INSUMOS",
            "url": "./grupos"
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
                    className="card-label"), ], href=link["url"], className="card bg-text-dark") for link in links]

    return html.Article(
        children=paths,
        className="welcome"
    )
