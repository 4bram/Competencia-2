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
        4,1,8,29,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,3,2,19,8,2,1,2,1,2,1,2,5,2,24,8,2,10,2,12,2,27,9,
        2,1,2,0,1,4,3,0,2,4,0,0,27,0,6,1,0,0,0,2,9,1,0,0,0,4,18,1,0,0,0,
        6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,0,0,10,11,5,3,0,0,11,
        12,3,4,2,0,12,13,5,7,0,0,13,14,5,8,0,0,14,3,1,0,0,0,15,16,6,2,-1,
        0,16,19,5,4,0,0,17,19,5,6,0,0,18,15,1,0,0,0,18,17,1,0,0,0,19,25,
        1,0,0,0,20,21,10,3,0,0,21,22,5,5,0,0,22,24,3,4,2,4,23,20,1,0,0,0,
        24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,5,1,0,0,0,27,25,1,0,
        0,0,2,18,25
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "'('", "<INVALID>", 
                     "'>'", "<INVALID>", "')'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "WS", "LPAREN", "IDT", "MAYOR", 
                      "NUM", "RPAREN", "DOBLE" ]

    RULE_root = 0
    RULE_ifstmt = 1
    RULE_expr = 2

    ruleNames =  [ "root", "ifstmt", "expr" ]

    EOF = Token.EOF
    IF=1
    WS=2
    LPAREN=3
    IDT=4
    MAYOR=5
    NUM=6
    RPAREN=7
    DOBLE=8

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

        def ifstmt(self):
            return self.getTypedRuleContext(ExprParser.IfstmtContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.ifstmt()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def DOBLE(self):
            return self.getToken(ExprParser.DOBLE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_ifstmt




    def ifstmt(self):

        localctx = ExprParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(ExprParser.IF)
            self.state = 10
            self.match(ExprParser.LPAREN)
            self.state = 11
            self.expr(0)
            self.state = 12
            self.match(ExprParser.RPAREN)
            self.state = 13
            self.match(ExprParser.DOBLE)
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

        def IDT(self):
            return self.getToken(ExprParser.IDT, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def MAYOR(self):
            return self.getToken(ExprParser.MAYOR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 16
                self.match(ExprParser.IDT)
                pass
            elif token in [6]:
                self.state = 17
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 20
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 21
                    self.match(ExprParser.MAYOR)
                    self.state = 22
                    self.expr(4) 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




