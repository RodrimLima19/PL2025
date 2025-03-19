from exp_analex import lexer
from exp_ast import Exp, Num

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)

def rec_Num():
    global prox_simb
    if prox_simb.type == 'NUM':
        num = int(prox_simb.value)
        rec_term('NUM')
        return Num(num)
    else:
        parserError(prox_simb)

def rec_Fator():
    global prox_simb
    if prox_simb.type == 'NUM':
        return rec_Num()
    else:
        parserError(prox_simb)

def rec_Termo():
    global prox_simb
    res = rec_Fator()
    while prox_simb and prox_simb.type in ('MULT', 'DIV'):
        if prox_simb.type == 'MULT':
            rec_term('MULT')
            res = Exp('MULT', res, '*', rec_Fator())
        elif prox_simb.type == 'DIV':
            rec_term('DIV')
            res = Exp('DIV', res, '/', rec_Fator())
    return res

def rec_Expr():
    global prox_simb
    res = rec_Termo()
    while prox_simb and prox_simb.type in ('PLUS', 'MINUS'):
        if prox_simb.type == 'PLUS':
            rec_term('PLUS')
            res = Exp('PLUS', res, '+', rec_Termo())
        elif prox_simb.type == 'MINUS':
            rec_term('MINUS')
            res = Exp('MINUS', res, '-', rec_Termo())
    return res

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_Expr()