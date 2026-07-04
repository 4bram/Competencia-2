grammar Expr;

root : ifstmt EOF;

ifstmt : IF LPAREN expr RPAREN DOBLE;

expr : expr MAYOR expr| IDT| NUM;

IF : 'if';
WS : [ \t\r\n]+ -> skip ;
LPAREN : '(';
IDT : [a-zA-Z_][a-zA-Z0-9_]*;
MAYOR : '>';
NUM : [0-9]+ ;
RPAREN : ')';
DOBLE : ':';