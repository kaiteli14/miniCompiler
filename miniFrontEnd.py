# Li, Kaite
# 1001645704
# 2019-04-16
# ---------#---------#---------#---------#---------#--------#
import sys
import traceback

import ply
import ply.yacc
import ply.lex

from pathlib import Path
from time import time

from Exceptions import *
from ParseTree import *

# ---------#---------#---------#---------#---------#--------#
lexer = None
parser = None

# ---------#---------#---------#---------#---------#--------#
# Lexical analysis section
reserved = {
    'int': 'INT',
    'if' : 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'write' : 'WRITE',
    'read' : 'READ'
}

tokens = [
    'ID', 'INT_LITERAL', 'STRING_LITERAL',
    'PLUS', 'EQUALS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS', 'EXPONENT',
    'LPAREN', 'RPAREN', 'SEMICOLON', 'COLON', 'LBRACE', 'RBRACE', 'LESS', 'LESS_EQ', 'GREATER', 'GREATER_EQ',
    'IS_EQ', 'NOT_EQ', 'AND', 'OR', 'NOT', 'COMMA',
] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t



# Tokens
t_EQUALS = r'='
t_LPAREN = r'\('
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COLON = r':'
t_EXPONENT = r'\^'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LESS = r'<'
t_LESS_EQ = r'<='
t_GREATER = r'>'
t_GREATER_EQ = r'>='
t_IS_EQ = r'=='
t_NOT_EQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_COMMA = r','


def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'"[^"]*"'
    t.value = str(t.value)
    return t

# -------------------
# Ignored characters
# Space, form feed, carriage return, tab, vertical tab
t_ignore = ' \f\r\t\v'


# Eats characters from the // marker to the end of the line.
def t_comment(_):
    r'//[^\n]*'


# Keep track of what line we're on.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


# -------------------
def t_error(t):
    # Go through elaborate shennanigans to determine the column
    # at which the lexical error occurred.
    lineStart = t.lexer.lexdata.rfind('\n', 0, t.lexer.lexpos) + 1
    column = t.lexer.lexpos - lineStart + 1

    msg = f'Illegal character "{t.value[0]}" at line {t.lexer.lineno}, column {column}.'

    # t.lexer.skip( 1 ) -- We used to just skip the character.
    #                  -- Now we throw an exception.

    raise LexicalError(msg)


# ---------#---------#---------#---------#---------#--------#
# Syntactic analysis section

# -------------------
# The start symbol.
start = 'program'

