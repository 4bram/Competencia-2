grammar Expr;

root : stmt EOF;

stmt : IDT LPAREN STR RPAREN SCOLON;

IDT : [a-zA-Z_][a-zA-Z0-9_]*;
LPAREN : '(';
STR : '"' (~["\\\r\n])* '"';
RPAREN : ')';
SCOLON : ';';
WS : [ \t\r\n]+ -> skip ;