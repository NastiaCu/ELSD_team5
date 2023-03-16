import re

# Define the regular expressions for each token type
token_patterns = {
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'COMMA': r',',
    'ASSIGN': r'=',
    'SEMICOLON': r';',
    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'GREATER': r'>',
    'GREATER_EQUAL': r'>=',
    'EQUAL': r'==',
    'LESS': r'<',
    'LESS_EQUAL': r'<=',
    'NOT_EQUAL': r'!=',
    'IF': r'if',
    'ELSE': r'else',
    'FOR': r'for',
    'RETURN': r'return',
    'BREAK': r'break',
    'CONTINUE': r'continue',
    'VAR': r'var',
    'FUNC': r'func',
    'ID': r'[a-zA-Z_]\w*',
    'NUMBER': r'\d+(\.\d+)?',
    'STRING': r'"[^"]*"',
    'WHITESPACE': r'\s+',
    'COMMENT': r'//.*'
}

# Compile the regular expressions into a list of (token_name, regex) tuples
token_regexes = [(name, re.compile(pattern)) for name, pattern in token_patterns.items()]


def tokenize(program):
    # Initialize an empty list to store the resulting tokens
    tokens = []

    # Loop through the program string, matching each token to its corresponding regex
    while program:
        match = None
        for token_name, regex in token_regexes:
            match = regex.match(program)
            if match:
                # Add the matched token to the list of tokens, and update the remaining program string
                token = (token_name, match.group(0))
                tokens.append(token)
                program = program[len(token[1]):]
                break
        if not match:
            # If no token pattern matched, raise a syntax error
            raise SyntaxError('Invalid syntax: {}'.format(program))

    return tokens

program = '''
func process() {
    var x = 123;
    var y = "hello, world!";
    set_gain(x + 456);
    if (x > 100) {
        return y;
    } else {
        for i = 0, 10 {
            delay(i);
        }
        break;
    }
}
'''

tokens = tokenize(program)

for token in tokens:
    print(token)
