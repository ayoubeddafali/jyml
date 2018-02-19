import argparse
import sys 

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # xml_pattern = re.compile(r'*.xml$')
        config_file, job_name = values
        if not config_file.endswith(".xml"):
            parser.error("File must end with .xml extension.")
        namespace.config_file = config_file.lower()
        namespace.job_name = job_name

class CreateAction(argparse.Action):
    known_actions=["get-plugins-info","delete-all","test","update","delete"]
    def __call__(self, parser, namespace, values, option_string=None):
        jenkins_credentials, action, yml_file = values
        # pattern = "*.yml$"
        # yaml_pattern = re.compile(r'*.yml$')
        if not yml_file.endswith(".yml"):
             parser.error("File must end with .yml extension.")
        namespace.jenkins_credentials = jenkins_credentials
        namespace.action = action.lower()
        namespace.yml_file = yml_file

def create_parser():
    parser = argparse.ArgumentParser(
                description="""
                Generate or Build Jenkins Jobs to/from YAML files.
                """
            )
    parser.add_argument('-g', '--generate', dest="ayoub", help='Job Config xml file & Job name',
            nargs=2,
            metavar=("CONFIG_FILE", "JOB_NAME"),
            action=DriverAction,
            required=False)
    parser.add_argument('-c', '--create', help="Jenkins credentials, action & yaml file.",
            nargs=3,
            metavar=("JENKINS_CREDENTIALS", "ACTION", "YML_FILE"),
            action=CreateAction,
            required=False)
    return parser


if __name__== "__main__":
    import jyml
    parser = create_parser()
    args = parser.parse_args()
    # print(sys.argv)
    if sys.argv[1] in ("--generate", "-g"):
        jyml.generate(args.config_file, args.job_name)
    elif sys.argv[1] in ("--create", "-c"):
        jyml.create(args.jenkins_credentials, args.action, args.yml_file)
    else:
        print("Argument not found")


def main():
    import jyml
    parser = create_parser()
    args = parser.parse_args()
    # print(sys.argv)
    if sys.argv[1] in ("--generate", "-g"):
        jyml.generate(args.config_file, args.job_name)
    elif sys.argv[1] in ("--create", "-c"):
        jyml.create(args.jenkins_credentials, args.action, args.yml_file)
    else:
        print("Argument not found")
