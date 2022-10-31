#! /usr/bin/python

import os

if __name__ == "__main__":
    print os.environ.get('SOME_OTHER', 'nothing')