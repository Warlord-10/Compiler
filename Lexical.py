##########################
# TOKENS
##########################
# Token Types: constant, keyword, identifier, operator, punctuation
keywords =["class", "return", "for", "if", "else", "while", "int", "string", "bool", "void", "main"]
operators =["+", "-", "*", "/", "="]
punctuations =["(", ")", "{", "}", ",", ":", ";", "."]



class Lexer:
    def __init__(self):
        self.row = 1
        self.TOKENS = []
        self.error_code = ""
    
    def tokenizer(self,file_name):
        line = file_name
        self.word = ""
        self.curr_line = ""
        self.position = 0


        for letter in line:
            if self.error_code>"":
                self.next_word()
                if letter == "\n":
                    #self.error()
                    return self.lex_tokens() 
                else:
                    self.curr_line += letter
            else: 
                if self.curr_line == "    " and self.curr_line[0].isspace:
                    self.curr_line =""
                    self.position = 0
                if letter == "\n":
                    self.row += 1
                    self.curr_line = ""
                    self.position = 0
                else:
                    self.curr_line += letter
                    self.position += 1

                if letter.isspace():
                    if self.word>"":
                        self.TOKENS.append(self.analysis(self.word))
                        #self.word=""
                        self.next_word()
                elif letter in punctuations or letter in operators:
                    if self.word>"":
                        self.TOKENS.append(self.analysis(self.word))
                        #self.word=""
                        self.next_word()
                    self.TOKENS.append(self.analysis(letter))
                elif letter.isdigit() or letter.isalpha() or letter == '"':
                    self.word+=letter
                else:
                    self.error_code = f"[ERROR]: Unexpected symbol '{letter}'"

        if self.word>"":
            self.TOKENS.append(self.analysis(self.word))
        return self.lex_tokens()

    def analysis(self,test):
        temp_length = len(test)

        # Test for strings and characters
        if test[0] == '"' or test[temp_length-1] =='"':
            if test[0] == test[temp_length-1]:
                return {"type": "CONSTANT", "value": test}
            else:
                if test[0] !='"':
                    self.error_code =f"[ERROR]: Syntax Error ' {test[temp_length-1]} ' "
                elif test[temp_length-1] !='"':
                    self.error_code=f"[ERROR]: Syntax Error ' {test[0]} ' "


        # Test for alphabets and digits
        elif test.isalnum():
            if test in keywords:
                return {"type": "KEYWORD", "value": test}
            elif test.isdigit():
                return {"type": "CONSTANT", "value": test}
            if test[0].isalpha():
                return {"type": "IDENTIFIER", "value": test}
            else:
                self.error_code = f"[ERROR]: Incorrect indentifier declaration '{test}'"
        
        # Test for punctuations
        else:
            if test in operators:
                return {"type": "OPERATOR", "value": test}
            elif test in punctuations:
                return {"type": "PUNCTUATION", "value": test}
            else:
                self.error_code = f"[ERROR]: Unexpected symbol '{test}'"

    def lex_tokens(self):
        if self.error_code=="":
            #print(self.TOKENS, "\n")
            #print("[PARSER]: File read",self.row,"rows.")
            return self.TOKENS
        else:
            return self.error()

    def next_word(self):
        self.prev_word = self.word
        self.word =""

    def error(self):
        print(self.error_code)
        print(self.curr_line)
        print(" "*(self.position-1-len(self.prev_word)),end="")
        print("^")

if __name__ == "__main__":
    lex = Lexer()
    dump_file = open("test.txt","r")
    dump_file = dump_file.read()
    print(lex.tokenizer(dump_file))

