import sqlite3
import pandas as pd
#Conecta ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect('BDRelacional.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")
conn.commit() #Salvar as alterações feita no banco de dados
#======================================================================
# FUNÇÂO DO SISTEMA
#======================================================================
def inserir_departamento():
    print("\n INSERIR NOVO USUARIO")
    nome_usuario = input("Digite o nome do usuario: ")
    if nome_usuario.strip() == "":
        print("Erro: o nome não pode ser vazio!")
        return

    #Inserir com segurança usando Placeholders(?)
    #para evitar SQL Injector
    cursor.execute("INSERT INTO departamentos (nome) VALUES (?)",
                   (nome_usuario,))
    conn.commit()
    print(f"Sucesso: Usuario {nome_usuario} cadastrado")

def listar_com_for():
    print("\n LISTAR COM FOR")
    cursor.execute("SELECT id, nome  FROM departamentos")
    linhas = cursor.fetchall() #Mostra todas as linha da tabela

    if not linhas:
        print("Nenhuma usuario cadastrada")

    for linha in linhas:
        print(f"ID: {linha[0]}, Nome: {linha[1]}")


def lista_com_pandas():
    print("\n LISTAR COM Pandas")
    df = pd.read_sql_query("SELECT id AS 'ID', nome AS 'Nome de usuario'"
                           "FROM departamentos", conn)
    if df.empty:
        print('Nenhum usuario encontrado.')
    else:
        print(df.to_string(index=False))

while True:
    print("\n" + "="*30)
    print("     SISTEMA DE USUARIOS")
    print("\n" + "=" * 30)
    print("[1] Inserir usuario")
    print("[2] Listar com for")
    print("[3] Listar pandas")
    print("[4] Sair")
    print("=" * 30)
    opcao = input('Escolha a opção: ')
    if opcao == '1':
        inserir_departamento()
    elif opcao == '2':
        listar_com_for()
    elif opcao == '3':
        lista_com_pandas()
    elif opcao == '4':
        print("\nSaindo do sistema... Até logo!")
        break
    else:
        print("\nOpção inválida! tente novamente!")
conn.close()