'''
modulo contendo funções uteis
'''

def num(s: str, d=0) -> int:
    # tenta converter em inteiro
    try:
        return int(s)
    except:
        pass

    # tenta converter em decimal
    try:
        return float(s)
    except:
        pass

    return d