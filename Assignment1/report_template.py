# F401 'os' imported but unused
import os


from FFF import Request, Form


def some_function(a,b):
    # E226 missing whitespace around arithmetic operator
    result=a+b
    # E231 missing whitespace after ','
    print("The result is:",result)
    return result
