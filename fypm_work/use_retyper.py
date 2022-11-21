import d as managers
  
def foo():  
    i = 1 / 0  
  
  
with managers.retyper(ZeroDivisionError, KeyError):  
    foo()  
