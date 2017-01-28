#!/usr/bin/env python

import sys, os
import json
import random as rand

_module_dir = os.path.realpath(os.path.dirname(__file__))
_default_path = os.path.join(_module_dir, 'tonyisms.json')
_TONYISMS = None

def get(source=_default_path):
    global _TONYISMS

    if _TONYISMS is None:
        with open(source) as f:
            _TONYISMS = json.load(f) 

    return _TONYISMS


def random():
    tonyisms = get()
    choice = rand.randint(0, len(tonyisms)-1)
    return tonyisms[choice]


if __name__ == '__main__':
    print random()

