from setuptools import find_packages, setup
setup(
    name='ivs_project_2',
    packages=find_packages(include=['math_lib']),
    version='0.1.0',
    description='Math library for calculator',
    author='xsirov01, xhrici01, xbrand13 , xblask05',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
