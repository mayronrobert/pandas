import pandas as pd 

print("Pandas versão:", pd.__version__) 

dados_alunos = { 
    "alunos": ['João', 'Maria', 'Pedro', 'Ana'],
    "notas": [8.5, 9.0, 7.5, 10.0]
    
}

litros_consumidos = pd.Series(       
 ['2l', '3l', '5l', '1l', '4l'],
    index = ['Segunda', 'Terça', 'Quarta', 'Quinta','Sexta']
) 

print(litros_consumidos.to_string())
print(litros_consumidos['Quarta'])  

precos_originais = pd.Series([10.0, 50.0, 100.0, 250.0], index=['Produto A', 'Produto B', 'Produto C', 'Produto D'])


precos_com_aumento = precos_originais * 1.1


print("Preços Originais:")
print(precos_originais.to_string())

print("\nPreços com 10% de aumento:")
print(precos_com_aumento.to_string()) 

dados_pesssoas = pd.DataFrame({
    "Nome": ['João', 'Maria', 'Pedro', 'Ana'], 
    "Idade": [25, 30, 22, 28] 
}) 
print(dados_pesssoas.to_string())  
print(dados_pesssoas.head(2)) 

dados_empresa = pd.DataFrame({ 
    "Funcionário": ['Carlos', 'Fernanda', 'Roberto', 'Juliana'], 
    
})
print(dados_empresa.to_string())
print(dados_empresa.head(3)) 

dados_empresa = pd.DataFrame({ 
    "Funcionário": ['Carlos', 'Fernanda', 'Roberto', 'Juliana'], 
    
})
print(dados_empresa.to_string())
print(dados_empresa.tail(2)) 

dados_empresa.info() 
dados_empresa.describe()

df_lojas = pd.DataFrame({ 
   "produtos": ['notebook', 'celular', 'placadevideo', 'monitor'],
})
print(df_lojas.to_string())

df_lojas = pd.DataFrame({ 
   "produtos": ['notebook', 'celular', 'placadevideo', 'monitor'],
    "precos": [3000, 1500, 2000, 800],
    "quantidade": [10, 20, 15, 5]
})
print(df_lojas.to_string()) 


sub_dataframe = df_lojas[['produtos', 'precos']]

print(sub_dataframe)


filtro_preco = df_lojas[df_lojas['precos'] > 1500]
print(filtro_preco)

df_lojas['Valor_Estoque'] = df_lojas['precos'] * df_lojas['quantidade']

print(df_lojas.to_string()) 




dados = {
    'produtos': ['notebook', 'celular', 'placadevideo', 'monitor'],
    'precos': [3000, 1500, 2000, 800],
    'quantidade': [10, 5, 15, 3]  # Celular (5) e Monitor (3) têm menos de 10
}
df_lojas = pd.DataFrame(dados)


produtos_pouco_estoque = df_lojas[df_lojas['quantidade'] < 10]

print(produtos_pouco_estoque)



dados = {
    'produtos': ['notebook', 'celular', 'placadevideo', 'monitor'],
    'precos': [3000, 1500, 2000, 800],
    'quantidade': [10, 20, 15, 5]
}
df_lojas = pd.DataFrame(dados)


df_lojas['Valor_Total'] = df_lojas['precos'] * df_lojas['quantidade']


print(df_lojas)




dados_filiais = {
    'Filial': ['Filial A', 'Filial B', 'Filial C', 'Filial D', 'Filial E'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'],
    'Faturamento_Milhares': [150, 85, 200, 95, 120]  # Valores fictícios para teste
}

df = pd.DataFrame(dados_filiais)


print("--- Resumo Estatístico ---")
print(df.describe())
print("\n" + "="*30 + "\n")


print("--- Filiais com Faturamento Superior a 100 ---")
filiais_top = df[df['Faturamento_Milhares'] > 100]
print(filiais_top)
