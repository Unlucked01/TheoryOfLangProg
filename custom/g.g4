grammar g;

program : variableDeclaration computationDescription ;

computationDescription : 'BEGIN' operatorsList 'END' ;

variableDeclaration : 'VAR' variableList ':' 'LOGICAL' ';' ;

variableList : identifier (',' identifier)* ;

operatorsList : (assignment+ | loop | read | write)+  ;

assignment : identifier '=' expression ';' ;

expression : unaryOperator subexpression | subexpression ;

subexpression : '(' expression ')' | operand | subexpression binaryOperator subexpression ;

unaryOperator : '.NOT.' ;

binaryOperator : '.AND.' | '.OR.' | '.IMP.' ;

operand : identifier | constant ;

identifier : LETTER*;

constant : '0' | '1' ;

read : 'READ' '(' variableList ')' ';' ;

loop : 'WHILE' expression 'DO' operatorsList 'END_WHILE' ;

write : 'WRITE' '(' variableList ')' ';' ;

LETTER : [a-zA-Z];

INT : [0-9]+;

WS : [ \t\r\n]+ -> skip;