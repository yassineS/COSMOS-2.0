from distutils.core import setup
import os
import re

from setuptools import find_packages


setup_py_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(setup_py_path, 'cosmos/VERSION'), 'r') as fh:
    __version__ = fh.read().strip()


def find_all(path, reg_expr, inverse=False, remove_prefix=False):
    if not path.endswith('/'):
        path = path + '/'
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            match = re.search(reg_expr, filename) is not None
            if inverse:
                match = not match
            if match:
                out = os.path.join(root, filename)
                if remove_prefix:
                    out = out.replace(path, '')
                yield out


setup(
    name="cosmos-wfm",
    version=__version__,
    description="Workflow Management System",
    url="https://cosmos.hms.harvard.edu/",
    author="Erik Gafni",
    author_email="egafni@gmail.com",
    maintainer="Erik Gafni",
    maintainer_email="egafni@gmail.com",
    license="Non-commercial use only",
    install_requires=[
        "psutil",
        "flask",
        'blinker',
        'Flask-Admin',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'networkx',
        "ipython",
        "enum34"],
    packages=find_packages(),
    include_package_data=True,
    package_data={'cosmos': list(find_all('cosmos/', '.py|.pyc$', True, True))}
)


