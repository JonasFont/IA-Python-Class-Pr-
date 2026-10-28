import sqlite3

conexao = sqlite3.connect("copa.db")

#Armazena dentro da variavel cursor todas as funções do sqlite3
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS selecoes(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    pais TEXT,
    grupo TEXT,
    ataque INTEGER,
    meio INTEGER,
    defesa INTEGER,
    tecnico TEXT
)""")
conexao.commit()

def cadastra():
    print("\n ==== CADASTRO DE SELEÇÕES ===")

    pais = input("País: ")
    grupo = input("Grupo: ")
    ataque = int(input("Ataque: "))
    meio = int(input("Meio: "))
    defesa = int(input("Defesa: "))
    tecnico = input("Técnico: ")

    cursor.execute("""
        INSERT INTO selecoes (pais, grupo, ataque, meio, defesa, tecnico)
         VALUES (?, ?, ?, ?, ?, ?)
    """, (pais, grupo, ataque, meio, defesa, tecnico))
    conexao.commit()

    print("\nSeleções cadastrada!\n")


def listar():
    cursor.execute("""SELECT * FROM selecoes""")
    dados = cursor.fetchall() #Lista todos os valores do db
    print("\n===== SELEÇÕES =====")

    for linha in dados:
        print(linha)


def atualizar():
    listar()
    codigo = int(input("\nDigite o ID da seleção: "))
    ataque = int(input("Nova ataque: "))

    cursor.execute("""UPDATE selecoes SET ataque=? WHERE id=?""",
                   (ataque, codigo))

    conexao.commit()
    print("\nAtualização com sucesso")


def excluir():
    listar()
    codigo = int(input("\nDigite o ID: "))
    cursor.execute("""DELETE FROM selecoes WHERE id=?""", (codigo,))
    conexao.commit()
    print("\nRegistro exluído.")


def procurar_null():
    print("\n===Campos Nulos===")
    cursor.execute("""SELECT * FROM selecoes WHERE
    pais IS NULL or grupo='' or tecnico='' or ataque=0 """)

    dados = cursor.fetchall()
    if not dados:
        print("Nenhum registro nulo")
    else:
        for linha in dados:
            print(linha)

def corrigir_dados_nulos():
    cursor.execute("""UPDATE selecoes SET tecnico='Sem Tecnico'
    WHERE tecnico=''
    """)
    cursor.execute("""UPDATE selecoes SET grupo='Sem Grupo'
        WHERE grupo=''
    """)
    cursor.execute("""UPDATE selecoes SET ataque=50
            WHERE ataque=0
    """)

while True:
    try:
        print("\n" + "="*30)
        print("     SELEÇÕES    ")
        print("\n" + "=" * 30)
        print("[1] Inserir Seleção")
        print("[2] Listar Seleções")
        print("[3] Excluir Seleção")
        print("[4] Atualiza Seleção")
        print("[5] Prcurar dados NULL")
        print("[6] Corrigir dados NULL")
        print("[0] Sair")
        print("=" * 30)
        opcao = input('Escolha a opção: ')
        if opcao == '1':
            cadastra()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            excluir()
        elif opcao == '4':
            atualizar()
        elif opcao == '5':
            procurar_null()
        elif opcao == '6':
            corrigir_dados_nulos()
        elif opcao != '0':
            print("Saido....")
            break
        else:
            print("\nOpção inválida! tente novamente!")
    except ValueError:
        print("Opção invalida! tente novamente")