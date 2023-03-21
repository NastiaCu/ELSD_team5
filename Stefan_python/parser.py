from token import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = 0

    def parse(self):
        return self.parse_statements()

    def parse_statements(self):
        statements = []
        while self.pos < len(self.tokens):
            statement = self.parse_statement()
            if statement is not None:
                statements.append(statement)
            self.pos += 1
        return ('Statements', *statements)

    def parse_statement(self):
        if self.match('VAR'):
            return self.parse_var_declaration()
        elif self.match('ID') and self.match('ASSIGN'):
            return self.parse_assignment()
        elif self.match('IF'):
            return self.parse_if_statement()
        elif self.match('FOR'):
            return self.parse_for_loop()
        elif self.match('WHILE'):
            return self.parse_while_loop()
        elif self.match('FUNC'):
            return self.parse_function_declaration()
        elif self.match('RETURN'):
            return self.parse_return_statement()
        elif self.match('BREAK'):
            return self.parse_break_statement()
        elif self.match('CONTINUE'):
            return self.parse_continue_statement()
        else:
            return None

    def parse_var_declaration(self):
        name = self.consume('ID').value
        if self.match('ASSIGN'):
            self.consume('ASSIGN')
            value = self.parse_expression()
        else:
            value = None
        self.consume('SEMICOLON')
        return ('VarDeclaration', name, value)

    def parse_assignment(self):
        name = self.consume('ID').value
        self.consume('ASSIGN')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return ('Assignment', name, value)
    def parse_if_statement(self):
        self.consume('IF')
        condition = self.parse_expression()
        self.consume('LBRACE')
        if_body = self.parse_statements()
        self.consume('RBRACE')
        if self.match('ELSE'):
            self.consume('ELSE')
            self.consume('LBRACE')
            else_body = self.parse_statements()
            self.consume('RBRACE')
        else:
            else_body = None
        return ('IfStatement', condition, if_body, else_body)

    def parse_for_loop(self):
        self.consume('FOR')
        self.consume('LPAREN')
        var_name = self.consume('ID').value
        self.consume('IN')
        iterable = self.parse_expression()
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return ('ForLoop', var_name, iterable, body)

    def parse_while_loop(self):
        self.consume('WHILE')
        condition = self.parse_expression()
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return ('WhileLoop', condition, body)

    def parse_function_declaration(self):
        self.consume('FUNC')
        name = self.consume('ID').value
        self.consume('LPAREN')
        params = self.parse_parameter_list()
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = self.parse_statements()
        self.consume('RBRACE')
        return ('FunctionDeclaration', name, params, body)

    def parse_parameter_list(self):
        params = []
        if self.match('ID'):
            params.append(self.consume('ID').value)
            while self.match('COMMA'):
                self.consume('COMMA')
                params.append(self.consume('ID').value)
        return params

    def parse_return_statement(self):
        self.consume('RETURN')
        value = self.parse_expression()
        self.consume('SEMICOLON')
        return ('ReturnStatement', value)

    def parse_break_statement(self):
        self.consume('BREAK')
        self.consume('SEMICOLON')
        return ('BreakStatement',)

    def parse_continue_statement(self):
        self.consume('CONTINUE')
        self.consume('SEMICOLON')
        return ('ContinueStatement',)

    def parse_expression(self):
        return self.parse_logical_or_expression()

    def parse_logical_or_expression(self):
        left = self.parse_logical_and_expression()
        while self.match('OR'):
            operator = self.consume('OR').value
            right = self.parse_logical_and_expression()
            left = ('BinaryExpression', operator, left, right)
        return left

    def parse_logical_and_expression(self):
        left = self.parse_equality_expression()
        while self.match('AND'):
            operator = self.consume('AND').value
            right = self.parse_equality_expression()
            left = ('BinaryExpression', operator, left, right)  # change node type to BinaryExpression
        return left

    def parse_equality(self):
        left = self.parse_comparison()
        while self.match('EQUAL') or self.match('NOT_EQUAL'):
            operator = self.consume().value
            right = self.parse_comparison()
            left = ('BinaryExpression', operator, left, right)  # change node type to BinaryExpression
        return left

    def parse_comparison(self):
        left = self.parse_addition()
        while self.match('GREATER') or self.match('GREATER_EQUAL') or \
              self.match('LESS') or self.match('LESS_EQUAL'):
            operator = self.consume().value
            right = self.parse_addition()
            if operator == '>':
                left = ('GreaterThan', left, right)
            elif operator == '>=':
                left = ('GreaterThanEqual', left, right)
            elif operator == '<':
                left = ('LessThan', left, right)
            elif operator == '<=':
                left = ('LessThanEqual', left, right)
        return left

    def parse_addition(self):
        left = self.parse_multiplication()
        while self.match('PLUS') or self.match('MINUS'):
            operator = self.consume().value
            right = self.parse_multiplication()
            left = ('Addition' if operator == '+' else 'Subtraction', left, right)
        return left

    def parse_multiplication(self):
        left = self.parse_unary()
        while self.match('MULTIPLY') or self.match('DIVIDE'):
            operator = self.consume().value
            right = self.parse_unary()
            left = ('Multiplication' if operator == '*' else 'Division', left, right)
        return left

    def parse_unary(self):
        if self.match('MINUS'):
            self.consume('MINUS')
            value = self.parse_unary()
            return ('Negation', value)
        elif self.match('NOT'):
            self.consume('NOT')
            value = self.parse_unary()
            return ('Not', value)
        else:
            return self.parse_primary()

    def parse_primary(self):
        if self.match('LPAREN'):
            self.consume('LPAREN')
            value = self.parse_expression()
            self.consume('RPAREN')
            return value
        elif self.match('NUMBER'):
            return self.parse_number()
        elif self.match('STRING'):
            return self.parse_string()
        elif self.match('ID'):
            if self.peek().type == 'LPAREN':
                return self.parse_function_call()
            else:
                return self.parse_variable()
        else:
            return None

    def parse_number(self):
        token = self.consume('NUMBER')
        return ('Number', float(token.value))

    def parse_string(string):
        parsed = []
        for s in string.split():
            try:
                parsed.append(int(s))
            except ValueError:
                try:
                    parsed.append(float(s))
                except ValueError:
                    parsed.append(s)
        return parsed

    def parse(self):
        ast = self.parse_statements()
        return ast

    def print_ast(self, node, level=0):
        if isinstance(node, tuple):
            print("    " * level + node[0])
            for child in node[1:]:
                self.print_ast(child, level + 1)
        else:
            print("    " * level + str(node))

    def match(self, token_type):
        if self.current_token.type == TokenType:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type} token but got {self.current_token.type}")

