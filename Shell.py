import Lexical
import Parser

while True:
    text = input("Input=> ")
    print(text)
    lex = Lexical.Lexer()
    tok = lex.tokenizer(text)
    par = Parser.Parser(tok)
    print(par.parse())