# -------------------
# Precedence rules for the operators
precedence = (
    ('right', 'EQUALS'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IS_EQ', 'NOT_EQ'),
    ('left', 'LESS', 'LESS_EQ', 'GREATER', 'GREATER_EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULUS'),
    ('right', 'EXPONENT'),
    ('left', 'UMINUS', 'NOT')
)


# -------------------
# PROGRAM ...

def p_program(p):
    'program : block_statement'
    p[0] = Program(p.lineno(1), p[1])


def p_semicolon_opt(p):
    '''semicolon_opt : epsilon
                     | SEMICOLON'''



# -------------------
# STATEMENTS ...
def p_block_statement(p):
    '''block_statement : LBRACE statement_decl_list semicolon_opt RBRACE'''
    p[0] = Statement_Block(p.lineno(1), p[2])

# Expression statement
def p_statement_expr(p):
    'statement : expression'
    p[0] = Statement_Expression(p.lineno(1), p[1])

def p_statement_A(p):
    '''statement : block_statement
                 | if_then_statement
                 | while_statement
                 | read_statement'''
    p[0] = p[1]

def p_read_statement(p):
    '''read_statement : READ LPAREN lvalue lvalue_list RPAREN'''
    p[4].append(p[3])
    p[0] = read_statement(p.lineno(1), p[4])

def p_lvalue_list_A(p):
    '''lvalue_list : lvalue_list COMMA lvalue'''
    p[1].append(p[3])
    p[0] = p[1]

def p_lvalue_list_B(p):
    '''lvalue_list : epsilon'''
    p[0] = []



# List of statements separated by semicolons
def p_statement_decl_list_A(p):
    '''statement_decl_list : statement_decl_list SEMICOLON statement_decl'''
    p[1].append(p[3])
    p[0] = p[1]

def p_statement_decl_list_B(p):
    'statement_decl_list : statement_decl'
    p[0] = [p[1]]

def p_statement_decl_list_C(p):
    'statement_decl_list : epsilon'
    p[0] = [p[1]]


def p_statement_decl(p) :
    '''statement_decl : statement
                      | decl'''
    p[0] = p[1]

 # Declaration
def p_decl(p):
    'decl : ID COLON type Initiation'
    if(p[4] == None):
        p[0] = decl_no_init(p.lineno(1), p[1], p[3], "(VARIABLE-NO-INIT)")
    else:
        p[0] = decl(p.lineno(1), p[1], p[3], "(VARIABLE)", p[4])

def p_with_initiation(p):
    'Initiation : EQUALS expression'
    p[0] = p[2]

def p_no_initiation(p):
    'Initiation : epsilon'
    p[0] = None

def p_if_then_statement_A(p):
    '''if_then_statement : IF expression block_statement'''
    p[0] = if_then_statement(p.lineno(1), p[2], p[3])

def p_if_then_statement_B(p):
    '''if_then_statement : IF expression block_statement ELSE block_statement'''
    p[0] = if_then_else_statement(p.lineno(1), p[2], p[3], p[5])

def p_while_statement(p):
    '''while_statement : WHILE expression block_statement'''
    p[0] = while_statement(p.lineno(1),p[2],p[3])

# -------------------
# IDENTIFIER ...

def p_identifier(p):
    'identifier : ID'
    p[0] = Identifier(p.lineno(1), p[1])

def p_type(p):
    'type : INT'
    p[0] = type(p.lineno(1), p[1])


# -------------------
# EXPRESSIONS ...

# Uniary operator expression
def p_expression_uniop(p):
    '''expression : PLUS expression %prec UMINUS
                  | MINUS expression %prec UMINUS
                  | NOT expression'''
    p[0] = UnaryOp(p.lineno(2), p[1], p[2])


# Binary operator expression
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression EXPONENT expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULUS expression
                  | expression LESS expression
                  | expression LESS_EQ expression
                  | expression GREATER expression
                  | expression GREATER_EQ expression
                  | expression IS_EQ expression
                  | expression NOT_EQ expression
                  | expression AND expression
                  | expression OR expression
                  | lvalue EQUALS expression'''
    p[0] = BinaryOp(p.lineno(1), p[2], p[1], p[3])


# Parenthesized expression
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# Integer literal
def p_expression_int_literal(p):
    'expression : INT_LITERAL'
    p[0] = Literal(p.lineno(1), 'int', p[1])

# String literal
def p_expression_string_literal(p):
    '''expression : STRING_LITERAL'''
    p[0] = Literal(p.lineno(1), 'String', p[1][1:-1])

# Lvlue
def p_lvalue(p):
    '''lvalue : identifier'''
    p[0] = lvalue(p.lineno(1), p[1])

# Name
def p_expression_lvalue(p):
    'expression : lvalue'
    p[0] = p[1]




# -------------------
# The 'empty' value.  It's possible to just have an empty RHS
# in a production, but having the non-terminal 'epsilon' makes
# it much more obvious that the empty string is being parsed.
def p_epsilon(p):
    'epsilon :'
    p[0] = None


# -------------------
# Gets called if an unexpected token (or the EOF) is seen during
# a parse.  We throw an exception
def p_error(p):
    msg = 'Syntax error at '
    if p is None:
        msg += 'EOF.'

    else:
        # Go through elaborate shennanigans to determine the column
        # at which the parse error occurred.
        lineStart = lexer.lexdata.rfind('\n', 0, p.lexpos) + 1
        column = p.lexpos - lineStart + 1

        msg += f'token "{p.value}", line {p.lineno}, column {column}'

    raise SyntacticError(msg)


# ---------#---------#---------#---------#---------#--------#
def _main(inputFileName):
    global lexer
    global parser

    begin = time()

    fileName = str(Path(inputFileName).name)
    parseFile = str(Path(inputFileName).with_suffix('.parse'))

    print(f'* Reading source file {inputFileName!r} ...')

    strt = time()
    with open(inputFileName, 'r') as fp:
        data = fp.read()

    print(f'    Read succeeded.  ({time() - strt:.3f}s)\n* Beginning parse ...')

    try:
        strt = time()
        lexer = ply.lex.lex()
        parser = ply.yacc.yacc()
        program = parser.parse(data, tracking=True)

        print(f'    Parse succeeded.  ({time() - strt:.3f}s)\n* Beginning parse dump to {parseFile!r} ...')

        strt = time()
        with open(parseFile, 'w') as fp:
            program.dump(fp=fp)

        print(f'    Parse dumped.  ({time() - strt:.3f}s)')

        total = time() - begin
        print(f'# Total time {total:.3f}s.\n#----------')

    except LexicalError as e:
        print('Exception detected during lexical analysis.')
        print(e)
        # traceback.print_exc()
        sys.exit(1)

    except SyntacticError as e:
        print('Exception detected during syntactic analysis.')
        print(e)
        # traceback.print_exc()
        sys.exit(1)

    except:
        print('*** (Unknown) exception detected during parse/result dump.')
        traceback.print_exc()
        sys.exit(1)


# ---------#---------#---------#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        _main(sys.argv[1])

    else:
        print('Input file name required.')

# ---------#---------#---------#---------#---------#--------#
