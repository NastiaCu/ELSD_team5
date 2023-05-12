# Generated from Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#query_invocation.
    def enterQuery_invocation(self, ctx:ExprParser.Query_invocationContext):
        pass

    # Exit a parse tree produced by ExprParser#query_invocation.
    def exitQuery_invocation(self, ctx:ExprParser.Query_invocationContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#variable.
    def enterVariable(self, ctx:ExprParser.VariableContext):
        pass

    # Exit a parse tree produced by ExprParser#variable.
    def exitVariable(self, ctx:ExprParser.VariableContext):
        pass


    # Enter a parse tree produced by ExprParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ExprParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#method_invocation.
    def enterMethod_invocation(self, ctx:ExprParser.Method_invocationContext):
        pass

    # Exit a parse tree produced by ExprParser#method_invocation.
    def exitMethod_invocation(self, ctx:ExprParser.Method_invocationContext):
        pass


    # Enter a parse tree produced by ExprParser#method_name.
    def enterMethod_name(self, ctx:ExprParser.Method_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#method_name.
    def exitMethod_name(self, ctx:ExprParser.Method_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ExprParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ExprParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#method_declaration.
    def enterMethod_declaration(self, ctx:ExprParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by ExprParser#method_declaration.
    def exitMethod_declaration(self, ctx:ExprParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by ExprParser#comments.
    def enterComments(self, ctx:ExprParser.CommentsContext):
        pass

    # Exit a parse tree produced by ExprParser#comments.
    def exitComments(self, ctx:ExprParser.CommentsContext):
        pass



del ExprParser