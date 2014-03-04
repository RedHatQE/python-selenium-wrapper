from setuptools import setup, find_packages

setup(name='selenium_wrapper',
    version=0.1,
    description='Selenium driver wrapper and screenshots nosetests plugin',
    author='dparalen',
    license='GPLv3+',
    provides=['selenium_wrapper'],
    install_requires=['nose', 'selenium'],
    entry_points = {
        'nose.plugins.0.10': [
            'webui_screenshots = selenium_wrapper.nose.webui_screenshots:WebuiScreenshots'
            ]
        },
    classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Operating System :: POSIX',
            'Intended Audience :: Developers',
            'Development Status :: 4 - Beta'
    ],
    packages = find_packages(),
    )
