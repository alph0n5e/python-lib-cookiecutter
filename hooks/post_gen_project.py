#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.generate_command_line_interface|lower }}' in ['n', 'no']:
        cli_file = os.path.join('src', '{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)
