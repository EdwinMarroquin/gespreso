import sqlite3


class DB:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("./gespreso/db/gespreso.db")
            self.cursor = self.conn.cursor()
        except sqlite3.OperationalError as error:
            print("Error al abrir:", error)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def info_table(self, table_name):
        query = f"PRAGMA table_info('{table_name}')"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create(self, table_name, data):
        """
        Crea un nuevo registro en la tabla especificada.
        :param table_name: nombre de la tabla
        :param data: datos del registro en forma de diccionario
        :return: el ID del registro creado
        """
        sanitized_data = self._sanitize_data(data)
        placeholders = ', '.join('?' * len(sanitized_data))
        columns = ', '.join(sanitized_data.keys())

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        self.cursor.execute(query, tuple(sanitized_data.values()))
        self.conn.commit()

        return self.cursor.lastrowid

    def read_all(self, table_name):
        """
        Devuelve todos los registros de la tabla especificada.
        :param table_name: nombre de la tabla
        :return: lista de registros en forma de diccionarios
        """
        query = f"SELECT * FROM {table_name}"

        self.cursor.execute(query)
        records = self.cursor.fetchall()

        # return [self._convert_to_dict(record) for record in records]
        return records

    def read_one(self, table_name, record_id):
        """
        Devuelve el registro con el ID especificado de la tabla especificada.
        :param table_name: nombre de la tabla
        :param record_id: ID del registro
        :return: registro en forma de diccionario
        """

        query = f"SELECT * FROM {table_name} WHERE id=?"

        self.cursor.execute(query, (record_id,))
        record = self.cursor.fetchone()

        if record:
            return self._convert_to_dict(record)
        else:
            return None

    def update(self, table_name, record_id, data):
        """
        Actualiza el registro con el ID especificado en la tabla especificada.
        :param table_name: nombre de la tabla
        :param record_id: ID del registro
        :param data: nuevos datos del registro en forma de diccionario
        """
        sanitized_data = self._sanitize_data(data)
        set_clause = ', '.join([f"{key}=?" for key in sanitized_data.keys()])

        query = f"UPDATE {table_name} SET {set_clause} WHERE id=?"

        self.cursor.execute(query, tuple(
            sanitized_data.values()) + (record_id,))
        self.conn.commit()

    def delete(self, table_name, record_id):
        """
        Elimina el registro con el ID especificado de la tabla especificada.
        :param table_name: nombre de la tabla
        :param record_id: ID del registro
        """
        query = f"DELETE FROM {table_name} WHERE id=?"

        self.cursor.execute(query, (record_id,))
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
