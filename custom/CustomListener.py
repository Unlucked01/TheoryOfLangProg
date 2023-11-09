from gen.gListener import gListener
from gen.gParser import gParser


class CustomListener(gListener):
    def __init__(self):
        self.variables = {}

    def enterVariableDeclaration(self, ctx):
        for identifierContext in ctx.variableList().identifier():
            variable = identifierContext.getText()
            if len(variable) > 12:
                raise Exception("Variable name is more than 12 symbols!")
            else:
                self.variables[variable] = None

    def enterComputationDescription(self, ctx):

        self.enterOperatorsList(ctx.operatorsList())

    def enterAssignment(self, ctx):
        # print("enter assignment")
        variable = self.enterIdentifier(ctx.identifier())
        expression = self.enterExpression(ctx.expression())
        self.variables[variable] = expression
        # print(f"{variable} = {self.variables[variable]}")

    def enterLoop(self, ctx):
        while self.enterExpression(ctx.expression()):
            self.enterOperatorsList(ctx.operatorsList())

    def enterOperatorsList(self, ctx):
        pass
        for child in ctx.children:
            if isinstance(child, gParser.AssignmentContext):
                self.enterAssignment(child)
            if isinstance(child, gParser.LoopContext):
                self.enterLoop(child)
            elif isinstance(child, gParser.ReadContext):
                self.enterRead(child)
            # elif isinstance(child, gParser.WriteContext):
            #     # print("write from operList")
            #     self.enterWrite(child)

    def enterRead(self, ctx):
        for identifierContext in ctx.variableList().identifier():
            variable = identifierContext.getText()
            self.variables[variable] = input()

    def enterWrite(self, ctx):
        for identifierContext in ctx.variableList().identifier():
            variable = identifierContext.getText()
            print(f"{identifierContext.getText()} = {self.variables[variable]}")

    def enterExpression(self, ctx):
        # An expression can be a unary operator followed by a subexpression
        # or just a subexpression.
        # You would need to implement logic to handle the unary operator.
        if ctx.unaryOperator() is not None:
            value = self.enterSubexpression(ctx.subexpression())
            value = not value
            pass
        else:
            value = self.enterSubexpression(ctx.subexpression())
        return value

    def enterSubexpression(self, ctx):
        # A subexpression can be an expression enclosed in parentheses,
        # an operand, or two subexpressions separated by a binary operator.
        # You would need to implement logic to handle the binary operator.
        if ctx.expression() is not None:
            value = self.enterExpression(ctx.expression())
        elif ctx.operand() is not None:
            value = self.enterOperand(ctx.operand())
        else:
            left = self.enterSubexpression(ctx.subexpression(0))
            operator = self.enterBinaryOperator(ctx.binaryOperator())
            right = self.enterSubexpression(ctx.subexpression(1))
            match operator:
                case ".AND.":
                    value = left and right
                case ".OR.":
                    value = left or right
                case ".IMP.":
                    value = not left or right
                case _:
                    raise Exception("Unexpected operand!")
        return value

    def enterBinaryOperator(self, ctx):
        return ctx.getText()

    def enterOperand(self, ctx):
        # An operand can be an identifier or a constant.
        # You would need to implement logic to retrieve the value of the identifier.
        if ctx.identifier() is not None:
            identifier = self.enterIdentifier(ctx.identifier())
            value = self.variables[identifier]
        else:
            value = self.enterConstant(ctx.constant())
        return value

    def enterIdentifier(self, ctx):
        # An identifier is just a variable name.
        return ctx.getText()

    def enterConstant(self, ctx):
        return int(ctx.getText())
