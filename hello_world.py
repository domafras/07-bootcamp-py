# Exemplo de função em Python
def hello_world():
    """
    Função que imprime Hello World
    """
    return("Hello World")

print(hello_world())

# Exemplo de função sem retorno
def sem_return():
    """
    Função que não retorna nada
    """
    print("Sem return")

sem_return()

# Exemplo de função com parâmetros
def soma(valor1: float, valor2: float) -> float:
    """
    Função que soma dois valores
    """
    resultado = valor1 + valor2
    return resultado

resultado_soma = soma(10, 20)
print(resultado_soma)

# Exemplo de função com parâmetros default
def subtracao_default(valor1: float, valor2: float = 10) -> float:
    """
    Função que subtrai dois valores
    """
    resultado = valor1 - valor2
    return resultado

resultado_subtracao = subtracao_default(20)
print(resultado_subtracao)
