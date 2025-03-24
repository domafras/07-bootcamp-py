from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_produtos

path_arquivo = 'vendas.csv'

# Invocação das funções definidas no arquivo etl.py
lista_produtos = ler_csv(path_arquivo)
print(lista_produtos)

produtos_entregues = filtrar_produtos_nao_entregues(lista_produtos)
print(produtos_entregues)

valor_dos_produtos = somar_valores_produtos(produtos_entregues)
print(valor_dos_produtos)