from setuptools import setup, find_packages

setup(
    name='pycloudlib',            # Package name
    version='0.1.0',             # Package version
    packages=find_packages(),    # List of packages to include
    install_requires=[           # Dependencies required for your package
        'requests',
    ],
    entry_points={               # Entry point for your package (main module that users call)
        'console_scripts': [
            'pycloudlib = pycloudlib.index:main',
        ],
    },
    # Other metadata like author, description, etc.

    author='Michael Appiah Dankwah',          # Author name
    author_email='michaelappiah2018@icloud.com',  # Author email
    description='Lightweight package to extract weather data from openweather',
    url='https://github.com/Terre8055/pycloudlib',  # URL to the package repository
    license='MIT', 
)
