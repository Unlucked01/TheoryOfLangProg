# Generated from /Users/unlucked/PycharmProjects/gram/g.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#program.
    def visitProgram(self, ctx:gParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#computationDescription.
    def visitComputationDescription(self, ctx:gParser.ComputationDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:gParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#variableList.
    def visitVariableList(self, ctx:gParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operatorsList.
    def visitOperatorsList(self, ctx:gParser.OperatorsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assignment.
    def visitAssignment(self, ctx:gParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#expression.
    def visitExpression(self, ctx:gParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#subexpression.
    def visitSubexpression(self, ctx:gParser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#unaryOperator.
    def visitUnaryOperator(self, ctx:gParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#binaryOperator.
    def visitBinaryOperator(self, ctx:gParser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operand.
    def visitOperand(self, ctx:gParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#identifier.
    def visitIdentifier(self, ctx:gParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#constant.
    def visitConstant(self, ctx:gParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#read.
    def visitRead(self, ctx:gParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#loop.
    def visitLoop(self, ctx:gParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#write.
    def visitWrite(self, ctx:gParser.WriteContext):
        return self.visitChildren(ctx)



del gParser