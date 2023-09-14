from setuptools import setup, find_packages

setup(
    name='asm2vec',
    version='1.0.0',
    description='Unofficial implementation of asm2vec using pytorch',
    install_requires=['torch',
                      'click',
                      'r2pipe'],
    author='oalieno',
    author_email='jeffrey6910@gmail.com',
    license='MIT License',
    packages = find_packages(),
)
