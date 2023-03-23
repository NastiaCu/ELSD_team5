import re
from token import Token
from token import TokenType

class Lexer:
    def __init__(self, code):
        self.code = code
        self.token_patterns = [
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('COMMA', r','),
            ('ASSIGN', r'='),
            ('ADD', r'add\b'),
            ('SEMICOLON', r';'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('GREATER', r'>'),
            ('GREATER_EQUAL', r'>='),
            ('EQUAL', r'=='),
            ('LESS', r'<'),
            ('LESS_EQUAL', r'<='),
            ('NOT_EQUAL', r'!='),
            ('IF', r'if\b'),
            ('ELSE', r'else\b'),
            ('FOR', r'for\b'),
            ('WHILE', r'while\b'),
            ('IN', r'in\b'),
            ('RETURN', r'return\b'),
            ('BREAK', r'break\b'),
            ('CONTINUE', r'continue\b'),
            ('VAR', r'var\b'),
            ('FUNC', r'func\b'),
            ('ID', r'[a-zA-Z_]\w*'),
            ('NUMBER', r'\d+(\.\d+)?'),
            ('STRING', r'"[^"]*"'),
            ('WHITESPACE', r'\s+'),
            ('COMMENT', r'//.*'),
            ('INVALID', r'.')
        ]
        self.token_regex = re.compile('|'.join('(?P<%s>%s)' % pair for pair in self.token_patterns))

    def tokenize(self, program):
        tokens = []
        for match in self.token_regex.finditer(program):
            type = match.lastgroup
            value = match.group()
            token = Token(type, value)
            if type != 'WHITESPACE' and type != 'COMMENT':
                tokens.append(token)
        return tokens

    def __iter__(self):
        tokens = self.tokenize(self.code)
        yield from tokens
        yield Token(TokenType.EOF, '')
