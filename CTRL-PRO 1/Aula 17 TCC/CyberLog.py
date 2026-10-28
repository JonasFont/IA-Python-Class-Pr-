import sqlite3 #Banco de Dados
import random
from datetime import datetime, timedelta
#Função nativa do python para pegar as horas
import numpy as np #Biblioteca nativa de matematica
import pandas as pd #Analise de dados
import matplotlib.pyplot as plt #Criação da graficos
import sklearn


banco = "cyberlog.db"

ataques = ["Brute Force", "SQL Injector",
           "XSS", "DDoS", "Malware", "Phising", "Ransomware", "Port Scan"]
gravidades = ["Baixo", "Media", "Alto", "Critico"]
status= ["Novo", "Em analise", "Resolvido"]
origem = ["Firewall", "IDS", "SIEM", "Servidor Web", "Antivirus"]


#--------------------Banco --------------------------
def conectar():
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS incidentes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    tipo TEXT,
    gravidade TEXT,
    status TEXT,
    origem TEXT, 
    data TEXT
)""")
    conn.commit()
    return conn

def gerar_ip():
    return ".".join(str(random.randint(1, 254))for _ in range(4))

def data_aleatoria():
    return (datetime.now()-timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

def gerar_logs(conn, qtd=500):
    cursor = conn.cursor()

    sql = """
    INSERT INTO incidentes
    (ip,tipo,gravidade,status,origem,data)VALUES (?, ?, ?,?,?,?)
    """

    for _ in range(qtd):
        cursor.execute(sql, (
            gerar_ip(),
            random.choice(ataques),
            random.choice(gravidades),
            random.choice(status),
            random.choice(origem),
            data_aleatoria()
        ))

    conn.commit()
    print(f"\nLogs inseridos com sucesso!")


def listar(conn):
    print("\n---INCIDENTES---")
    for linha in conn.execute("SELECT * FROM incidentes ORDER BY id"):
        print(linha)


def dashboard(conn):
    df = pd.read_sql_query("SELECT * FROM incidentes", conn)
    if df.empty:
        print("Banco Vazio.")
        return

    print("\n========== DASHBOARD ==========")
    print(f"total de incidentes: {len(df)}")
    mapa={"Baixo": 1,
          "Media":2,
          "Alto":3,
          "Critico":4
          }
    severidade = df['gravidade'].map(mapa)
    print(f"Media severidade: {np.mean(severidade):.2f}")
    print(f"Mediana         : {np.median(severidade)}")
    print(f"Desvio Padrão   : {np.std(severidade)}")

    print("\nIncidentes por tipo")
    print(df['tipo'].value_counts())

    print('\nIncidentes por gravidade')
    print(df['gravidade'].value_counts())

    print('\nIncidentes por origem')
    print(df['origem'].value_counts())

    df['tipo'].value_counts().plot(kind='bar', title='Ataque por tipo')
    plt.tight_layout()
    plt.show()

def menu():
    conn=conectar()
    while True:
        try:
            print("\n" + "="*30)
            print("     CYBERLOG ANALYZER")
            print("\n" + "=" * 30)
            print("[1] Gerar logs aleatórios")
            print("[2] Listar incidentes")
            print("[3] Dashboard")
            print("[0] Sair")
            print("=" * 30)
            opcao = input('Escolha a opção: ')
            if opcao == '1':
                gerar_logs(conn)
            elif opcao == '2':
                listar(conn)
            elif opcao == '3':
                dashboard(conn)
            elif opcao == '0':
                conn.close()
                print("Saido....")
                break
            else:
                print("\nOpção inválida! tente novamente!")
        except ValueError:
            print("Opção invalida! tente novamente")


if __name__ == '__main__':
    menu()