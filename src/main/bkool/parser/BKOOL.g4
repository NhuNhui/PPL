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


program: declaration+ EOF;

declaration: variableDeclaration | functionDeclaration;
variableDeclaration: typ var SM;
typ: INT|FLOAT;
var: ID (CM ID)*;

functionDeclaration: typ ID LR paramlist RR body;
paramlist: param(SM param)*| ;
param: typ var; 

body: LB bodyfunc RB;
bodyfunc: typefunc* re;
typefunc: assign|variableDeclaration|callf;
assign: ID ASS expr SM;
callf: ID* LR expr(CM expr)* RR SM; 
re: 'return' expr SM;

INT: 'int';
FLOAT: 'float';
SM: ';';
CM: ',';
LR: '(';
RR: ')';
LB: '{';
RB: '}';
ASS: '=';
expr: typexpr (OPERATOR typexpr)*;
typexpr: number|ID|funcsmall;
funcsmall: ID+ LR (number|ID) (CM ID)* RR;
number: INTDEF|FLOATDEF;
INTDEF: '0'|([1-9] [0-9]*);
FLOATDEF: INTDEF '.' [0-9]+;
OPERATOR: '+'|'-'|'*'|'/';
ID: [a-zA-Z]+;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
