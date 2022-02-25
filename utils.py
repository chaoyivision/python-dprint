import inspect
import tokenize
import token
import io

def dprint(var_value, color=True):

    #debug_print
    BOLD = '\033[1m'
    END = '\033[0m'
    START = END + BOLD    
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    COLOR = '\033[93m'
    if color:
        START += COLOR
        END += COLOR
    MIDDLE1 = END+UNDERLINE+ITALIC
    MIDDLE2 = END

    
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)

    caller_filename = calframe[1][1].split('/')[-1]
    caller_funcname = calframe[1][3]
    caller_lineno = calframe[1][2]

    def _format_expression(code_context):
        # borrowed from https://github.com/pradyunsg/dprint/blob/de8ed1ad75412d710d31f71e5b477826a92a0005/dprint/_impl.py#L106 to derive the var_name
        if not code_context:
            return ""

        line = code_context[0]

        # Tokenize the line
        token_list = tokenize.tokenize(io.BytesIO(line.encode('utf-8')).readline)

        # Determine the start and end of expression
        start = None
        end = None
        level = 0  # because nesting
        for tok in token_list:
            # Looking for the start of string.
            if start is None:
                if tok.type == token.NAME and tok.string == "dprint":
                    start = tok.start[1]  # we get the proper value later.
                continue
            if end is None:
                if tok.type != token.OP:
                    continue

                if tok.string == "(":
                    if level == 0:  # opening parens
                        start = tok.end[1]
                    level += 1
                elif tok.string == ")":
                    level -= 1
                    if level == 0:  # closing parens
                        end = tok.start[1]
                        # This is fine since we don't need more information
                        break
        return line[start:end]

    var_name = _format_expression(inspect.stack()[1].code_context)
    print('{}[{}-{}()-L{}] {}{}{} -> {}{}'.format(START, caller_filename, caller_funcname, caller_lineno, MIDDLE1, var_name, MIDDLE2, var_value, END.replace(COLOR, '')))
    return var_value
