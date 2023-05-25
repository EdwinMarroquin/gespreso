import dash
import backend
from dash import html, dcc
from flask import redirect
from backend import tables as btb
from backend import database as bdb


app = dash.Dash(
    __name__,
    use_pages=True,
    update_title=None,
    suppress_callback_exceptions=True,
)

app.layout = dash.page_container

app.title = 'Gespreso'

btb.show_body_tables()
dbd.redirect_after_delete()
dbd.redirect_after_update()
dbd.redirect_after_save()
dbd.redirect_after_save_custom('unidades')
dbd.redirect_after_update_unidades()
dbd.update_after_change_select()
dbd.redirect_after_add()
dbd.redirect_previously()
dbd.eliminar_insumo_item()
dbd.redirect_after_update_subcapitulos()
dbd.redirect_after_update_capitulos()
dbd.redirect_after_save_capitulo()
dbd.redirect_after_save_subcapitulo()


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8088, debug=True)
