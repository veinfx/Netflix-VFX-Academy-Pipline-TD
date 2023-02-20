# -*- coding: utf-8 -*-

name = 'sungwooPark'
version = '1.0.0'
authors = ['sungwooPark']
requires = [
    'python',
]
variants = [
    ['platform-linux', 'python'],
]
# tools = ['todo']

def commands():
    env.PYTHONPATH.prepend("{root}/python")


format_version = 2
