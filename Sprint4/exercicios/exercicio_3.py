from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda lanc: lanc[0] if lanc[1] == 'C' else -lanc[0], lancamentos)
    saldo_final = reduce(lambda x, y: x + y, valores)
    
    return saldo_final
