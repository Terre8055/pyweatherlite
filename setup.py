from setuptools import setup, find_packages

setup(
    name='pycloudlib_Terre8055',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pycloudlib = pycloudlib_Terre8055.index:main',
        ],
    },
    # Other metadata like author, description, etc.
    author='Michael Appiah Dankwah',
    author_email='michaelappiah2018@icloud.com',
    description='A lightweight python library to extract weather data',
    url='https://github.com/Terre8055/pycloudlib',
    license='MIT',
)
