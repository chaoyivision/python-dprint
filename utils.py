import inspect
def dprint(var_dict, color=True):

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

    for var_name, var_value in var_dict.items():
        print('{}[{}-{}()-L{}] {}{}{} = {}{}'.format(START, caller_filename, caller_funcname, caller_lineno, MIDDLE1, var_name, MIDDLE2, var_value, END.replace(COLOR, '')))

