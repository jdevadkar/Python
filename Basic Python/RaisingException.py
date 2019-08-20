try:
    # raise Exception
    raise NameError("Hi there")
except NameError:
    print("An Exception")
    raise
