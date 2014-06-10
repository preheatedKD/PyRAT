# Layer __init__

from TSX import *

def list():
    import sys
    from inspect import getmembers, isclass
    current_module = sys.modules[__name__]
    modules = getmembers(current_module, isclass)
    print 
    print "Content of module "+__name__+":"
    print 
    for mod in modules:
        if 'PyRat' in mod[1].__module__:
            doc = str(mod[1].__doc__)
            if doc != 'None':
                doc = doc.split('\n')[1]
            print mod[0].ljust(20)+doc