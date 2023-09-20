def check(f):
    def helper(x):

        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not negative integer")

    return helper

  