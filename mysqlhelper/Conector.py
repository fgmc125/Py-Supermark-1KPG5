import mysql.connector


# pip install mysql-connector-python
#                  DB_HOST='bsi5brxpk0wz9ygdti6z-mysql.services.clever-cloud.com',
#                  DB_USER='ulgg0or7rymoucea',
#                  DB_PASS='KbmgO9lZCsLyLnKgWcGa',
#                  DB_NAME='bsi5brxpk0wz9ygdti6z',
#                  DB_PORT='3306'


class Conexion:
    def __init__(self,
                 DB_HOST='bhhj3cug6bdknptqdl7k-mysql.services.clever-cloud.com',
                 DB_USER='uk8uc4waiyp7kpnd',
                 DB_PASS='NzF8qVpKG6ClKY0vo6wk',
                 DB_NAME='bhhj3cug6bdknptqdl7k',
                 DB_PORT='3306'
                 ):
        self._is_connected = False
        try:
            self._conexion = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                port=DB_PORT,
                database=DB_NAME
            )
            self._cursor = self._conexion.cursor()
            self._is_connected = True
        except:
            print("Error al conectar a la base de datos")

    def is_connected(self):
        return self._is_connected

    def run_query(self, query='', data=None):
        #       try:
        if self.is_connected():
            self._cursor.execute(query, data)
            if query.upper().startswith('SELECT'):
                data = self._cursor.fetchall()
            else:
                self._conexion.commit()
        #       except:
        # print("error")
        # self._conexion.rollback()
        return data

    def close(self):
        if self.is_connected():
            self._cursor.close()
            self._conexion.close()
            self._is_connected = False


if __name__ == "__main__":
    consulta = Conexion()
    if consulta.is_connected():
        print("conectado")
        consulta._cursor.execute("SHOW DATABASES")
        for db in consulta._cursor:
            print(db)
        consulta.close()

    if not consulta.is_connected():
        print("cerrada")
