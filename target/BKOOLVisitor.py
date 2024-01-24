# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declaration.
    def visitDeclaration(self, ctx:BKOOLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:BKOOLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var.
    def visitVar(self, ctx:BKOOLParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:BKOOLParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bodyfunc.
    def visitBodyfunc(self, ctx:BKOOLParser.BodyfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typefunc.
    def visitTypefunc(self, ctx:BKOOLParser.TypefuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign.
    def visitAssign(self, ctx:BKOOLParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#callf.
    def visitCallf(self, ctx:BKOOLParser.CallfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#re.
    def visitRe(self, ctx:BKOOLParser.ReContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typexpr.
    def visitTypexpr(self, ctx:BKOOLParser.TypexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcsmall.
    def visitFuncsmall(self, ctx:BKOOLParser.FuncsmallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#number.
    def visitNumber(self, ctx:BKOOLParser.NumberContext):
        return self.visitChildren(ctx)



del BKOOLParser