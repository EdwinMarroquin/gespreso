import dash
from dash import html, dcc
from db import database


def layout(table_name, record_id):
    db = database.DB()

    info = db.read_one(table_name, record_id)

    return html.A(
        [
            dcc.Location(id="url", refresh=True),
            html.I(
                className="bi bi-trash padding-xl",
                style={"font-size": "5rem"}
            ),
            html.Span(
                [
                    html.Table(
                        [
                            html.Caption('ELIMINAR REGISTRO'),
                            html.Thead(
                                html.Tr([
                                    html.Th('ITEM'),
                                    html.Th('VALOR'),
                                ])
                            ),
                            html.Tbody([
                                html.Tr(
                                    [html.Td('ID'), html.Td(info[0])]),
                                html.Tr(
                                    [html.Td('TABLA'), html.Td(table_name)]),
                                html.Tr(
                                    [html.Td('VALOR'), html.Td(info[1])]),
                            ])
                        ]),
                ]
            )
        ],
        **{'data-database': table_name, 'data-code': record_id},
        className="btn btn-large bg-text-danger",
        id="deleteItem"
    )
