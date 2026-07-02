grammar Expr;

root : expr EOF;

expr : expr MAYOR expr| IDT| NUM| IF expr DOTDOBLE expr ;

IF : 'if' ;
DOTDOBLE : ':' ;
NUM : [0-9]+ ;
IDT : [a-zA-Z]+ ;
MAYOR : '>' ;
WS : [ \t\r\n]+ -> skip ;