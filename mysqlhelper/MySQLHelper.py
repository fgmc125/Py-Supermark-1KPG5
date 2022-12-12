from mysqlhelper.Conector import Conexion


class MySQLHelper:
    def __init__(self):
        self._connector = None

    def user_list(self):
        data = list()
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT id,nombre, apellido, id_tipo_usuario, email, fecha_acceso FROM byesikch2cyefw2pvcqg.usuario"
            data = list(self._connector.run_query(sql))

            lista = list()
            for i in range(len(data)):
                data[i] = list(data[i])
                if not str(data[i][3]) in lista:
                    lista.append(str(data[i][3]))

            sql = "SELECT id, descripcion FROM byesikch2cyefw2pvcqg.tipo_usuario where id in (" + ",".join(lista) + ");"
            aux = self._connector.run_query(sql)

            for i in range(len(data)):
                for j in range(len(aux)):
                    if data[i][3] == aux[j][0]: data[i][3] = aux[j][1]
        return data

    def student_list(self):
        data = list()
        self._connector = Conexion()
        if self._connector.is_connected():
            sql = "SELECT * FROM byesikch2cyefw2pvcqg.estudiantes_cursada"
            data = self._connector.run_query(sql)
        return data
