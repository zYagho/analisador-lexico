
#Lista de estados que serão reconhecidos pela linguagem C-
estados = [
    'q0', 'id', 'number',
    'i', 'in', 'int', 'if',
    'if_esq_parenteses', 'if_final',
    'int_esq_parenteses', 'int_dir_parenteses', 'int_final',
    'e', 'el', 'els', 'else', 
    'else_esq_chaves', 'else_final',
    'r', 're', 'ret', 'retu', 'retur', 'return' 
    'return_esq_parenteses', 'return_ponto_virgula', 'return_final',
    'v', 'vo', 'voi', 'void', 
    'void_dir_parenteses', 'void_ponto_virgula', 'void_final',
    'w', 'wh', 'whi', 'whil', 'while', 
    'while_esq_parenteses', 'while_final',
    'f', 'fl', 'flo', 'floa', 'float',
    'float_esq_parenteses', 'float_dir_parenteses', 'float_final',
    'adicao', 'subtracao', 'multiplicacao', 'divisao', 
    'divisao_finalizado', 'divisao_equal', 'divisao_id', 'divisao_number',
    'maior', 'maior_igual', 'menor', 'menor_igual',
    'maior_finalizado', 'menor_finalizado',
    'atribuicao', 'igual', 
    'atribuicao_finalizado',
    'exclamacao', 'exclamacao_igual', 
    'virgula', 'ponto_virgula', 'ponto', 
    'esq_parenteses', 'dir_parenteses', 'esq_colchetes', 'dir_colchetes', 'esq_chaves', 'dir_chaves',

    'id_esq_parenteses', 'id_dir_parenteses', 'id_esq_colchetes', 'id_dir_colchetes', 'id_esq_chaves', 'id_dir_chaves',
    'id_ponto_virgula', 'id_virgula', 'id_final',
    'id_adicao', 'id_subtracao', 'id_multiplicacao', 'id_divisao', 'id_maior', 'id_menor', 'id_atribuicao', 'id_exclamacao', 
    'number_esq_parenteses', 'number_dir_parenteses', 'number_esq_colchetes', 'number_dir_colchetes', 'number_esq_chaves', 'number_dir_chaves',
    'number_ponto_virgula', 'number_virgula', 'number_final',
    'number_adicao', 'number_subtracao', 'number_multiplicacao', 'number_divisao', 'number_maior', 'number_menor', 'number_atribuicao', 'number_exclamacao',

    'divisao_multiplicacao', 'comentario', 'comentario_multiplicacao', 'comentario_finalizado'
]

#Alfaberto permitido na linguagem
alfabeto_entrada = [ 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '+', '-', '*', '/', '<', '>', '=', '!', '(', ')', '[', ']', '{', '}', ';', ',', '.',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '\n'
]

#tokens
alfabeto_saida = [
    'ID',
    'NUMBER',
    'INT',
    'IF',
    'ELSE',
    'RETURN',
    'VOID',
    'WHILE',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GREATER',
    'GREATER_EQUAL',
    'LESS',
    'LESS_EQUAL',
    'ATTRIBUTION',
    'EQUALS',
    'DIFFERENT',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACKETS',
    'RBRACKETS',
    'LBRACES',
    'RBRACES',
]

#Simbolo inicial
estado_inicial = 'q0'

#configurando as tansações iniciais.
transicoes_iniciais = {chr(caracter): "id" for caracter in range(ord('a'), ord('z') + 1)}
transicoes_iniciais.update({'i':'i'})
transicoes_iniciais.update({'v':'v'})
transicoes_iniciais.update({'e':'e'})
transicoes_iniciais.update({'w':'w'})
transicoes_iniciais.update({'r':'r'})
transicoes_iniciais.update({'f':'f'})

transicoes_iniciais.update({chr(caracter): "number" for caracter in range(ord('0'), ord('9') + 1)})
transicoes_iniciais.update({
    ' ':'q0',
    '\n':'q0',
    '+' : 'adicao',
    '-' : 'subtracao',
    '*' : 'multiplicacao',
    '/' : 'divisao',
    '>' : 'maior',
    '<' : 'menor',
    '=' : 'atribuicao',
    '!' : 'exclamacao',
    ',' : 'virgula',
    ';' : 'ponto_virgula',
    '(' : 'esq_parenteses',
    ')' : 'dir_parenteses',
    '[' : 'esq_colchetes',
    ']' : 'dir_colchetes',
    '{' : 'esq_chaves',
    '}' : 'dir_chaves'
})

