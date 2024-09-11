from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

def run_kairos():
    interpreter = Interpreter()
    while True:
        try:
            code = input("kairos> ")
            if code.strip() == 'exit':
                break

            tokens = tokenize(code)
            if not tokens:
                continue  # Skip empty input

            # Check if the command is to toggle debugging
            if tokens[0][1] == 'debug':
                if len(tokens) > 1 and tokens[1][1] == 'on':
                    interpreter.set_debug(True)
                    print("Debugging turned on")
                elif len(tokens) > 1 and tokens[1][1] == 'off':
                    interpreter.set_debug(False)
                    print("Debugging turned off")
                else:
                    print("Usage: debug on | off")
            else:
                # Handle other commands
                parser = Parser(tokens)
                ast = parser.parse()
                
                if ast[0] == 'ASSIGN':
                    interpreter.eval(ast)
                elif ast[0] == 'ECHO':
                    interpreter.echo(ast[1])
                else:
                    print("Unknown statement")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    run_kairos()
