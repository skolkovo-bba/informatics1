from app import VeryImportantClass, decorator 
from collections.abc import Callable

def hack(cl):
    cl_copy = cl
    for name in cl.__dict__:
        if name.startswith("_"):
            continue

        if isinstance(cl.__dict__[name], Callable):
            setattr(cl_copy, name, decorator(cl.__dict__[name]))

        elif isinstance(cl.__dict__[name], int) or isinstance(cl.__dict__[name], float):
            def getter(self):
                return self.__dict__[getter.name] * 2
            getter.name = name

            def setter(self, var):
                self.__dict__[setter.name] = var
            setter.name = name
            
            setattr(cl_copy, name, property(getter, setter))
        else:
            try:
                len(cl.__dict__[name])
            except:
                pass
            else:
                #print(f"atr {name}")
                def getter(self):
                    #print(f"get {getter.name}", str(type(self.__dict__[getter.name])))
                    s = str(type(self.__dict__[getter.name]))
                    s = s[s.find('\'') + 1:s.rfind('\'')]
                    return eval(s + "()")
                getter.name = name

                def setter(self, var):
                    self.__dict__[setter.name] = var
                setter.name = name

                setattr(cl_copy, name, property(getter, setter))

    return cl_copy

HackedClass = hack(VeryImportantClass)

#h = HackedClass()
#h.defer()
#h.b = [1, 2, 3]
#print(h.b)