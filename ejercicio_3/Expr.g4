grammar Expr;

root : expr EOF;

expr : expr ASIG expr| IDT| NUM ;

NUM : [0-9]+ ;
IDT : [a-zA-Z]+ ;
ASIG : '=' ;
WS : [ \t\r\n]+ -> skip ;