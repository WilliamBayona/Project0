import re
#parser

tokenLibrary=[
    ("EXEC", r"exec" ),
    ("NEW", r"new"),
    ("VALUE", r"\d+(\.\d*)?"),
    ("MACRO", r"macro"),
    ("VAR", r"var"), 
    #("PARAM", r"\(([a-zA-Z_][a-zA-Z0-9_]*)\)"),
    ("LPAREN", r"\("), #Parentesis Izquierdo
    ("RPAREN", r"\)"), #Parentesis derecho    
    ("EQUALS", r"\="), 
    ("WHITESPACE", r"\s+"),
    ("NAME", r"\w+"), #Nombre
    ("LCORCH", r"\{"), #Corchete Izquierdo de BLOQUE
    ("RCORCH", r"\}") #Corchete Derecho de BLOQUE
    
    #INSTRUCCIONES
    ##COMANDOS
    ("TURNTOMY", r"turntomy"),
    ('D', r'\b(left|right|back)\b'),
    
    ("TURNTOTHE", r"turntothe"),
    ('O', r'\b(north|south|east|west)\b'),
    ("WALK", r"walk"),
    ("JUMP", r"jump"),
    ("DROP", r"drop"),
    ("PICK", r"pick"),
    ("GRAB", r"grab"),
    ("LETGO", r"letgo"),
    ("POP", r"pop"),
    ("MOVES", r"moves"),
    ("MLIST", r"^(forward|right|left|backwards)(,((forward|right|left|backwards))*$"),
    
    
    
     
    
       
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokenLibrary)

print(token_regex)


def lexer(input_text):
    tokens = []
    for match in re.finditer(token_regex, input_text):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'WHITESPACE':
            continue  # Ignorar espacios en blanco

        tokens.append((token_type, token_value))
    
    return tokens

# Ejemplo de uso
input_text = "NEW VAR HOLA = (3)"
input_text = input_text.lower()

tokens = lexer(input_text)
print(tokens)