transicoes = {
    'q0':transicoes_iniciais,

    #ID
    'id':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        '!' : 'id_exclamacao',
        '.' : 'id',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        ' ' : 'id_final',
        '\n' : 'id_final',
    },
    'id_esq_parenteses':transicoes_iniciais,
    'id_dir_parenteses':transicoes_iniciais,
    'id_esq_colchetes':transicoes_iniciais,
    'id_dir_colchetes':transicoes_iniciais,
    'id_esq_chaves':transicoes_iniciais,
    'id_dir_chaves':transicoes_iniciais,
    'id_final':transicoes_iniciais,
    'id_adicao':transicoes_iniciais,
    'id_subtracao':transicoes_iniciais,
    'id_multiplicacao':transicoes_iniciais,
    'id_divisao':transicoes_iniciais,
    'id_menor':transicoes_iniciais,
    'id_maior':transicoes_iniciais,
    'id_atribuicao':transicoes_iniciais,
    'id_igual' : transicoes_iniciais,
    'id_exclamacao' : transicoes_iniciais, 
    'id_ponto_virgula' : transicoes_iniciais,
    'id_virgula' : transicoes_iniciais,

    #INT
    'i':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'id',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        'n':'in',
        'f':'if'
    },
    'in':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'id',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        't':'int'
    },
    'int':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'int_esq_parenteses',
        ')' : 'int_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ' : 'int_final',
        '\n' : 'int_final',
    },
    'int_esq_parenteses':transicoes_iniciais,
    'int_dir_parenteses':transicoes_iniciais,
    'int_final':transicoes_iniciais,

    #IF
    'if':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'if_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ':'if_final',
        '\n':'if_final'
    },
    'if_esq_parenteses':transicoes_iniciais,
    'if_final':transicoes_iniciais,

    #else
    'e':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'l':'el'
    },
    'el':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        's':'els'
    },
    'els':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'e':'else'
    },
    'else':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'else_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ':'else_final',
        '\n':'else_final'
    },
    'else_esq_chaves':transicoes_iniciais,
    'else_final': transicoes_iniciais,

    #While
    'w':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'h':'wh'
    },
    'wh':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'i':'whi'
    },
    'whi':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'l':'whi'
    },
    'whil':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'e':'while'
    },
    'while':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'while_esq_parentese',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ':'while_final',
        '\n':'while_final'
    },
    'while_esq_parentese':transicoes_iniciais,
    'while_final':transicoes_iniciais,

    #Return
    'r':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'e':'re'
    },
    're':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        't':'ret'
    },
    'ret':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'u':'retu'
    },
    'retu':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'r':'retur'
    },
    'retur':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'n':'return'
    },
    'return':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'return_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ';' : 'return_ponto_virgula',
        ' ':'return_final',
        '\n':'return_final'
    },
    'return_final':transicoes_iniciais,
    'return_ponto_virgula':transicoes_iniciais,
    'return_esq_parenteses':transicoes_iniciais,

    #Void
    'v':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'id',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        ' ' : 'id_final',
        '\n' : 'id_final',
        'o' :'vo'
    },
    'vo':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'id',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        ' ' : 'id_final',
        '\n' : 'id_final',
        'i' :'voi'
    },
    'voi':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'id',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        ',' : 'id_virgula',
        ';' : 'id_ponto_virgula',
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        ' ' : 'id_final',
        '\n' : 'id_final',
        'd' :'void'
    },
    'void':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'void_dir_parentese',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ' : 'void_final',
        '\n': 'void_final',
        ';' : 'void_ponto_virgula'
    },
    'void_ponto_virgula':transicoes_iniciais,
    'void_final':transicoes_iniciais,
    'void_dir_parentese':transicoes_iniciais,

    #Number
    'number':{
        **{chr(caracter): 'number' for caracter in range(ord('0'), ord('9') + 1)},
        '.' : 'number',
        '+' : 'number_adicao',
        '-' : 'number_subtracao',
        '*' : 'number_multiplicacao',
        '/' : 'number_divisao',
        ',' : 'number_virgula',
        ';' : 'number_ponto_virgula',
        '(' : 'number_esq_parenteses',
        ')' : 'number_dir_parenteses',
        '[' : 'number_esq_colchetes',
        ']' : 'number_dir_colchetes',
        '{' : 'number_esq_chaves',
        '}' : 'number_dir_chaves',
        ' ' : 'number_final',
        '\n' : 'number_final',
    },
    'number_final' : transicoes_iniciais,
    'number_esq_parenteses' : transicoes_iniciais,
    'number_dir_parenteses' : transicoes_iniciais,
    'number_esq_colchetes' : transicoes_iniciais,
    'number_dir_colchetes' : transicoes_iniciais,
    'number_esq_chaves' : transicoes_iniciais,
    'number_dir_chaves' : transicoes_iniciais,
    'number_ponto_virgula' : transicoes_iniciais,
    'number_virgula' : transicoes_iniciais,
    'number_adicao' : transicoes_iniciais,
    'number_subtracao' : transicoes_iniciais,
    'number_multiplicacao' : transicoes_iniciais,
    'number_divisao' : transicoes_iniciais,
    'number_maior' : transicoes_iniciais, 
    'number_menor' : transicoes_iniciais, 
    'number_atribuicao' : transicoes_iniciais,
    'number_exclamacao' : transicoes_iniciais, 
    'adicao' : transicoes_iniciais,
    'subtracao' : transicoes_iniciais,
    'multiplicacao' : transicoes_iniciais,
    'divisao':{
        '/':'comentario',
        ' ':'divisao_final',
        '*':'divisao_multiplicacao'
    },
    'comentario':transicoes_iniciais,
    'divisao_final':transicoes_iniciais,

    'maior' : {
        ' ' : 'maior_finalizado',
        '=' : 'maior_igual',
    },
    'maior_igual' : {
        ' ' : 'q0',
    },
    'maior_finalizado' : transicoes_iniciais,
    'menor' : {
        ' ' : 'menor_finalizado',
        '=' : 'menor_igual',
    },
    'menor_igual' : {
        ' ' : 'q0',
    },
    'menor_finalizado' : transicoes_iniciais,
    'atribuicao' : {
        ' ' : 'atribuicao_finalizado',
        '=' : 'igual',
    },
    'atribuicao_finalizado' : transicoes_iniciais,
    'igual' : {
        ' ' : 'q0',
    },
    'exclamacao' : {
        '=' : 'exclamacao_igual',
    },
    'virgula' : transicoes_iniciais,

    #Chaves, parenteses e colchetes
    'esq_parenteses' : transicoes_iniciais,
    'dir_parenteses' : transicoes_iniciais,
    'esq_colchetes' : transicoes_iniciais,
    'dir_colchetes' : transicoes_iniciais,
    'esq_chaves' : transicoes_iniciais,
    'dir_chaves' : transicoes_iniciais,
    
    'exclamacao_igual' : transicoes_iniciais,
    'virgula' : transicoes_iniciais,
    'ponto_virgula' : transicoes_iniciais,
    'ponto' : transicoes_iniciais,

    #Float
    'f':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'l' :'fl'
    },
    'fl':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'o' :'flo'
    },
    'flo':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        'a' :'floa'
    },
    'floa':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'id_esq_parenteses',
        ')' : 'id_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        't' :'float'
    },
    'float':{
        **{chr(caracter): 'id' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'id' for caracter in range(ord('0'), ord('9') + 1)},
        '(' : 'float_esq_parenteses',
        ')' : 'float_dir_parenteses',
        '[' : 'id_esq_colchetes',
        ']' : 'id_dir_colchetes',
        '{' : 'id_esq_chaves',
        '}' : 'id_dir_chaves',
        '+' : 'id_adicao',
        '-' : 'id_subtracao',
        '*' : 'id_multiplicacao',
        '/' : 'id_divisao',
        '>' : 'id_maior',
        '<' : 'id_menor',
        '=' : 'id_atribuicao',
        ' ' :'float_final'
    },
    'float_esq_parenteses':transicoes_iniciais,
    'float_dir_parenteses':transicoes_iniciais,
    'float_final':transicoes_iniciais,

    'divisao_multiplicacao' : {
        **{chr(caracter): 'comentario' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'comentario' for caracter in range(ord('0'), ord('9') + 1)},
        '+' : 'comentario',
        '-' : 'comentario',
        '*' : 'comentario_multiplicacao',
        '/' : 'comentario',
        '>' : 'comentario',
        '<' : 'comentario',
        '=' : 'comentario',
        '!' : 'comentario',
        ',' : 'comentario',
        ';' : 'comentario',
        '(' : 'comentario',
        ')' : 'comentario',
        '[' : 'comentario',
        ']' : 'comentario',
        '{' : 'comentario',
        '}' : 'comentario',
        ' ' : 'comentario',
        '\n' : 'comentario',
    },
    'comentario' : {
        **{chr(caracter): 'comentario' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'comentario' for caracter in range(ord('0'), ord('9') + 1)},
        '+' : 'comentario',
        '-' : 'comentario',
        '*' : 'comentario_multiplicacao',
        '/' : 'comentario',
        '>' : 'comentario',
        '<' : 'comentario',
        '=' : 'comentario',
        '!' : 'comentario',
        ',' : 'comentario',
        ';' : 'comentario',
        '(' : 'comentario',
        ')' : 'comentario',
        '[' : 'comentario',
        ']' : 'comentario',
        '{' : 'comentario',
        '}' : 'comentario',
        ' ' : 'comentario',
        '\n' : 'comentario',
    },
    'comentario_multiplicacao' : {
        **{chr(caracter): 'comentario' for caracter in range(ord('a'), ord('z') + 1)},
        **{chr(caracter): 'comentario' for caracter in range(ord('0'), ord('9') + 1)},
        '+' : 'comentario',
        '-' : 'comentario',
        '*' : 'comentario_multiplicacao',
        '/' : 'comentario_finalizado',
        '>' : 'comentario',
        '<' : 'comentario',
        '=' : 'comentario',
        '!' : 'comentario',
        ',' : 'comentario',
        ';' : 'comentario',
        '(' : 'comentario',
        ')' : 'comentario',
        '[' : 'comentario',
        ']' : 'comentario',
        '{' : 'comentario',
        '}' : 'comentario',
        ' ' : 'comentario',
        '\n' : 'comentario',
    },
    'comentario_finalizado' : transicoes_iniciais,
}

