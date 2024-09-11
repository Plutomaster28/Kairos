import re

def tokenize(code):
    tokens = []
    code = code.strip()

    # Regex patterns for tokens
    patterns = {
        'NUMBER': r'\d+',
        'ID': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'STRING': r'"[^"]*"',  # Match strings enclosed in double quotes
        'ASSIGN': r'=',
        'LPAREN': r'\(',
        'RPAREN': r'\)',
        'EOF': r'$',
        'WHITESPACE': r'\s+'
    }

    while code:
        matched = False
        for token_type, pattern in patterns.items():
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, match.group(0)))
                code = code[match.end():]
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Unexpected character: {code[0]}")
    
    return tokens
