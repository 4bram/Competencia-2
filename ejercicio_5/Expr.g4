grammar Expr;

root : expr EOF;

expr : expr PRINT expr| CADENA ;

PRINT : 'print' ;
CADENA : '"' ~["\r\n]* '"' ;
WS : [ \t\r\n]+ -> skip ;