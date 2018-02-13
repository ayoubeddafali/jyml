import argparse
import re

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        xml_pattern = re.compile(r'[a-zA-Z]{1,}.xml$')
        config_file, job_name = values
        if not xml_pattern.match(config_file):
            parser.error("File must end with .xml extension.")
        namespace.config_file = config_file.lower()
        namespace.job_name = job_name

class CreateAction(argparse.Action):
    known_actions=["get-plugins-info","delete-all","test","update","delete"]
    def __call__(self, parser, namespace, values, option_string=None):
        jenkins_credentials, action, yml_file = values
        yaml_pattern = re.compile(r'[a-zA-Z]{1,}.yml$')
        if not yaml_pattern.match(yml_file):
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
    parser.add_argument('--generate-yaml', help='Job Config xml file & Job name',
            nargs=2,
            metavar=("CONFIG_FILE", "JOB_NAME"),
            action=DriverAction,
            required=False)
    parser.add_argument('--create-job', help="Jenkins credentials, action & yaml file.",
            nargs=3,
            metavar=("JENKINS_CREDENTIALS", "ACTION", "YML_FILE"),
            action=CreateAction,
            required=False)
    return parser


if __name__== "__main__":
    parser = create_parser()
    parser.parse_args()


def main():
    from jyml import jyml
    args = create_parser().parse_args()
    if args.generate_yaml:
        jyml.generate(args.config_file, args.job_name)
    elif args.create_job:
        jyml.create(args.jenkins_credentials, args.action, args.yml_file)
    else:
        print("Argument not found")

