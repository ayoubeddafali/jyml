from setuptools import setup, find_packages


with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="jyml-tool",
    version="0.1.0",
    description="Jenkins YAML tool to convert jobs and create them.",
    long_description=readme,
    author='Ayoub ED-DAFALI',
    author_email='ayoubensalem@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    setup_requires=["jenkins-job-builder", "jenkins-job-wrecker"],
    install_requires=[],
    entry_points={
            'console_scripts': [
                'jyml=jyml.cli:main'],
        }
)

