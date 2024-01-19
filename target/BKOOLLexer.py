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
        buf.write("\67\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\5\2")
        buf.write("\32\n\2\3\2\3\2\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\3\3")
        buf.write("\3\3\4\5\4(\n\4\3\5\6\5+\n\5\r\5\16\5,\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\2\2\t\3\3\5\2\7\2\t\4\13\5\r\6\17")
        buf.write("\7\3\2\4\b\2\"\"/\60\62;AAC\\c|\5\2\13\f\17\17\"\"\28")
        buf.write("\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\3\21\3\2\2\2\5\35\3\2\2\2\7\'\3\2\2\2\t*\3\2")
        buf.write("\2\2\13\60\3\2\2\2\r\63\3\2\2\2\17\65\3\2\2\2\21\25\7")
        buf.write(")\2\2\22\24\5\7\4\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\30")
        buf.write("\32\5\5\3\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\34\7)\2\2\34\4\3\2\2\2\35!\7)\2\2\36 \5\7\4\2\37\36")
        buf.write("\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#")
        buf.write("!\3\2\2\2$%\7)\2\2%\6\3\2\2\2&(\t\2\2\2\'&\3\2\2\2(\b")
        buf.write("\3\2\2\2)+\t\3\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2")
        buf.write("\2\2-.\3\2\2\2./\b\5\2\2/\n\3\2\2\2\60\61\13\2\2\2\61")
        buf.write("\62\b\6\3\2\62\f\3\2\2\2\63\64\13\2\2\2\64\16\3\2\2\2")
        buf.write("\65\66\13\2\2\2\66\20\3\2\2\2\b\2\25\31!\',\4\b\2\2\3")
        buf.write("\6\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENTIFIER = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INDENTIFIER", "QC", "CHAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[4] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


