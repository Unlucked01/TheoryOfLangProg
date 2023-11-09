from antlr4 import *
from gen.gLexer import gLexer
from gen.gParser import gParser
from custom.CustomListener import CustomListener
from custom.ErrorHandler import ErrorHandler


def main():
    # Create a lexer and a parser
    lexer = gLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = gParser(stream)

    parser.addErrorListener(ErrorHandler())

    # Parse the input
    tree = parser.program()

    # Create a custom listener
    listener = CustomListener()

    # Create a walker and walk the parse tree with the custom listener
    walker = ParseTreeWalker()
    try:
        print("\n\n" + '#' * 5 + "OUT" + '#' * 5)
        walker.walk(listener, tree)
        print('#' * 5 + "OUT" + '#' * 5)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()


