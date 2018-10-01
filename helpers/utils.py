#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import subprocess


def call(args):
    process = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1
    )

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            break
        print(line.decode('utf-8'), end='')

    process.wait()

    response = process.communicate()  # tuple('stdout', 'stderr')
    if response[0] != b'':
        print(response[0].decode('utf-8'), end='')
    if response[1] != b'':
        print(response[1].decode('utf-8'), end='')


def generate_ui():
    script = './helpers/generate_ui.sh'

    args = [
        script,
    ]

    if platform.system() == 'Windows':
        args.insert(0, r'C:\Program Files\Git\bin\sh.exe')

    call(args)
