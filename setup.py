#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import (
    setup,
    find_packages,
    )


def find_package_data(target, package_root):
    return [
        os.path.relpath(os.path.join(root, filename), package_root)
        for root, dirs, files in os.walk(target)
        for filename in files
        ]

src = 'src'
install_requires = []
test_require = []
packages = find_packages(src)
package_dir = {'': src}
package_data = {}


setup(
    name='scaff',
    version='0.1.0',
    url='https://github.com/TakesxiSximada/wdc',
    download_url='https://github.com/TakesxiSximada/wdc/master.zip',
    license='See http://www.python.org/2.7/license.html',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description="IBM Watson Developer Cloud API",
    long_description="IBM Watson Developer Cloud API",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        ],
    platforms='any',
    packages=packages,
    package_dir=package_dir,
    namespace_packages=[
        ],
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    test_require=test_require,
    entry_points='''
    [console_scripts]
    '''
    )
