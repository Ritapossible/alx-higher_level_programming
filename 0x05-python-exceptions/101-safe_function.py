#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as exp:
        print("Exception: {}".format(exp), file=sys.stderr)
        return None
