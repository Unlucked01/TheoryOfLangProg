class ErrorHandler():
    @staticmethod
    def syntaxError(recognizer, offendingSymbol, line, column, msg, e):
        exit(1)
