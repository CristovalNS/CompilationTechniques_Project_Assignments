# Compilation Techniques Group Assignment 1
# Cristoval Neo Sasono_2602158235
# Kenneth Jayadi Yu_2602158260
# Brandon Salim_2602177783

import ply.lex as lex

# List of token names
tokens = (
    'ID', 'NUMBER',
    'IF', 'WHILE', 'RETURN', 'ELSE',
    'INT', 'FLOAT', 'CHAR',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMI', 'COMMA',
)

# Reserved words
reserved = {
    'if': 'IF',
    'while': 'WHILE',
    'return': 'RETURN',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR'
}

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','

# A regular expression rule for ID (only lowercase letters now)
def t_ID(t):
    r'[a-z][a-z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Define a rule for ignoring spaces and tabs
t_ignore = ' \t'

# Define a rule for new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define a rule for tracking errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Input string
data = """
int x (float y) {
    if (y = 5)
        if (z = y)
            return z;
    else if (z = 5)
        return (z + 5);
    else 
        return (z + z);
}
"""

lexer.input(data)

# Tokenize the input
while True:
    tok = lexer.token()
    if not tok:
        break  # When no more input
    print(tok)
