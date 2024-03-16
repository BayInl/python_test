def risky_operation():
    raise Exception("This is a risky operation")


try:
    risky_operation()
except:
    pass
