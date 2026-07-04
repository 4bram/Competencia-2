# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,18,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,1,0,0,2,0,2,0,0,18,0,4,1,0,0,0,2,15,1,0,0,0,4,5,
        3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,5,1,0,0,8,16,3,2,1,0,9,10,5,
        2,0,0,10,16,3,2,1,0,11,12,5,3,0,0,12,16,3,2,1,0,13,14,5,4,0,0,14,
        16,3,2,1,0,15,7,1,0,0,0,15,9,1,0,0,0,15,11,1,0,0,0,15,13,1,0,0,0,
        16,3,1,0,0,0,1,15
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "INT", "IDT", "IGUAL", "NUM", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    INT=1
    IDT=2
    IGUAL=3
    NUM=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def IDT(self):
            return self.getToken(ExprParser.IDT, 0)

        def IGUAL(self):
            return self.getToken(ExprParser.IGUAL, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(ExprParser.INT)
                self.state = 8
                self.expr()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(ExprParser.IDT)
                self.state = 10
                self.expr()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 11
                self.match(ExprParser.IGUAL)
                self.state = 12
                self.expr()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 13
                self.match(ExprParser.NUM)
                self.state = 14
                self.expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





