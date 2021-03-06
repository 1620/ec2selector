#!/usr/bin/env python
from distutils.core import setup
import re
import os

# From http://cburgmer.posterous.com/pip-requirementstxt-and-setuppy
# If somebody wants to install the package via "pip install pdfserver" 
# all dependencies should be fulfilled during the install in setup.py. 
# But as the software is to be deployed on a server many users will probably 
# download and extract the source package and then created a virtualenv around 
# it using "pip install -r requirements.txt".
# As I found no simple solution to answer my needs, I extended setup.py to 
# parse the dependencies given in a requirements.txt file. The file is parsed 
# twice, first to extract all dependency names and then again for all URLs for
# packages not found on PyPI. What it doesn't do so far is parse the versioning
# information.
def parse_requirements(file_name):
	requirements = []
	for line in open(file_name, 'r').read().split('\n'):
		if re.match(r'(\s*#)|(\s*$)', line):
			continue
		if re.match(r'\s*-e\s+', line):
			requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
		elif re.match(r'\s*-f\s+', line):
			pass
		else:
			requirements.append(line)
	return requirements

def parse_dependency_links(file_name):
	dependency_links = []
	for line in open(file_name, 'r').read().split('\n'):
		if re.match(r'\s*-[ef]\s+', line):
			dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))
	return dependency_links

def get_packages():
    # setuptools can't do the job :(
    packages = []
    for root, dirnames, filenames in os.walk('ec2selector'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))
    return packages

setup(
    name = "ec2selector",
    version = "1.0.0",
    # requires => not used, see parse_requirements above
    install_requires = parse_requirements('requirements.txt'),
	dependency_links = parse_dependency_links('requirements.txt'),
    packages = get_packages(),
    description = "Interactive prompt to select an AMI " +
        "(Amazon Machine Image) from Amazon EC2",
    long_description = open('README.md').read(),
    author = 'RED Interactive Agency',
    author_email = 'geeks@ff0000.com',
    url = "https://github.com/ff0000/ec2selector",
    download_url = "https://github.com/ff0000/ec2selector",
    license = 'MIT license',
    keywords = ["amazon", "ec2", "ami", "cloud", "boto", "red"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",        
        "Natural Language :: English",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
        ],
)

# To create the package: python setup.py register sdist upload
