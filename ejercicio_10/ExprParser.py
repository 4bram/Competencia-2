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
        4,1,6,14,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        0,0,2,0,2,0,0,11,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,
        6,1,1,0,0,0,7,8,5,1,0,0,8,9,5,2,0,0,9,10,5,3,0,0,10,11,5,4,0,0,11,
        12,5,5,0,0,12,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "<INVALID>", "')'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "IDT", "LPAREN", "STR", "RPAREN", "SCOLON", 
                      "WS" ]

    RULE_root = 0
    RULE_stmt = 1

    ruleNames =  [ "root", "stmt" ]

    EOF = Token.EOF
    IDT=1
    LPAREN=2
    STR=3
    RPAREN=4
    SCOLON=5
    WS=6

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

        def stmt(self):
            return self.getTypedRuleContext(ExprParser.StmtContext,0)


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
            self.stmt()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDT(self):
            return self.getToken(ExprParser.IDT, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def STR(self):
            return self.getToken(ExprParser.STR, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def SCOLON(self):
            return self.getToken(ExprParser.SCOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.IDT)
            self.state = 8
            self.match(ExprParser.LPAREN)
            self.state = 9
            self.match(ExprParser.STR)
            self.state = 10
            self.match(ExprParser.RPAREN)
            self.state = 11
            self.match(ExprParser.SCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





