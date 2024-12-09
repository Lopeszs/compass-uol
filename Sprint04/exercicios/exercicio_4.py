def calcular_valor_maximo(operadores, operandos) -> float:
    def calcular(op, par):
        if op == '+':
            return par[0] + par[1]
        elif op == '-':
            return par[0] - par[1]
        elif op == '*':
            return par[0] * par[1]
        elif op == '/':
            return par[0] / par[1]
        elif op == '%':
            return par[0] % par[1]

    resultados = map(lambda x: calcular(x[0], x[1]), zip(operadores, operandos))

    return max(resultados)
