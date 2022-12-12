import mysql.connector
# pip install mysql-connector-python
#                  DB_HOST='bsi5brxpk0wz9ygdti6z-mysql.services.clever-cloud.com',
#                  DB_USER='ulgg0or7rymoucea',
#                  DB_PASS='KbmgO9lZCsLyLnKgWcGa',
#                  DB_NAME='bsi5brxpk0wz9ygdti6z',
#                  DB_PORT='3306'


class Conexion:
    def __init__(self,
                 DB_HOST='byesikch2cyefw2pvcqg-mysql.services.clever-cloud.com',
                 DB_USER='urplxlscfyqjee1o',
                 DB_PASS='Fp35RY3YeLEk6Ql0nnXJ',
                 DB_NAME='byesikch2cyefw2pvcqg',
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
            print("la cosa se jodio")

    def is_connected(self):
        return self._is_connected

    def run_query(self, query=''):
        data = None
        try:
            if self.is_connected():
                self._cursor.execute(query)
                if query.upper().startswith('SELECT'):
                    data = self._cursor.fetchall()
                else:
                    self._conexion.commit()
        except:
            self._conexion.rollback()
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
        # if consulta.run_query("SELECT * FROM bsi5brxpk0wz9ygdti6z.users_db WHERE user = 'admin'"):
        #    print(consulta.run_query("SELECT password FROM bsi5brxpk0wz9ygdti6z.users_db WHERE type = '0'"))
        consulta._cursor.execute("SHOW DATABASEs")
        for db in consulta._cursor:
            print(db)
        consulta.close()

    if not consulta.is_connected(): print("cerrada")
