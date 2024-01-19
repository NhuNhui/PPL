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


IPv4: FIRST '.' SECOND '.' THIRD '.' FOURTH;
fragment FIRST: [1-9] [0-9]? [0-9]?| [0-9];
fragment SECOND: [1-9] [0-9]? [0-9]?| [0-9];
fragment THIRD: [1-9] [0-9]? [0-9]?| [0-9];
fragment FOURTH: [1-9] [0-9]? [0-9]?| [0-9];





WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;