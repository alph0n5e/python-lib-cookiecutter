from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIREMENTS = [
    # Third party Requirements,
    {%- if cookiecutter.generate_command_line_interface|lower not in ['n', 'no'] %}
    'click',
    {%- endif %}
]

TEST_REQUIREMENTS = [
    'pytest>=3',
    'pytest-cov',
    'pytest-runner'
]

DEV_REQUIREMENTS = [
    'bump2version',
    'flake8'
]


setup(
    name='{{ cookiecutter.package_name }}',
    short_description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    version='{{ cookiecutter.version }}',
    url='https://github.com/alph0n5e/{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.7',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    test_suite='tests',
    extras_require={
        'test': TEST_REQUIREMENTS,
        'dev': TEST_REQUIREMENTS + DEV_REQUIREMENTS
    },
    {%- if cookiecutter.generate_command_line_interface|lower not in ['n', 'no'] %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.repo_name }}={{ cookiecutter.package_name }}.cli:main',
        ],
    },
    {%- endif %}
)
