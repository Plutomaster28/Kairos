class Interpreter:
    def __init__(self):
        self.variables = {}
        self.debug = False

    def set_debug(self, value):
        self.debug = value

    def eval(self, node):
        if self.debug:
            print(f"Evaluating node: {node}")

        if node[0] == 'ASSIGN':
            var_name = node[1]
            value = self.eval(node[2])
            self.variables[var_name] = value
            if self.debug:
                print(f"Assigned {value} to {var_name}")
        elif node[0] == 'NUMBER':
            return int(node[1])
        elif node[0] == 'STRING':
            return node[1].strip('"')  # Remove surrounding quotes
        elif node[0] == 'ID':
            value = self.variables.get(node[1], "Undefined variable")
            if self.debug:
                print(f"Retrieved {value} for {node[1]}")
            return value
        else:
            raise ValueError("Unknown node type: %s" % node[0])

    def echo(self, node):
        if node[0] == 'STRING':
            value = node[1].strip('"')  # Handle string literals
        elif node[0] == 'ID':
            value = self.variables.get(node[1], "Undefined variable")
        else:
            raise ValueError("Unknown node type for echo")
        
        if self.debug:
            print(f"Echoing {value}")
        print(value)
