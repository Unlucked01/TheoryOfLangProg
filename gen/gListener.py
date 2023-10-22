# Generated from /Users/unlucked/PycharmProjects/gram/g.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete listener for a parse tree produced by gParser.
class gListener(ParseTreeListener):

    # Enter a parse tree produced by gParser#program.
    def enterProgram(self, ctx:gParser.ProgramContext):
        pass

    # Exit a parse tree produced by gParser#program.
    def exitProgram(self, ctx:gParser.ProgramContext):
        pass


    # Enter a parse tree produced by gParser#computationDescription.
    def enterComputationDescription(self, ctx:gParser.ComputationDescriptionContext):
        pass

    # Exit a parse tree produced by gParser#computationDescription.
    def exitComputationDescription(self, ctx:gParser.ComputationDescriptionContext):
        pass


    # Enter a parse tree produced by gParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:gParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by gParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:gParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by gParser#variableList.
    def enterVariableList(self, ctx:gParser.VariableListContext):
        pass

    # Exit a parse tree produced by gParser#variableList.
    def exitVariableList(self, ctx:gParser.VariableListContext):
        pass


    # Enter a parse tree produced by gParser#operatorsList.
    def enterOperatorsList(self, ctx:gParser.OperatorsListContext):
        pass

    # Exit a parse tree produced by gParser#operatorsList.
    def exitOperatorsList(self, ctx:gParser.OperatorsListContext):
        pass


    # Enter a parse tree produced by gParser#assignment.
    def enterAssignment(self, ctx:gParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gParser#assignment.
    def exitAssignment(self, ctx:gParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gParser#expression.
    def enterExpression(self, ctx:gParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gParser#expression.
    def exitExpression(self, ctx:gParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gParser#subexpression.
    def enterSubexpression(self, ctx:gParser.SubexpressionContext):
        pass

    # Exit a parse tree produced by gParser#subexpression.
    def exitSubexpression(self, ctx:gParser.SubexpressionContext):
        pass


    # Enter a parse tree produced by gParser#unaryOperator.
    def enterUnaryOperator(self, ctx:gParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by gParser#unaryOperator.
    def exitUnaryOperator(self, ctx:gParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by gParser#binaryOperator.
    def enterBinaryOperator(self, ctx:gParser.BinaryOperatorContext):
        pass

    # Exit a parse tree produced by gParser#binaryOperator.
    def exitBinaryOperator(self, ctx:gParser.BinaryOperatorContext):
        pass


    # Enter a parse tree produced by gParser#operand.
    def enterOperand(self, ctx:gParser.OperandContext):
        pass

    # Exit a parse tree produced by gParser#operand.
    def exitOperand(self, ctx:gParser.OperandContext):
        pass


    # Enter a parse tree produced by gParser#identifier.
    def enterIdentifier(self, ctx:gParser.IdentifierContext):
        pass

    # Exit a parse tree produced by gParser#identifier.
    def exitIdentifier(self, ctx:gParser.IdentifierContext):
        pass


    # Enter a parse tree produced by gParser#constant.
    def enterConstant(self, ctx:gParser.ConstantContext):
        pass

    # Exit a parse tree produced by gParser#constant.
    def exitConstant(self, ctx:gParser.ConstantContext):
        pass


    # Enter a parse tree produced by gParser#read.
    def enterRead(self, ctx:gParser.ReadContext):
        pass

    # Exit a parse tree produced by gParser#read.
    def exitRead(self, ctx:gParser.ReadContext):
        pass


    # Enter a parse tree produced by gParser#loop.
    def enterLoop(self, ctx:gParser.LoopContext):
        pass

    # Exit a parse tree produced by gParser#loop.
    def exitLoop(self, ctx:gParser.LoopContext):
        pass


    # Enter a parse tree produced by gParser#write.
    def enterWrite(self, ctx:gParser.WriteContext):
        pass

    # Exit a parse tree produced by gParser#write.
    def exitWrite(self, ctx:gParser.WriteContext):
        pass



del gParser