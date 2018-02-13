import subprocess
import sys

def generate(config_file, job_name):
    try:
        return subprocess.Popen(['jjwrecker', '-f', config_file, '-n', job_name], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: jjwrecker command  not found.")
        sys.exit(2)
def create(ini_file, action, yml_file):
    try:
        return subprocess.Popen(['jenkins-jobs', '--conf', ini_file, action, yml_file ], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: jenkins-jobs commnad not found.")
        sys.exit(2)
