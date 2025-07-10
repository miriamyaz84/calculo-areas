import math

def calcular_area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado.

    Parámetros:
    lado (float): Longitud de uno de los lados del cuadrado. Debe ser mayor que 0.

    Retorna:
    float: Área del cuadrado si el lado es válido.
    None: Si el valor del lado es inválido (0 o negativo).
    """
    if lado <= 0:
        return None
    return lado * lado

def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float): Radio del círculo. Debe ser mayor que 0.

    Retorna:
    float: Área del círculo si el radio es válido.
    None: Si el radio es inválido (0 o negativo).
    """
    if radio <= 0:
        return None
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo.

    Parámetros:
    base (float): Base del triángulo. Debe ser mayor que 0.
    altura (float): Altura correspondiente a la base. Debe ser mayor que 0.

    Retorna:
    float: Área del triángulo si los valores son válidos.
    None: Si alguno de los valores es inválido.
    """
    if base <= 0 or altura <= 0:
        return None
    return (base * altura) / 2
