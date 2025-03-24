from typing import List

# 1) Calcular Média de Valores em uma Lista
def calcular_media(lista: List[float]) -> float:
    """
    Função que calcula a média de valores em uma lista
    """
    media = sum(lista) / len(lista)
    return media

# Teste da função calcular_media
print(calcular_media([1, 2, 3, 4, 5]))

# 2) Filtrar Dados Acima de um Limite
def filtrar_dados_acima_de_limite(lista: List[float], limite: float) -> List[float]:
    """
    Função que filtra valores acima de um limite
    """
    valores_filtrados = [valor for valor in lista if valor > limite]
    return valores_filtrados

# Teste da função filtrar_dados_acima_de_limite
print(filtrar_dados_acima_de_limite([1, 2, 3, 4, 5], 3))

# 3) Contar Valores Únicos em uma Lista
def contar_valores_unicos(lista: List[float]) -> int:
    """
    Função que conta valores únicos em uma lista
    """
    valores_unicos = len(set(lista))
    return valores_unicos

# Teste da função contar_valores_unicos
print(contar_valores_unicos([1, 2, 3, 4, 5, 1, 2, 3]))

# 4) Converter Celsius para Fahrenheit em lista
def converter_celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    """
    Função que converte temperaturas de Celsius para Fahrenheit
    """
    temperaturas_fahrenheit = [temp * 9/5 + 32 for temp in temperaturas_celsius]
    return temperaturas_fahrenheit

# Teste da função converter_celsius_para_fahrenheit
print(converter_celsius_para_fahrenheit([-10, 0, 10, 20, 30]))

# 5) Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(lista: List[float]) -> float:
    """
    Função que calcula o desvio padrão de uma lista de valores
    """
    media = sum(lista) / len(lista)
    variancia = sum((valor - media) ** 2 for valor in lista) / len(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

# Teste da função calcular_desvio_padrao
print(calcular_desvio_padrao([1, 2, 3, 4, 5]))

# 6) Encontrar Valores Ausentes em uma sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """
    Função que encontra valores ausentes em uma sequência
    """
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

# Teste da função encontrar_valores_ausentes
print(encontrar_valores_ausentes([1, 2, 3, 5, 6, 8, 9]))