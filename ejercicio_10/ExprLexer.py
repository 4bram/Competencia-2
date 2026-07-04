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
        4,0,6,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,2,1,2,5,2,25,8,2,10,
        2,12,2,28,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,37,8,5,11,5,12,5,38,
        1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,4,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,4,0,10,10,13,13,34,34,92,92,3,0,
        9,10,13,13,32,32,44,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,20,1,0,0,0,5,22,1,0,
        0,0,7,31,1,0,0,0,9,33,1,0,0,0,11,36,1,0,0,0,13,17,7,0,0,0,14,16,
        7,1,0,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,2,1,0,0,0,19,17,1,0,0,0,20,21,5,40,0,0,21,4,1,0,0,0,22,26,5,34,
        0,0,23,25,8,2,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,34,0,0,30,6,1,0,0,0,
        31,32,5,41,0,0,32,8,1,0,0,0,33,34,5,59,0,0,34,10,1,0,0,0,35,37,7,
        3,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,
        40,1,0,0,0,40,41,6,5,0,0,41,12,1,0,0,0,4,0,17,26,38,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDT = 1
    LPAREN = 2
    STR = 3
    RPAREN = 4
    SCOLON = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IDT", "LPAREN", "STR", "RPAREN", "SCOLON", "WS" ]

    ruleNames = [ "IDT", "LPAREN", "STR", "RPAREN", "SCOLON", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


