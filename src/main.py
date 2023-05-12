from antlr4 import *
from resources.ExprLexer import ExprLexer
from resources.ExprParser import ExprParser
from resources.ExprListener import ExprListener
from playsound import playsound


# Create a stream of characters from the input string
input_stream = FileStream('input.txt')

# Create a lexer that will identify tokens in the input stream
lexer = ExprLexer(input_stream)

# Create a stream of tokens from the lexer
token_stream = CommonTokenStream(lexer)

# Create a parser that will generate a parse tree from the token stream
parser = ExprParser(token_stream)

# Parse the input string and generate a parse tree
tree = parser.prog()



loaded_sound = ""
current_sound = ""
fx = ()
# Create a listener to traverse the parse tree
class MyListener(ExprListener):
    

    def enterMethod_invocation(self, ctx:ExprParser.Method_invocationContext):
        method_name = ctx.method_name().getText()
        rhs = ctx.getText().split("(")
        lhs = rhs[1].split(")")
        method_atributes = lhs[0]
        global loaded_sound
        global current_sound
        if method_name == "load":
            loaded_sound = method_atributes
            current_sound = loaded_sound
        if method_name == "play":
            playsound(current_sound)
        pass



listener = MyListener()

walker = ParseTreeWalker()
walker.walk(listener, tree)
