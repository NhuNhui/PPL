# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4\3\4\6")
        buf.write("\4(\n\4\r\4\16\4)\3\4\3\4\5\4.\n\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\5\5\65\n\5\3\5\3\5\3\6\3\6\3\6\7\6<\n\6\f\6\16\6?\13")
        buf.write("\6\5\6A\n\6\3\7\3\7\3\b\6\bF\n\b\r\b\16\bG\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\2\2\f\3\3\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\4\21\5\23\6\25\7\3\2\6\3\2\62;\3\2\63;\4\2GGg")
        buf.write("g\5\2\13\f\17\17\"\"\2U\2\3\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\32\3\2\2\2\5\34\3")
        buf.write("\2\2\2\7$\3\2\2\2\t\61\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2")
        buf.write("\17E\3\2\2\2\21K\3\2\2\2\23N\3\2\2\2\25P\3\2\2\2\27\33")
        buf.write("\5\5\3\2\30\33\5\7\4\2\31\33\5\t\5\2\32\27\3\2\2\2\32")
        buf.write("\30\3\2\2\2\32\31\3\2\2\2\33\4\3\2\2\2\34\35\5\13\6\2")
        buf.write("\35!\7\60\2\2\36 \t\2\2\2\37\36\3\2\2\2 #\3\2\2\2!\37")
        buf.write("\3\2\2\2!\"\3\2\2\2\"\6\3\2\2\2#!\3\2\2\2$%\5\13\6\2%")
        buf.write("\'\7\60\2\2&(\t\2\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2")
        buf.write(")*\3\2\2\2*+\3\2\2\2+-\5\r\7\2,.\7/\2\2-,\3\2\2\2-.\3")
        buf.write("\2\2\2./\3\2\2\2/\60\5\13\6\2\60\b\3\2\2\2\61\62\5\13")
        buf.write("\6\2\62\64\5\r\7\2\63\65\7/\2\2\64\63\3\2\2\2\64\65\3")
        buf.write("\2\2\2\65\66\3\2\2\2\66\67\5\13\6\2\67\n\3\2\2\28A\7\62")
        buf.write("\2\29=\t\3\2\2:<\t\2\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2")
        buf.write("=>\3\2\2\2>A\3\2\2\2?=\3\2\2\2@8\3\2\2\2@9\3\2\2\2A\f")
        buf.write("\3\2\2\2BC\t\4\2\2C\16\3\2\2\2DF\t\5\2\2ED\3\2\2\2FG\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\b\b\2\2J\20\3\2")
        buf.write("\2\2KL\13\2\2\2LM\b\t\3\2M\22\3\2\2\2NO\13\2\2\2O\24\3")
        buf.write("\2\2\2PQ\13\2\2\2Q\26\3\2\2\2\13\2\32!)-\64=@G\4\b\2\2")
        buf.write("\3\t\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOAT = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "FLOAT", "NORMAL", "SCIENCE1", "SCIENCE2", "INT", "EXP", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


