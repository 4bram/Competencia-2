# Importa ANTLR4 para funciones
from antlr4 import *

from ExprLexer import ExprLexer

import sys

import os

if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    # Si el archivo existe, lo procesa como un archivo
    input_stream = FileStream(sys.argv[1])
else:
    # Si no existe el archivo, lo procesa como texto directo
    input_stream = InputStream(input("? "))

# Lo que obtienes es la entrada, analiza el texto y lo separa en tokens
lexer = ExprLexer(input_stream)
# Toma los tokens que produjo el lexer 
tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ", token.text)
    print("Tipo ", token.type)
    print("Linea ", token.line)
    print("Columna ", token.column)
    nombre = lexer.symbolicNames[token.type]
    print("Nombre ", nombre)

    print("--------------------------------------------------")
