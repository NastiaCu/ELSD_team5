# Generated from Expr.g4 by ANTLR 4.12.0
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
        4,1,24,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,3,0,26,8,0,1,0,1,
        0,3,0,30,8,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,0,1,0,1,0,3,0,
        42,8,0,1,0,1,0,3,0,46,8,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,1,
        1,1,1,3,1,57,8,1,1,2,1,2,1,2,1,2,3,2,63,8,2,1,3,1,3,3,3,67,8,3,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,5,6,81,8,6,10,6,
        12,6,84,9,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,104,8,9,10,9,12,9,107,9,9,1,9,5,
        9,110,8,9,10,9,12,9,113,9,9,1,9,1,9,1,9,3,9,118,8,9,1,9,1,9,3,9,
        122,8,9,5,9,124,8,9,10,9,12,9,127,9,9,1,9,1,9,1,10,1,10,1,10,1,10,
        2,88,111,0,11,0,2,4,6,8,10,12,14,16,18,20,0,3,2,0,20,20,22,23,1,
        0,9,17,1,0,22,23,142,0,22,1,0,0,0,2,56,1,0,0,0,4,62,1,0,0,0,6,66,
        1,0,0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,77,1,0,0,0,14,93,1,0,0,0,16,
        95,1,0,0,0,18,99,1,0,0,0,20,130,1,0,0,0,22,23,5,1,0,0,23,33,5,2,
        0,0,24,26,5,21,0,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,
        29,3,2,1,0,28,30,5,21,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,32,1,0,
        0,0,31,25,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,
        1,0,0,0,35,33,1,0,0,0,36,37,5,3,0,0,37,38,5,21,0,0,38,39,5,4,0,0,
        39,49,5,2,0,0,40,42,5,21,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,
        0,0,0,43,45,3,2,1,0,44,46,5,21,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,
        48,1,0,0,0,47,41,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,
        0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,3,0,0,53,1,1,0,0,0,54,57,3,
        4,2,0,55,57,3,20,10,0,56,54,1,0,0,0,56,55,1,0,0,0,57,3,1,0,0,0,58,
        63,3,10,5,0,59,63,3,12,6,0,60,63,3,18,9,0,61,63,3,16,8,0,62,58,1,
        0,0,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,5,1,0,0,0,64,
        67,3,8,4,0,65,67,5,22,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,7,1,0,0,
        0,68,69,5,23,0,0,69,9,1,0,0,0,70,71,5,23,0,0,71,75,5,5,0,0,72,76,
        5,22,0,0,73,76,5,23,0,0,74,76,3,12,6,0,75,72,1,0,0,0,75,73,1,0,0,
        0,75,74,1,0,0,0,76,11,1,0,0,0,77,78,3,14,7,0,78,82,5,6,0,0,79,81,
        7,0,0,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,
        83,88,1,0,0,0,84,82,1,0,0,0,85,87,5,7,0,0,86,85,1,0,0,0,87,90,1,
        0,0,0,88,89,1,0,0,0,88,86,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,
        92,5,8,0,0,92,13,1,0,0,0,93,94,7,1,0,0,94,15,1,0,0,0,95,96,5,23,
        0,0,96,97,5,5,0,0,97,98,7,2,0,0,98,17,1,0,0,0,99,100,5,18,0,0,100,
        101,5,23,0,0,101,105,5,6,0,0,102,104,5,23,0,0,103,102,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,111,1,0,0,0,107,
        105,1,0,0,0,108,110,5,7,0,0,109,108,1,0,0,0,110,113,1,0,0,0,111,
        112,1,0,0,0,111,109,1,0,0,0,112,114,1,0,0,0,113,111,1,0,0,0,114,
        115,5,8,0,0,115,125,5,2,0,0,116,118,5,21,0,0,117,116,1,0,0,0,117,
        118,1,0,0,0,118,119,1,0,0,0,119,121,3,2,1,0,120,122,5,21,0,0,121,
        120,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,117,1,0,0,0,124,
        127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,
        125,1,0,0,0,128,129,5,3,0,0,129,19,1,0,0,0,130,131,5,19,0,0,131,
        132,5,20,0,0,132,21,1,0,0,0,17,25,29,33,41,45,49,56,62,66,75,82,
        88,105,111,117,121,125
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func process()'", "'{'", "'}'", "'func compose()'", 
                     "'='", "'('", "','", "')'", "'load'", "'delay'", "'setreverb'", 
                     "'setgain'", "'changepitch'", "'fadein'", "'fadeout'", 
                     "'play'", "'splice'", "'func '", "'//'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STRING", "NEWLINE", "INT", "CHR", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_query_invocation = 2
    RULE_term = 3
    RULE_variable = 4
    RULE_variable_declaration = 5
    RULE_method_invocation = 6
    RULE_method_name = 7
    RULE_assignment_statement = 8
    RULE_method_declaration = 9
    RULE_comments = 10

    ruleNames =  [ "prog", "statement", "query_invocation", "term", "variable", 
                   "variable_declaration", "method_invocation", "method_name", 
                   "assignment_statement", "method_declaration", "comments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    STRING=20
    NEWLINE=21
    INT=22
    CHR=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ExprParser.T__0)
            self.state = 23
            self.match(ExprParser.T__1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11533824) != 0):
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 24
                    self.match(ExprParser.NEWLINE)


                self.state = 27
                self.statement()
                self.state = 29
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 28
                    self.match(ExprParser.NEWLINE)


                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(ExprParser.T__2)
            self.state = 37
            self.match(ExprParser.NEWLINE)
            self.state = 38
            self.match(ExprParser.T__3)
            self.state = 39
            self.match(ExprParser.T__1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11533824) != 0):
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 40
                    self.match(ExprParser.NEWLINE)


                self.state = 43
                self.statement()
                self.state = 45
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.match(ExprParser.NEWLINE)


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(ExprParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query_invocation(self):
            return self.getTypedRuleContext(ExprParser.Query_invocationContext,0)


        def comments(self):
            return self.getTypedRuleContext(ExprParser.CommentsContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.query_invocation()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.comments()
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


    class Query_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ExprParser.Variable_declarationContext,0)


        def method_invocation(self):
            return self.getTypedRuleContext(ExprParser.Method_invocationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(ExprParser.Method_declarationContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ExprParser.Assignment_statementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_query_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_invocation" ):
                listener.enterQuery_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_invocation" ):
                listener.exitQuery_invocation(self)




    def query_invocation(self):

        localctx = ExprParser.Query_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query_invocation)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.method_invocation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.method_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.assignment_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(ExprParser.VariableContext,0)


        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ExprParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.variable()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ExprParser.INT)
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


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHR(self):
            return self.getToken(ExprParser.CHR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = ExprParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.CHR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHR)
            else:
                return self.getToken(ExprParser.CHR, i)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def method_invocation(self):
            return self.getTypedRuleContext(ExprParser.Method_invocationContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)




    def variable_declaration(self):

        localctx = ExprParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ExprParser.CHR)
            self.state = 71
            self.match(ExprParser.T__4)
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 72
                self.match(ExprParser.INT)
                pass
            elif token in [23]:
                self.state = 73
                self.match(ExprParser.CHR)
                pass
            elif token in [9, 10, 11, 12, 13, 14, 15, 16, 17]:
                self.state = 74
                self.method_invocation()
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


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_name(self):
            return self.getTypedRuleContext(ExprParser.Method_nameContext,0)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def CHR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHR)
            else:
                return self.getToken(ExprParser.CHR, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.STRING)
            else:
                return self.getToken(ExprParser.STRING, i)

        def getRuleIndex(self):
            return ExprParser.RULE_method_invocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_invocation" ):
                listener.enterMethod_invocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_invocation" ):
                listener.exitMethod_invocation(self)




    def method_invocation(self):

        localctx = ExprParser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.method_name()
            self.state = 78
            self.match(ExprParser.T__5)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13631488) != 0):
                self.state = 79
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13631488) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 85
                    self.match(ExprParser.T__6) 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 91
            self.match(ExprParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_method_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_name" ):
                listener.enterMethod_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_name" ):
                listener.exitMethod_name(self)




    def method_name(self):

        localctx = ExprParser.Method_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 261632) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHR)
            else:
                return self.getToken(ExprParser.CHR, i)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




    def assignment_statement(self):

        localctx = ExprParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ExprParser.CHR)
            self.state = 96
            self.match(ExprParser.T__4)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CHR)
            else:
                return self.getToken(ExprParser.CHR, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def getRuleIndex(self):
            return ExprParser.RULE_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_declaration" ):
                listener.enterMethod_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_declaration" ):
                listener.exitMethod_declaration(self)




    def method_declaration(self):

        localctx = ExprParser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ExprParser.T__17)
            self.state = 100
            self.match(ExprParser.CHR)
            self.state = 101
            self.match(ExprParser.T__5)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 102
                self.match(ExprParser.CHR)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 108
                    self.match(ExprParser.T__6) 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 114
            self.match(ExprParser.T__7)
            self.state = 115
            self.match(ExprParser.T__1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11533824) != 0):
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 116
                    self.match(ExprParser.NEWLINE)


                self.state = 119
                self.statement()
                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.match(ExprParser.NEWLINE)


                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(ExprParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)




    def comments(self):

        localctx = ExprParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ExprParser.T__18)
            self.state = 131
            self.match(ExprParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





