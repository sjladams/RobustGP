import jug

def TaskGenerator(debug):
    if debug:
        def decorator(func):
            return func
        return decorator
    else:
        return jug.TaskGenerator

def bvalue(debug, out):
    if debug:
        return out
    else:
        return jug.bvalue(out)