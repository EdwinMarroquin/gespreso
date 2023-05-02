from app import app
from index import *
from dashboard import *

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.pages
    else:
        return index.layout


if __name__ == '__main__':
    app.run_server()
