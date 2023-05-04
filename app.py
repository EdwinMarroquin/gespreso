import dash
from dash import html, Input, Output, State

app = dash.Dash(__name__, use_pages=True,
                external_scripts=[{
                    'src': '/assets/js/tables.js'
                }])

app.layout = html.Div(
    children=[dash.page_container])
# children=[dash.page_container])

for i in range(1, 6):
    @app.callback(
        Output(f'tableBody{i}', 'style'),
        Output(f'tableHead{i}', 'style'),
        Output(f'buttonTable{i}', 'className'),
        Input(f'buttonTable{i}', 'n_clicks'),
    )
    def show_hide(n_clicks):
        display = 'none' if (n_clicks % 2) == 0 else 'table-row-group'
        classStyle = 'bi-list' if (n_clicks % 2) == 0 else 'bi-view-list'
        return {'display': display}, {'display': display}, f"caption-action bi {classStyle} "

if __name__ == "__main__":
    app.run_server(debug=True, port="8088", dev_tools_prune_errors=True)
