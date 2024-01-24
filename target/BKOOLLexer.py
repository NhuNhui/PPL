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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\f\7\fF\n\f\f\f\16\fI\13\f\5\fK\n\f\3\r\3\r")
        buf.write("\3\r\6\rP\n\r\r\r\16\rQ\3\16\3\16\3\17\6\17W\n\17\r\17")
        buf.write("\16\17X\3\20\3\20\3\20\3\20\3\21\3\21\3\21\2\2\22\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22\3\2\7\3\2\63;\3\2\62;\5\2,-//\61")
        buf.write("\61\4\2C\\c|\5\2\13\f\17\17\"\"\2d\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5*\3\2\2\2\7.\3\2\2\2\t")
        buf.write("\64\3\2\2\2\13\66\3\2\2\2\r8\3\2\2\2\17:\3\2\2\2\21<\3")
        buf.write("\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27J\3\2\2\2\31L\3\2\2\2")
        buf.write("\33S\3\2\2\2\35V\3\2\2\2\37Z\3\2\2\2!^\3\2\2\2#$\7t\2")
        buf.write("\2$%\7g\2\2%&\7v\2\2&\'\7w\2\2\'(\7t\2\2()\7p\2\2)\4\3")
        buf.write("\2\2\2*+\7k\2\2+,\7p\2\2,-\7v\2\2-\6\3\2\2\2./\7h\2\2")
        buf.write("/\60\7n\2\2\60\61\7q\2\2\61\62\7c\2\2\62\63\7v\2\2\63")
        buf.write("\b\3\2\2\2\64\65\7=\2\2\65\n\3\2\2\2\66\67\7.\2\2\67\f")
        buf.write("\3\2\2\289\7*\2\29\16\3\2\2\2:;\7+\2\2;\20\3\2\2\2<=\7")
        buf.write("}\2\2=\22\3\2\2\2>?\7\177\2\2?\24\3\2\2\2@A\7?\2\2A\26")
        buf.write("\3\2\2\2BK\7\62\2\2CG\t\2\2\2DF\t\3\2\2ED\3\2\2\2FI\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2HK\3\2\2\2IG\3\2\2\2JB\3\2\2")
        buf.write("\2JC\3\2\2\2K\30\3\2\2\2LM\5\27\f\2MO\7\60\2\2NP\t\3\2")
        buf.write("\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\32\3\2\2\2")
        buf.write("ST\t\4\2\2T\34\3\2\2\2UW\t\5\2\2VU\3\2\2\2WX\3\2\2\2X")
        buf.write("V\3\2\2\2XY\3\2\2\2Y\36\3\2\2\2Z[\t\6\2\2[\\\3\2\2\2\\")
        buf.write("]\b\20\2\2] \3\2\2\2^_\13\2\2\2_`\b\21\3\2`\"\3\2\2\2")
        buf.write("\7\2GJQX\4\b\2\2\3\21\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT = 2
    FLOAT = 3
    SM = 4
    CM = 5
    LR = 6
    RR = 7
    LB = 8
    RB = 9
    ASS = 10
    INTDEF = 11
    FLOATDEF = 12
    OPERATOR = 13
    ID = 14
    WS = 15
    ERROR_CHAR = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'int'", "'float'", "';'", "','", "'('", "')'", 
            "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "SM", "CM", "LR", "RR", "LB", "RB", "ASS", "INTDEF", 
            "FLOATDEF", "OPERATOR", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INT", "FLOAT", "SM", "CM", "LR", "RR", "LB", 
                  "RB", "ASS", "INTDEF", "FLOATDEF", "OPERATOR", "ID", "WS", 
                  "ERROR_CHAR" ]

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
            actions[15] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


