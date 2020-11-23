#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dirname):
    result = []
    paths = os.listdir(dirname)  # list of paths in that dir
    for file_name in paths:
        match = re.search(r'__(\w+)__', file_name)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, file_name)))
    return result


def copy_dir(paths, todir):
    if not os.path.exists(todir):
        os.mkdir(todir)
    for path in paths:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(todir, fname))


def zip_dir(paths, tozip):
    cmd = 'zip -j ' + tozip + ' ' + ' '.join(paths)
    print("Command I'm going to do:" + cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    # If command had a problem (status is non-zero),
    # print its output to stderr and exit.
    if status:
        sys.stderr.write(output)
        sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    paths = []
    for dirname in args:
        paths.extend(get_special_paths(dirname))

    if todir:
        copy_dir(paths, todir)
    elif tozip:
        zip_dir(paths, tozip)
    else:
        print('\n'.join(paths))


if __name__ == "__main__":
    main()
