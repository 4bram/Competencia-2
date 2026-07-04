# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,1,4,1,22,8,1,11,1,12,1,23,1,1,1,1,1,
        2,1,2,1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,1,4,1,5,4,5,40,8,5,
        11,5,12,5,41,1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,1,0,4,3,0,9,10,13,13,32,32,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,1,0,48,57,49,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,1,17,1,0,0,0,3,21,1,0,0,0,5,27,1,0,0,0,7,29,1,0,0,0,9,36,1,0,0,
        0,11,39,1,0,0,0,13,43,1,0,0,0,15,45,1,0,0,0,17,18,5,105,0,0,18,19,
        5,102,0,0,19,2,1,0,0,0,20,22,7,0,0,0,21,20,1,0,0,0,22,23,1,0,0,0,
        23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,6,1,0,0,26,4,1,0,
        0,0,27,28,5,40,0,0,28,6,1,0,0,0,29,33,7,1,0,0,30,32,7,2,0,0,31,30,
        1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,8,1,0,0,0,35,
        33,1,0,0,0,36,37,5,62,0,0,37,10,1,0,0,0,38,40,7,3,0,0,39,38,1,0,
        0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,12,1,0,0,0,43,44,
        5,41,0,0,44,14,1,0,0,0,45,46,5,58,0,0,46,16,1,0,0,0,4,0,23,33,41,
        1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    WS = 2
    LPAREN = 3
    IDT = 4
    MAYOR = 5
    NUM = 6
    RPAREN = 7
    DOBLE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'('", "'>'", "')'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "WS", "LPAREN", "IDT", "MAYOR", "NUM", "RPAREN", "DOBLE" ]

    ruleNames = [ "IF", "WS", "LPAREN", "IDT", "MAYOR", "NUM", "RPAREN", 
                  "DOBLE" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


