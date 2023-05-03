import dash
from dash import html

app = dash.Dash(__name__, use_pages=True,
                external_scripts=['./gespreso/assets/js/tables.js'])

app.scripts.config.serve_locally = True
app.scripts.config.eager_loading = True

app.layout = html.Div(dash.page_container)

if __name__ == "__main__":
    app.run_server(debug=True, port="8088")
