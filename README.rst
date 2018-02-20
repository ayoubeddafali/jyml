JYML Tool
========

CLI for generating and building jenkins jobs to and from yaml files.

**Right now, it works just with python 2.**

Preparing for Development
--------------------------

1. Ensure ``pip``, and ``pipenv`` are installed.
2. Clone the repo: ``https://github.com/ayoubensalem/jyml``
3. Fetch development dependencies : ``make install``


Usage
------


To generate a .yml file :

::

    $ jyml --generate config.xml job_name

A folder named `output` will be created, and there you'll find your yaml file.

To create a jenkins job from a .yml file :

::

    $ jyml --create jenkins_credentials.ini update job.yml


The Jenkins credentials is a file containing the url, username, password of your jenkins server :


..  image:: images/jenkins_creds.png


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make




Build
-------------

Build a wheel

::

    $ python setup.py bdist_wheel




















