# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xchk_ap_db_intro']

package_data = \
{'': ['*'],
 'xchk_ap_db_intro': ['static/xchk_ap_db_intro/images/*', 'templates/xchk_ap_db_intro/*']}

install_requires = \
[]

setup_kwargs = {
    'name': 'xchk_ap_db_intro',
    'version': '0.0.1',
    'description': 'Course material related to APDBIntro for the xchk teaching framework',
    'long_description': None,
    'author': 'Vincent Nys',
    'author_email': 'vincentnys@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
