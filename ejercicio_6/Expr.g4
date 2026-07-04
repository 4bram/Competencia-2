grammar Expr;

root : expr EOF;

expr : expr MAS expr| NUM | MUL expr;

NUM : [0-9]+ ;
MAS : '+' ;
MUL : '*' ;
WS : [ \t\r\n]+ -> skip ;