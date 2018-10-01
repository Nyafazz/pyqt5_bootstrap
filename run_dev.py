#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import platform

from helpers import utils


def main():
    print('generate ui: START')
    utils.generate_ui()
    print('generate ui: END')

    args = [
        {
            'Windows': r'.\venv\Scripts\python.exe',
            'Linux': r'./venv/bin/python',
            'Darwin': r'./venv/bin/python',
        }.get(platform.system()),
        r'./pyqt5_bootstrap/pyqt5_bootstrap.py'
    ]

    print('app: START')
    utils.call(args)
    print('app: END')


if __name__ == '__main__':
    main()
