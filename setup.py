from setuptools import setup, find_packages

setup(
        name='shaw',
        version='1.0.1',
        description='Common python package',
        url='https://github.com/hangyan/shaw',
        author='Hang Yan',
        author_email='yanhangyhy@gmail.com',
        license='GPL V3',

        # See https://pypi.python.org/pypi?%3Action=list_classifiers
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
        ],
        packages=find_packages(),
        keywords='common utils web',
        install_requires=[
            'colorlog',
        ]
)
