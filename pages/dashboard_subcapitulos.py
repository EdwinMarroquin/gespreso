import dash
from dash import html
from components import table


def layout():
    return html.Article(
        [
            table.generate(table='subcapitulos', context='subcapitulos')
        ],
        className='subcapitulos'
    )
