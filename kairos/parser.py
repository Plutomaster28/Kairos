class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        if self.tokens[0][1] == 'let':
            return self.parse_assignment()
        elif self.tokens[0][1] == 'echo':
            return self.parse_echo()
        else:
            raise SyntaxError("Unknown command")

    def parse_assignment(self):
        self.consume('ID')
        var_name = self.tokens[self.current][1]
        self.consume('ID')
        if self.peek() == 'ASSIGN':
            self.consume('ASSIGN')
            value = self.parse_expression()
            return ('ASSIGN', var_name, value)
        else:
            raise SyntaxError("Expected '=' after variable name")

    def parse_echo(self):
        self.consume('ID')
        if self.peek() == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            if self.peek() == 'RPAREN':
                self.consume('RPAREN')
                return ('ECHO', expr)
            else:
                raise SyntaxError("Expected ')' after expression")
        else:
            expr = self.parse_expression()
            return ('ECHO', expr)

    def parse_expression(self):
        token_type, token_value = self.tokens[self.current]
        if token_type == 'STRING':
            self.consume('STRING')
            return ('STRING', token_value)
        elif token_type == 'NUMBER':
            self.consume('NUMBER')
            return ('NUMBER', token_value)
        elif token_type == 'ID':
            self.consume('ID')
            return ('ID', token_value)
        else:
            raise SyntaxError("Unexpected token")

    def consume(self, expected_type):
        if self.peek() == expected_type:
            self.current += 1
        else:
            raise SyntaxError(f"Expected {expected_type}, got {self.peek()}")

    def peek(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current][0]
        return 'EOF'
