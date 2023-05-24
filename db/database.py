import sqlite3


class DB:
    def __init__(self):
        """
        Inicializa una instancia de la clase y establece
        la conexión con la base de datos.

        Raises:
            sqlite3.OperationalError: Error al abrir la
            conexión con la base de datos.
        """
        try:
            self.conn = sqlite3.connect(
                "./gespreso/db/gespreso.db",
                check_same_thread=False
            )
            self.cursor = self.conn.cursor()
        except sqlite3.OperationalError as error:
            print("Error al abrir la conexión:", error)

    def close(self):
        """
        Cierra la conexión con la base de datos y el cursor.

        Esta función debe ser llamada al finalizar las operaciones
        con la base de datos para liberar los recursos y cerrar la conexión.

        """
        self.cursor.close()
        self.conn.close()

    def info_table(self, table_name):
        """
        Obtiene información sobre las columnas de una tabla especificada.

        Args:
            table_name (str): Nombre de la tabla.

        Returns:
            list: Lista de tuplas con información de las columnas.
                Cada tupla contiene los siguientes elementos:
                - cid (int): ID de la columna.
                - name (str): Nombre de la columna.
                - type (str): Tipo de datos de la columna.
                - notnull (int): Indica si la columna permite valores nulos
                                (0 o 1).
                - dflt_value (str): Valor predeterminado de la columna.
                - pk (int): Indica si la columna es una clave primaria
                            (0 o 1).
        """
        query = f"PRAGMA table_info('{table_name}')"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create(self, table_name, data):
        """
        Crea un nuevo registro en la tabla especificada.

        Args:
            table_name (str): Nombre de la tabla.
            data (dict): Datos del registro en forma de diccionario.

        Returns:
            int: ID del registro creado.
        """
        placeholders = ', '.join('?' * len(data))
        columns = ', '.join(data.keys())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

        return self.cursor.lastrowid

    def read_all(self, table_name):
        """
        Devuelve todos los registros de una tabla especificada.

        Args:
            table_name (str): Nombre de la tabla.

        Returns:
            list: Lista de registros en forma de diccionarios.
        """
        query = f"SELECT * FROM {table_name}"

        self.cursor.execute(query)
        records = self.cursor.fetchall()

        return records

    def read_one(self, table_name, record_id):
        """
        Devuelve el registro con el ID especificado de la tabla especificada.

        Args:
            table_name (str): Nombre de la tabla.
            record_id: ID del registro.

        Returns:
            dict or None: Registro en forma de diccionario si se encuentra,
                          o None si no se encuentra.
        """

        query = f"SELECT * FROM {table_name} WHERE id=?"

        self.cursor.execute(query, (record_id,))
        record = self.cursor.fetchone()

        if record:
            # return self._convert_to_dict(record)
            return record
        else:
            return None

    def custom_read(self, table_name=None, columns=None, where=None, order_by=None, group_by=None):
        """
        Devuelve los registros de una tabla específica según
        los parámetros de consulta.

        Args:
            table_name (str): Nombre de la tabla.
            columns (str or None): Columnas a seleccionar. Si es None,
                                   se seleccionarán todas las columnas.
            where (str or None): Condición de consulta WHERE.
            order_by (str or None): Orden de los resultados.
            group_by (str or None): Agrupamiento de los resultados.

        Returns:
            dict: Diccionario con información de los registros y columnas.
                - 'lastId' (int): Último ID insertado.
                - 'records' (list): Lista de registros en forma de diccionarios.
                - 'columns' (tuple): Tupla con los nombres de las columnas.
        """
        str_columns = f'{columns}' if columns != None else "*"
        str_where = f"WHERE {where}" if where != None else ""
        str_order_by = f"ORDER BY {order_by}" if order_by != None else ""
        str_group_by = f"GROUP BY {group_by}" if group_by != None else ""

        query = f"SELECT {str_columns} FROM {table_name} {str_where} {str_group_by} {str_order_by}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        return {
            'lastId': self.cursor.lastrowid,
            'records': records,
            'columns': next(zip(*self.cursor.description))
        }

    def update(self, table_name, record_id, data):
        """
        Actualiza un registro específico en una tabla de datos con los
        nuevos valores proporcionados.

        Args:
            table_name (str): Nombre de la tabla de datos.
            record_id (int): ID del registro que se desea actualizar.
            data (dict): Diccionario que contiene los nuevos valores para
                         las columnas a actualizar.
        """
        set_clause = ', '.join([f"{key}=?" for key in data.keys()])
        set_data = tuple(data.values()) + (int(record_id),)

        query = f"UPDATE {table_name} SET {set_clause} WHERE id=?"

        self.cursor.execute(
            query,
            set_data
        )
        self.conn.commit()

    def delete(self, table_name, record_id):
        """
        Elimina un registro específico de una tabla de datos.

        Args:
            table_name (str): Nombre de la tabla de datos.
            record_id (int): ID del registro que se desea eliminar.
        """
        query = f"DELETE FROM {table_name} WHERE id={int(record_id)}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_with_conditions(self, table_name, conditions):
        """
        Eliminar uno o varios registros de una tabla de datos segun
        se cumplan las condiciones dadas

        Args:
            table_name (str): Nombre de la tabla de datos
            conditions (dict): Condiciones de consulta
        """
        where_conditions = ' and '.join(
            [
                f"{columna} = {valor}" for columna, valor in conditions.items()
            ]
        )
        query = f"delete from {table_name} where {where_conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def _sanitize_data(self, data):
        """
        Sanitiza los datos del registro para evitar inyección de código.
        :param data: datos del registro en forma de diccionario
        :return: datos sanitizados
        """
        sanitized_data = {}
        for key, value in data.items():
            sanitized_data[key] = sqlite3.escape_string(str(value))
        return sanitized_data

    def _convert_to_dict(self, record):
        """
        Convierte un registro de SQLite en un diccionario.
        :param record:
        """
        return {
            'id': record[0],
            'column1': record[1],
            'column2': record[2],
            # Añadir más columnas según la tabla
        }

# db = DB('database.db')

# # Crear un registro
# data = {'column1': 'valor1', 'column2': 'valor2'}
# record_id = db.create('mi_tabla', data)

# # Leer todos los registros
# records = db.read_all('mi_tabla')

# # Leer un registro específico
# record = db.read_one('mi_tabla', record_id)

# # Actualizar un registro
# data = {'column1': 'nuevo_valor1', 'column2': 'nuevo_valor2'}
# db.update('mi_tabla', record_id, data)

# # Eliminar un registro
# db.delete('mi_tabla', record_id)
