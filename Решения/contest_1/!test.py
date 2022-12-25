import subprocess
import os
from pathlib import Path


N = 100



path = ["igors_work", "ejudge_1"]

gen = path + ["gen.py"]
script = path + ["c.py"]
check =  path + ["c_good.py"]

gen = os.path.abspath(os.sep.join(gen))
script = os.path.abspath(os.sep.join(script))
check = os.path.abspath(os.sep.join(check))

gen_txt = os.path.abspath(os.sep.join(path + ['gen.txt']))
script_txt = os.path.abspath(os.sep.join(path + ['script.txt']))
check_txt = os.path.abspath(os.sep.join(path + ['script.txt']))

with open(gen_txt, 'wb', 0) as gen_file:
    subprocess.call(['python3', gen], stdout=gen_file)

with open(script_txt, 'wb', 0) as out:
    subprocess.call(['python3', script, f"-i {gen_file}"], stdout=out)
