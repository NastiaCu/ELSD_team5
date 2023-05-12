grammar Expr;
prog:    'func process()''{'(NEWLINE? statement NEWLINE?)*'}' NEWLINE 'func compose()''{'(NEWLINE? statement NEWLINE?)*'}';
statement:   query_invocation
        |   comments
        ;
query_invocation:   variable_declaration
                |   method_invocation
                |   method_declaration
                |   assignment_statement
                ;
term: variable | INT;
variable: CHR;
variable_declaration: CHR '=' (INT|CHR|method_invocation);
method_invocation: method_name '('(INT|CHR|STRING)* ','*? ')';
method_name: 'load' | 'delay' | 'setreverb' | 'setgain' | 'changepitch' |'fadein' | 'fadeout' | 'play' | 'splice';
assignment_statement: CHR '=' (CHR | INT);
method_declaration: 'func ' CHR '(' CHR* ','*?')' '{' (NEWLINE? statement NEWLINE?)* '}';

comments: '//' STRING;
STRING  : [CHR/,.]+;
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
CHR : [a-z]+;
WS  : [ \t\n\r] -> skip;


