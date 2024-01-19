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
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\5\3 \n\3\3\3\5\3#\n\3\3\3\5\3&\n\3\3\4\3\4")
        buf.write("\5\4*\n\4\3\4\5\4-\n\4\3\4\5\4\60\n\4\3\5\3\5\5\5\64\n")
        buf.write("\5\3\5\5\5\67\n\5\3\5\5\5:\n\5\3\6\3\6\5\6>\n\6\3\6\5")
        buf.write("\6A\n\6\3\6\5\6D\n\6\3\7\6\7G\n\7\r\7\16\7H\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\n\3\n\2\2\13\3\3\5\2\7\2\t\2\13\2")
        buf.write("\r\4\17\5\21\6\23\7\3\2\5\3\2\63;\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2[\2\3\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5%\3\2\2\2\7/\3\2\2\2")
        buf.write("\t9\3\2\2\2\13C\3\2\2\2\rF\3\2\2\2\17L\3\2\2\2\21O\3\2")
        buf.write("\2\2\23Q\3\2\2\2\25\26\5\5\3\2\26\27\7\60\2\2\27\30\5")
        buf.write("\7\4\2\30\31\7\60\2\2\31\32\5\t\5\2\32\33\7\60\2\2\33")
        buf.write("\34\5\13\6\2\34\4\3\2\2\2\35\37\t\2\2\2\36 \t\3\2\2\37")
        buf.write("\36\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2!#\t\3\2\2\"!\3\2\2")
        buf.write("\2\"#\3\2\2\2#&\3\2\2\2$&\t\3\2\2%\35\3\2\2\2%$\3\2\2")
        buf.write("\2&\6\3\2\2\2\')\t\2\2\2(*\t\3\2\2)(\3\2\2\2)*\3\2\2\2")
        buf.write("*,\3\2\2\2+-\t\3\2\2,+\3\2\2\2,-\3\2\2\2-\60\3\2\2\2.")
        buf.write("\60\t\3\2\2/\'\3\2\2\2/.\3\2\2\2\60\b\3\2\2\2\61\63\t")
        buf.write("\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66")
        buf.write("\3\2\2\2\65\67\t\3\2\2\66\65\3\2\2\2\66\67\3\2\2\2\67")
        buf.write(":\3\2\2\28:\t\3\2\29\61\3\2\2\298\3\2\2\2:\n\3\2\2\2;")
        buf.write("=\t\2\2\2<>\t\3\2\2=<\3\2\2\2=>\3\2\2\2>@\3\2\2\2?A\t")
        buf.write("\3\2\2@?\3\2\2\2@A\3\2\2\2AD\3\2\2\2BD\t\3\2\2C;\3\2\2")
        buf.write("\2CB\3\2\2\2D\f\3\2\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2\2")
        buf.write("HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\7\2\2K\16\3\2\2\2L")
        buf.write("M\13\2\2\2MN\b\b\3\2N\20\3\2\2\2OP\13\2\2\2P\22\3\2\2")
        buf.write("\2QR\13\2\2\2R\24\3\2\2\2\20\2\37\"%),/\63\669=@CH\4\b")
        buf.write("\2\2\3\b\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IPv4 = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IPv4", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IPv4", "FIRST", "SECOND", "THIRD", "FOURTH", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[6] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


