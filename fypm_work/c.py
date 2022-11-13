import sys
import traceback

def force_load(s):
    f = open(s + ".py", "r")
    lines = f.read().split("\n")
    lines = list(map(lambda x: x + "\n", lines))
    f.close()


    ldict = {}
    while True:
        try:
            exec(''.join(lines), globals(), ldict)
        except:
            ln = 0
            for frame in traceback.extract_tb(sys.exc_info()[2]):
                fname, lineno, fn, text = frame
                ln = lineno
            
            lines[ln - 1] = "#" + lines[ln - 1]
        else:
            break
    
    return ldict
