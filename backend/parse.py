import json


def jsonPresupuesto(header, tuples):
    result = {}

    for tuple in tuples:
        # pares ordenados
        par = zip(header, tuple)
        # asignacion dinamica de las variables
        for key, value in par:
            globals()[key] = value

        if capitulo not in result:
            result[capitulo] = {}
        if subcapitulo not in result[capitulo]:
            result[capitulo][subcapitulo] = {}
        if item not in result[capitulo][subcapitulo]:
            result[capitulo][subcapitulo][item] = {}
        if insumo not in result[capitulo][subcapitulo][item]:
            result[capitulo][subcapitulo][item][insumo] = {
                'id': id,
                'cantidad': rendimiento,
                'rendimiento': rendimiento,
                'valor_unitario': precio,
                'subtotal': subtotal
            }
    return result


# t = jsonPresupuesto(
#     ('id', 'insumo', 'item', 'subcapitulo', 'capitulo',
#         'cantidad', 'rendimiento', 'precio', 'subtotal'),
#     [
#         (1, 'Cemento portland', 'Excavación de zanjas para cimentación', 'Movimiento de tierras',
#          'Preparación del terreno', '10.00', '0.25', '$ 1,5000.00', '$ 3,7500.00'),
#         (2, 'Arena', 'Excavación de zanjas para cimentación', 'Movimiento de tierras',
#          'Preparación del terreno', '5.00', '0.10', '$ 8,0000.00', '$ 4,0000.00'),
#         (5, 'Cal', 'Mampostería de cerramiento de bloque de concreto', 'Mampostería de cerramiento',
#          'Mampostería', '2000.00', '0.15', '$ 12,0000.00', '$ 3,600,0000.00'),
#         (1, 'Cemento portland', 'Zapata aislada de hormigón armado', 'Zapatas aisladas',
#          'Cimentación', '100.00', '0.10', '$ 1,5000.00', '$ 15,0000.00')
#     ]
# )

# print(t)
