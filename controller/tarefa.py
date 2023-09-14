import mysql.connector

# Conexão com o banco
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RafaelSouto17",
    database="tarefas"
)
cursor = banco.cursor()

# cursor.execute("CREATE DATABASE tarefas")
# cursor.execute("CREATE TABLE IF NOT EXISTS tarefas(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR (255), concluido BOOLEAN)")


# Adição

def adicionar(i):
    sql = "INSERT INTO tarefas (descricao, concluido) VALUES (%s, %s)"

    valores = (i, False)
    cursor.execute(sql, valores)
    banco.commit()


# Ver tarefas
def ver_tarefas():
    sql = "SELECT * FROM tarefas"
    cursor.execute(sql)
    return cursor.fetchall()


# Marcar
def marcar_tarefa(id, concluido):
    cursor = banco.cursor()
    cursor.execute(f"UPDATE tarefas SET concluido={concluido} WHERE id={id}")
    banco.commit()


# Deletar
def deletar(id_tarefa):
    sql = "DELETE FROM tarefas WHERE id = %s"
    valores = (id_tarefa,)
    cursor.execute(sql, valores)
    banco.commit()


# Selecionar o id
def selecionar_id(id):
    cursor.execute("""
            SELECT * FROM tarefas WHERE id = '%s'
    """ % (id))
    recset = cursor.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows
