#CRUD
#C -> Create ok
#R -> Read ok
#U -> Update
#D -> Delete

import sqlite3

conn = sqlite3.connect("copa.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS selecoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    grupo TEXT NOT NULL,
    nivel INTEGER NOT NULL
    )
""")

conn.commit()
conn.close()
print("Tabela criada com sucesso!")


def create():
    try:
        nome = input("Nome da seleção: ").upper()
        grupo = input("Grupo: ")

        print("\nNível das seleções")
        print("""
            (1) - Fraco
            (2) - Medio
            (3) - Forte
        """)
        nivel = int(input('Escolha o nivel da Seleção: '))

        conn = sqlite3.connect("copa.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO selecoes(nome, grupo, nivel) VALUES (?, ?, ?)",
            (nome, grupo, nivel)
        )
        conn.commit()

        print(f"Seleção cadastrada: {nome} {grupo} {nivel}")
    except ValueError:
        print("O nivel deve ser um numer!")
    except sqlite3.DatabaseError as erro:
        print(f"Erro no banco: {erro}")
    finally:
        try:
            conn.close()
        except:
            pass

def read():
    try:
        conn = sqlite3.connect("copa.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM selecoes")

        dados = cursor.fetchall()

        for id, nome, grupo, nivel in dados:
            if nivel == 1:
                texto = "Fraco"
            elif nivel == 2:
                texto = "Medio"
            else:
                texto = "Forte"

            print(f"""
                ID: {id}
                Seleção: {nome}
                Grupo: {grupo}
                Nível: {texto}
                {"-" * 20}
    """)

    except sqlite3.DatabaseError as erro:
            print(f"Erro no banco: {erro}")
    finally:
        try:
            conn.close()
        except:
            pass


def delete():
    try:
        nome_selecao = input("Nome da seleção: ").lower()

        conn = sqlite3.connect("copa.db")
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM selecoes WHERE nome = ?", (nome_selecao,)
        )

        conn.commit()
        conn.close()
        print(f"Seleção apagada com sucesso! {nome_selecao}")

    except sqlite3.DatabaseError as erro:
        print(f"Erro no banco: {erro}")
    finally:
        try:
            conn.close()
        except:
            pass


def update():
    try:
        id_selecao = int(input("Id da seleção: "))

        print("""
            1 - Fraco
            2 - Medio
            3 - Forte
        """)
        novo_nivel = int(input('Novo nivel: '))

        conn = sqlite3.connect("copa.db")
        cursor = conn.cursor()

        cursor.execute((
            "UPDATE selecoes SET nivel = ? WHERE id = ?",(novo_nivel, id_selecao)
        ))
        conn.commit()
        print(f"Nivel da seleção atualizado {novo_nivel} ")
    except ValueError:
        print("Valor inserido errado")
    except sqlite3.DatabaseError as erro:
        print(f"Erro no banco: {erro}")
    finally:
        try:
            conn.close()
        except:
            pass



while True:
    try:
        print("\n" + "="*30)
        print("     SISTEMA DE USUARIOS")
        print("\n" + "=" * 30)
        print("[1] Inserir Seleção")
        print("[2] Listar Seleções")
        print("[3] Excluir Seleção")
        print("[4] Atualiza Seleção")
        print("[0] Sair")
        print("=" * 30)
        opcao = input('Escolha a opção: ')
        if opcao == '1':
            create()
        elif opcao == '2':
            read()
        elif opcao == '3':
            delete()
        elif opcao == '4':
            update()
        elif opcao == '0':
            print("Saido....")
            break
        else:
            print("\nOpção inválida! tente novamente!")
    except ValueError:
        print("Opção invalida! tente novamente")