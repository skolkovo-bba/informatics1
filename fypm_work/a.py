import sys 
 
class ExtendedList(list):
    
    def get_reversed(self):
        return self[::-1]
    
    reversed = property(get_reversed)
    R = reversed

    def get_first(self):
        return self[0]
    
    def sef_first(self, var):
        self[0] = var
    
    first = property(get_first, sef_first)
    F = first

    def get_last(self):
        return self[-1]
    
    def set_last(self, var):
        self[-1] = var
    
    last = property(get_last, set_last)
    L = last

    def get_size(self):
        return len(self)
    
    def set_size(self, var):
        print(self, var)
        if var > len(self):
            self += [None] * (var - len(self))
        elif var < len(self):
            del self[var:]
    
    size = property(get_size, set_size)
    S = size
    


exec(sys.stdin.read())
