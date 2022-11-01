
datatypes =["int", "string", "bool", "void"]
keywords =["class", "return", "for", "if", "else", "while"]
operators =["+", "-", "*", "/", "="]
punctuations =["(", ")", "{", "}", ",", ":", ";", "''"]

class NumberNode:
    def __init__(self,tok):
        self.tok = tok
    def __repr__(self):
        return f"{self.tok['value']}"
        
class BinOpNode:
    def __init__(self,left_node,op_tok,right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
    def __repr__(self):
        return f"({self.left_node},{self.op_tok},{self.right_node})" 
    

class Parser:
    def __init__(self,tokens):
        self.total_tokens = tokens
        self.tok_index = -1
        self.advance()
    
    def parse(self):
        res = self.expr()
        return res

    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.total_tokens):
            self.current_token = self.total_tokens[self.tok_index]
        return self.current_token 
    
    def factor(self):
        #if self.current_token["type"] == "CONSTANT":
        temp_tok = self.current_token
        if temp_tok["value"].isdigit():
            self.advance()
            return NumberNode(temp_tok)
    
    def term(self):
        left = self.factor()
        while self.current_token["value"] in "*/":
            op_tok = self.current_token["value"]
            self.advance()
            right = self.factor()
            left = BinOpNode(left,op_tok,right)
        return left

    def expr(self):
        left = self.term()
        while self.current_token["value"] in "+-":
            op_tok = self.current_token["value"]
            self.advance()
            right = self.term()
            left = BinOpNode(left,op_tok,right)
        return left

if __name__ == "__main__":
    temp_tokens = [
        {'type': 'CONSTANT', 'value': '1'},
        {'type': 'OPERATOR', 'value': '+'}, 
        {'type': 'CONSTANT', 'value': '5'}, 
        {'type': 'OPERATOR', 'value': '*'}, 
        {'type': 'CONSTANT', 'value': '8'}
            ]

    par = Parser(temp_tokens)
    print(par.parse())


