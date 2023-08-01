from setuptools import setup, find_packages

setup(
    name='pyweatherlite',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pyweatherlite = pyweatherlite.index:Scaffold',
        ],
    },
    # Other metadata like author, description, etc.
    author='Michael Appiah Dankwah',
    author_email='michaelappiah2018@icloud.com',
    description='A lightweight python library to extract weather data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Terre8055/pyweatherlite',
    license='MIT',
)
