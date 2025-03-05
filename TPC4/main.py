import ply.lex as lex

reserved = {
    "select" : "SELECT",
    "where" : "WHERE",
    "limit" : "LIMIT"
}

identifier_map = {
    "?nome": "VAR_NOME",
    "?desc": "VAR_DESC",
    "?s": "VAR_S",
    "?w": "VAR_W"
}

tokens = [
    "URI",
    "COMMAND",
    "NUMBER",
    "STRING",
    "IDENTIFIER",
    "ATTRIBUTE",
    "LBRACE",
    "RBRACE",
    "DOT",
    "HASH",
] + list(reserved.values()) + list(identifier_map.values())

t_STRING = r'"[^"]*"(@[a-zA-Z]+)?'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_DOT = r'\.'
t_HASH = r'\#'

def t_URI(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_ATTRIBUTE(t):
    r'\b\w{1}\b'
    return t

def t_IDENTIFIER(t):
    r'\?\w+\b'  
    t.type = identifier_map.get(t.value, t.value.upper())  
    return t

def t_COMMAND(t):
    r'\b[a-zA-Z]+\b'
    t.type = reserved.get(t.value.lower(), "COMMAND")
    return t


def t_NUMBER(t):
    r'\d+'
    t.type = "NUMBER"
    t.value = int(t.value)  
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t,;'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    filename = "./results/input.txt"
    output_filename = "./results/output.txt"

    try:
        with open(filename, "r") as file:
            with open(output_filename, "w") as output_file:
                for line in file:
                    lexer.input(line)
                    for token in lexer:
                        output_file.write(f"Token: {token.type}, Valor: {token.value}\n")
                    
                    output_file.write("-" * 40 + "\n")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":  
    main()