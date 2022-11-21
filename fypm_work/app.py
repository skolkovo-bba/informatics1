class VeryImportantClass:
    k = 1
    b = [1, 2, 3]

    def __init__(self):
        self.k = 1
    
    def defer(self):
        self.k = 2
        return self.k
    
    

def decorator(f):
    def ret_f(*args, **kwargs):
        print(f"call {args}, {kwargs}")
        ret = f(*args, **kwargs)
        print(f"return {ret}")

        return ret_f

    return ret_f
