import pandas as pd

df_magias = pd.DataFrame({
    'nome_magia': [
'Bola de fogo', 'Raio de Gelo', "Nova Solar",
'Nevasca', 'Raio', 'Tempestade', 'Cura Menor', "Ressureiçã",
'Chama Azul', "Vendaval"],

    'escola': [
'Fogo','Gelo', "Fogo", 'Gelo', "Trovão", "Trovão",
"Luz", "Luz", "Fogo", "Trovão"
],
    'dano':[85, 60, 120, 95, 70, 110, 0, 0, 50, 45],
    'custo_mana': [50, 35, 80, 65, 40, 75, 20, 90, 30, 20],
    'nivel': [3,2,5,4,2,5,1,5,1,1]
})
print(df_magias)
df_itens = pd.DataFrame({
    'nome_item'   : ['Espada Longa', 'Cajado Arcano', 'Armadura de Placas',
                       'Manto das Sombras', 'Adaga Envenenada', 'Escudo Solar',
                       'Poção de Vida', 'Elixir de Mana', 'Arco Longo', 'Orbe do Caos'],
    'tipo'        : ['Arma','Arma','Armadura','Armadura','Arma','Armadura',
                       'Consumível','Consumível','Arma','Arma'],
    'raridade'    : ['Comum','Raro','Comum','Raro','Comum','Épico',
                       'Comum','Raro','Comum','Épico'],
    'preco_ouro'  : [150, 800, 400, 900, 200, 1500, 50, 120, 300, 2000],
    'peso_kg'     : [3.5, 2.0, 15.0, 1.5, 0.8, 8.0, 0.3, 0.3, 1.5, 0.5]
})
#Dano medio por escola de magia
#Estamos agrupando atrasves da escola, e depois chamo dentro do dataFrame
#a coluna de dano e tiro a media usando a função mean()
media_dano = df_magias.groupby('escola')['dano'].mean()
print(media_dano)

#Quantidade de itens por tipo
qtd_por_tipo = df_itens.groupby('tipo').size()
print(qtd_por_tipo)

#Custo taotal de mana por nivel
mana_por_nivel = df_magias.groupby('nivel')['custo_mana'].sum()
print(mana_por_nivel)

#Preço maximo e minimo por raridade
preco_raridade = df_itens.groupby('raridade')['preco_ouro'].agg(
    ['max', 'min']
)
print(preco_raridade)

#Dano maximo poor escola de magia
dano_maximo = df_magias.groupby('escola')['dano'].max()
print(dano_maximo)
mais_forte = df_magias.loc[df_magias.groupby('escola')['dano'].idxmax()]
print(mais_forte)

relatorio = df_itens.groupby('tipo').agg({
	   'preco_ouro': ['max', 'min'],
	   'peso_kg': ['sum', 'mean']
})
print(relatorio)


resultado = df_magias.groupby('escola').agg(
    dano_total = ('dano', 'sum'),
    mana_total = ('custo_mana', 'sum'),
    qtd_magias = ('nome_magia', 'count')
)
resultado['dano_por_mana'] = (resultado['dano_total'] / resultado['mana_total']).round(2)

print(resultado)
resultado = resultado.sort_values('dano_por_mana', ascending=False)
print(resultado)