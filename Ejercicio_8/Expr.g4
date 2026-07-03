grammar Expr;

root : expr EOF;

expr :  IDT expr | MAYOR expr| IGUAL expr| NUM expr;

IDT : [a-zA-Z]+;
MAYOR : '>';
IGUAL : '=';
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
