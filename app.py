import dash
import backend
from dash import html, dcc
from flask import redirect
from backend import tables
from backend import database
1

app = dash.Dash(
    __name__,
    use_pages=True,
    update_title=None,
    suppress_callback_exceptions=True,
)

app.layout = dash.page_container

app.title = 'Gespreso'

backend.tables.show_body_tables()
backend.database.redirect_after_delete()
backend.database.redirect_after_update()
backend.database.redirect_after_save()
backend.database.redirect_after_save_custom('unidades')
backend.database.redirect_after_update_unidades()
backend.database.update_after_change_select()
backend.database.redirect_after_add()
backend.database.redirect_previously()
backend.database.eliminar_insumo_item()
backend.database.redirect_after_update_subcapitulos()
backend.database.redirect_after_update_capitulos()


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088, debug=True)