tabela_saida = {

    'q0': '',
    #Saida dos IDs
    'id': '',
    'id_esq_parenteses' :'ID\nLPAREN\n',
    'id_dir_parenteses':'ID\nRPAREN\n',
    'id_esq_colchetes':'ID\nLBRACKETS\n',
    'id_dir_colchetes':'ID\nRBRACKETS\n',
    'id_esq_chaves':'ID\nLBRACES',
    'id_dir_chaves':'ID\nRBRACES',
    'id_ponto_virgula' : 'ID\nSEMICOLON\n',
    'id_virgula' : 'ID\nCOMMA\n',
    'id_adicao' : 'ID\nPLUS\n',
    'id_subtracao' : 'ID\nMINUS\n',
    'id_multiplicacao' : 'ID\nTIMES\n',
    'id_divisao' : 'ID\nDIVIDE\n',
    'id_maior' : 'ID\nGREATER\n', 
    'id_menor' : 'ID\nLESS\n', 
    'id_atribuicao' : 'ID\nATTRIBUTION\n', 
    'id_exclamacao' : 'ID\nDIFFERENT\n', 
    'id_final':'ID\n',

    #Saída do INT
    'i':'',
    'in':'',
    'int':'',
    'int_final': 'INT\n',  # Estado final do 'int'
    'int_esq_parenteses' : 'INT\nLPAREN\n',
    'int_dir_parenteses' : 'INT\nRPAREN\n',

    #Saída do IF
    'if':'',
    'if_final': 'IF\n',
    'if_esq_parenteses' : 'IF\nLPAREN\n',

    #Saida do ELSE
    'e':'',
    'el':'',
    'els':'',
    'else':'',
    'else_final': 'ELSE\n',
    'else_esq_chaves':'ELSE\nLBRACES',

    #Saída do WHILE
    'w':'',
    'wh':'',
    'whi':'',
    'whil':'',
    'while':'',
    'while_final':'WHILE\n',
    'while_esq_parentese':'WHILE\nLPAREN',

    #Saída do Return
    'r':'',
    're':'',
    'ret':'',
    'retu':'',
    'retur':'',
    'return':'',
    'return_final':'RETURN\n',
    'return_esq_parenteses':'RETURN\nLPAREN\n',
    'return_ponto_virgula':'RETURN\nSEMICOLON\n',

    #Saída do VOID
    'v':'',
    'vo':'',
    'voi':'',
    'void':'',
    'void_final':'VOID\n',
    'void_dir_parentese':'VOID\nRPAREN\n',
    'void_ponto_virgula':'VOID\nSEMICOLON',

    #Saída Number
    'number':'',
    'number_final': 'NUMBER\n',
    'number_esq_parenteses' : 'NUMBER\nLPAREN\n',
    'number_dir_parenteses' : 'NUMBER\nRPAREN\n',
    'number_esq_colchetes' : 'NUMBER\nLBRACKETS\n',
    'number_dir_colchetes' : 'NUMBER\nRBRACKETS\n',
    'number_esq_chaves' : 'NUMBER\nLBRACES\n',
    'number_dir_chaves' : 'NUMBER\nRBRACES\n',
    'number_ponto_virgula' : 'NUMBER\nSEMICOLON\n',
    'number_virgula' : 'NUMBER\nCOMMA\n',
    'number_adicao' : 'NUMBER\nPLUS\n',
    'number_subtracao' : 'NUMBER\nMINUS\n',
    'number_multiplicacao' : 'NUMBER\nTIMES\n',
    'number_divisao' : 'NUMBER\nDIVIDE\n',
    'number_maior' : 'NUMBER\nGREATER\n', 
    'number_menor' : 'NUMBER\nLESS\n', 
    'number_atribuicao' : 'NUMBER\nATTRIBUTION', 
    'number_exclamacao' : 'NUMBER\nDIFFERENT\n',

    #Operadores
    'adicao' : 'PLUS\n',
    'subtracao' : 'MINUS\n',
    'multiplicacao' : 'TIMES\n',
    'divisao':'',
    'divisao_final' : 'DIVIDE\n',
    'maior' : '',
    'maior_igual' : 'GREATER_EQUAL\n',
    'maior_finalizado' : 'GREATER\n',
    'menor' : '',
    'menor_igual' : 'LESS_EQUAL\n',
    'menor_finalizado' : 'LESS\n',
    'atribuicao' : '',
    'igual' : 'EQUALS\n',
    'atribuicao_finalizado' : 'ATTRIBUTION\n',
    'exclamacao' : '',
    'exclamacao_igual' : 'DIFFERENT\n',
    'virgula' : 'COMMA\n',
    'ponto_virgula' : 'SEMICOLON\n',
    'ponto' : '',
    'esq_parenteses' : 'LPAREN\n',
    'dir_parenteses' : 'RPAREN\n',
    'esq_colchetes' : 'LBRACKETS\n',
    'dir_colchetes' : 'RBRACKETS\n',
    'esq_chaves' : 'LBRACES\n',
    'dir_chaves' : 'RBRACES\n',

    #Float
    'f' : '',
    'fl' : '',
    'flo' : '',
    'floa' : '',
    'float' : '',
    'float_esq_parenteses' : 'FLOAT\nLPAREN\n',
    'float_dir_parenteses' : 'FLOAT\nRPAREN\n',
    'float_final' : 'FLOAT\n',

    'esq_parenteses' : 'LPAREN\n',
    'dir_parenteses' : 'RPAREN\n',
    'esq_colchetes' : 'LBRACKETS\n',
    'dir_colchetes' : 'RBRACKETS\n',
    'esq_chaves' : 'LBRACES\n',
    'dir_chaves' : 'RBRACES\n',

    'divisao_multiplicacao' : '',
    'comentario' : '',
    'comentario_multiplicacao' : '',
    'comentario_finalizado' : '',
}