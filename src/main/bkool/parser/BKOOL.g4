grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.


program: EOF;


FLOAT:NORMAL|SCIENCE1|SCIENCE2;
fragment NORMAL:INT '.' [0-9]*;
fragment SCIENCE1:INT '.' [0-9]+ EXP '-'? INT;
fragment SCIENCE2:INT EXP '-'? INT;
fragment INT:'0'|[1-9] [0-9]*;
fragment EXP:'e'|'E';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;