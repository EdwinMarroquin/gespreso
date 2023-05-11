import dash
import backend
from dash import html, dcc
from flask import redirect
from backend import tables

app = dash.Dash(__name__, use_pages=True,
                suppress_callback_exceptions=True)


app.layout = html.Div(
    children=[dash.page_container])

tables.show_body_tables(app)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088, debug=True)
