import pytest
import subprocess

from jyml import jyml

config_file="test.xml"
job_name="job_name"
jenkins_credentials="jenkins.ini"
action="update"
yml_file="job.yml"
def test_generate_call_jjwrecker(mocker):
    """
    Utilize jjwrecker
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert jyml.generate(config_file, job_name) == proc
    subprocess.Popen.assert_called_with(['jjwrecker','-v',  '-f', config_file,'-n', job_name, '-o', '/tmp/output'], stdout=subprocess.PIPE)

def test_generate_handles_oserror(mocker):
    """
    jyml.generate  returns an error if jjwrecker  isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("NO such file"))
    with pytest.raises(SystemExit):
        jyml.generate(config_file, job_name)

def test_create_call_jenkins_jobs(mocker):
    """
    Utilize jenkins-jobs
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert jyml.create(jenkins_credentials, action, yml_file) == proc
    subprocess.Popen.assert_called_with(['jenkins-jobs', '--conf', jenkins_credentials, action, yml_file], stdout=subprocess.PIPE)

def test_generate_handles_oserror(mocker):
    """
    jyml.generate  returns an error if jjwrecker  isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("NO such file"))
    with pytest.raises(SystemExit):
        jyml.create(jenkins_credentials, action, yml_file)

