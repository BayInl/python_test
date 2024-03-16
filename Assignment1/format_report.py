# This py source file is used to show some formatted report of the flake8

# # E231 missing whitespace after ','
def format_func(a,b):
    # E226 missing whitespace around arithmetic operator
    result = a+b
    # E231 missing whitespace after ','
    print("The result is:",result)
    return result
# W292 no newline at end of file