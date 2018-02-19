import subprocess
import sys
import cli

def generate(config_file, job_name):
    try:
        return subprocess.Popen(['jjwrecker', '-v' , '-f', config_file, '-n', job_name, '-o', '/tmp/output'], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: jjwrecker command  not found.")
        sys.exit(2)

def create(ini_file, action, yml_file):
    try:
        return subprocess.Popen(['jenkins-jobs', '--conf', ini_file, action, yml_file ], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: jenkins-jobs commnad not found.")
        sys.exit(2)


if __name__ == "__main__":
    parser = cli.create_parser()
    args = parser.parse_args()
    print(sys.argv)
    if sys.argv[1] in ("--generate", "-g"):
        generate(args.config_file, args.job_name)
    elif sys.argv[1] in ("--create", "-c"):
        create(args.jenkins_credentials, args.action, args.yml_file)
    else:
        print("Argument not found")
