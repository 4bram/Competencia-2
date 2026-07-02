grammar Expr;

root : expr EOF;

expr :  INT expr | IDT expr | IGUAL expr| NUM expr;

INT : 'int';
IDT : [a-zA-Z]+;
IGUAL : '=';
NUM : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;

