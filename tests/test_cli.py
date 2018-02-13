import pytest
from jyml import cli


@pytest.fixture()
def parser():
    return cli.create_parser()


def test_parser_with_config_file(parser):
    """
    The parser will exit if it receivers a config_file without a job_name
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--generate-yaml', 'config.xml'])


def test_parser_with_config_file_and_jobname(parser):
    """
    The parser will not exit if it receives a valid config_file and a job_name
    """
    args = parser.parse_args(['--generate-yaml', 'config.xml', 'name'])
    assert args.config_file == 'config.xml'
    assert args.job_name == 'name'


def test_parser_with_invalied_config_file(parser):
    """
       The parser will throw an error if config file is not valid
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--generate-yaml', 'config.json', 'job_name'])



def test_parser_with_jenkins_credentials(parser):
    """
    The parser will exit if it receivers a less than 3 args
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--create-job', 'config.ini'])


def test_parser_with_jenkins_credentials(parser):
    """
    The parser will exit if it receivers less than 3 args
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--create-job', 'config.ini', 'update'])

def test_parser_with_credentials_and_action_and_yml_file(parser):
    """
    The parser will not exit if it receives a valid yml file, action and jenkins credentials file
    """
    args = parser.parse_args(['--create-job', 'config.ini', 'update', 'job.yml'])
    assert args.yml_file == 'job.yml'
    assert args.action == 'update'
    assert args.jenkins_credentials == 'config.ini'


def test_parser_with_invalied_yaml_file(parser):
    """
       The parser will throw an error if yaml file is not valid
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--create-job', 'config.ini', 'update', 'job.json'])
