from setuptools import setup, find_packages

setup(
    name='styled_print',
    version='0.1.0',  
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'termcolor',  
    ],
    author='Usmonov Shoxruxmirzo',
    author_email='usmonovshohruxmirzo@gmail.com',
    description='Pencil Art Generator from Images',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webbro-software/styled_print',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)