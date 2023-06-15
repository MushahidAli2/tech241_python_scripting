import os
import subprocess
# stores the file path to the current file
script_dir = os.path.dirname(__file__)
# stores the filepath to the scrip you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")

# calls the shell file and run it
subprocess.call(['sh', script_absolute_path])