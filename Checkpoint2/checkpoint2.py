import pandas as pd

lojas = pd.read_excel(r'C:\Users\mypc\Desktop\FIAP2Semestre\Computational Thinking Using (Python)\Check 2 22.09\Checkpoint2\Checkpoint2/lojas.xlsx')
produtos = pd.read_excel(r'C:\Users\mypc\Desktop\FIAP2Semestre\Computational Thinking Using (Python)\Check 2 22.09\Checkpoint2\Checkpoint2/produtos.xlsx')

df_lojas = pd.DataFrame(data=lojas)
df_lojas = df_lojas.rename(columns={"Código da loja": "Cod_loja", "Nome da loja": "Nome_loja"})

df_produtos = pd.DataFrame(data=produtos)
df_produtos = df_produtos.rename(columns={"Código do produto": "Cod_prod", "Nome do produto": "Nome_Produto", "Código da loja" : "Cod_loja", "preço" : "preco"})



def listar_lojas():
    print("------------------------------------------\n"
          "LOJAS CADASTRADAS\n"
          "__________________________________________")

    print(df_lojas.to_string(index=False))
    print("------------------------------------------\n")
    print("--------------------------------------------------------------------------------\n")

def listar_produtos():
    print("--------------------------------------------------------------------------------\n"
          "PRODUTOS CADASTRADOS\n"
          "________________________________________________________________________________")
    print(df_produtos.to_string(index=False))
    print("--------------------------------------------------------------------------------\n")


def produtos_loja():
    print("------------------------------------------\n"
          "Relatório Produto por Loja\n")

    for value in df_lojas.sort_values(by='Cod_loja').itertuples():
        codLoja = str(value.Cod_loja)
        nomeLoja = str(value.Nome_loja)
        print("-------------------------------------------------------------")
        print(codLoja + " - " + nomeLoja, "\n")
        pd.options.display.float_format = '{:,.2f}'.format
        df_produtos_filtro = df_produtos.loc[df_produtos['Cod_loja'] == int(value.Cod_loja)][['Nome_Produto','preco']]
        produtos = df_produtos_filtro.to_string(header=False, index=False)
        print(produtos)

    print("\n")
    
def produtos_p():
    print("------------------------------------------\n"
          "\033[1m  Relatório de Produtos  \033[0m\n")
    
    
    for value in df_produtos.sort_values(by='Nome_Produto').itertuples():
        nome_Prod = str(value.Nome_Produto)
        preco_Prod = str(value.preco) 
        print("-------------------------------------------------------------")
        print(nome_Prod + " - " + preco_Prod)
        pd.options.display.float_format = '{:,.2f}'.format
        df_lojas_filtro = df_lojas.loc[df_lojas['Cod_loja'] == int(value.Cod_loja)][['Cod_loja', 'Nome_loja']]
        lojas = df_lojas_filtro.to_string(header=False, index=False)
        print(lojas)

        


def menu():

    escolha = ' '
    while (escolha != '4'):

        print('\n-----------------------------------\n'
              'MENU - LOJA E PRODUTOS:\n'
              '-----------------------------------\n'
              '1 - Listar Lojas\n'
              '2 - Listas Produtos\n'
              '3 - Relatório - Produtos por loja\n'
              '4 - Relatório de Produtos\n'
              '5 - Sair\n'
              '-----------------------------------')

        escolha = input("Digite uma opção: ")

        if (escolha == '1'):
            listar_lojas()

        elif (escolha == '2'):
            listar_produtos()

        elif (escolha == '3'):
            produtos_loja()
        
        elif (escolha == '4'):
            produtos_p()

menu()