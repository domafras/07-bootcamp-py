import csv

def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos não entregues
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get('Entregue') == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_produtos(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Função que soma os valores dos produtos
    """
    valores = [int(produto.get('Venda')) for produto in lista_com_produtos_filtrados]
    return sum(valores)