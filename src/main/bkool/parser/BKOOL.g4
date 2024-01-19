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


BKNETID: FIRST+ '.' SECOND+ FREE? FREE? FREE? FREE? END;
fragment FIRST: [a-z];
fragment SECOND: [a-z];
fragment FREE: [a-z0-9]|'_'|'.';
fragment END: [a-z0-9]|'_';




WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;