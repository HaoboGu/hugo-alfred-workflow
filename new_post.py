#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function
import sys
import os
import subprocess
from workflow import Workflow3
from workflow import Variables

log = None
HUGO_PATH = os.getenv("SOURCE_FOLDER")


def main(wf):
    if HUGO_PATH == "" or HUGO_PATH is None:
        v = Variables()
        v["fail"] = "Please specify hugo source folder using \"hugoset\""
        print(v)
        return

    file_name = os.getenv("filename")
    file_full_path = HUGO_PATH + "/content/posts/" + file_name
    file_full_path = file_full_path.strip(" ")
    file_full_path = file_full_path.strip("\n")
    log.debug("hugo source folder: " + HUGO_PATH)
    log.debug("post path: " + file_full_path)

    command = "/usr/local/bin/hugo new posts/" + file_name
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=HUGO_PATH, executable="/bin/zsh")
    p.wait()
    if p.returncode == 0:
        # Subprocess terminates without error
        print(file_full_path, end="")
    elif p.returncode == 255:
        v = Variables()
        v["fail"] = "File already exists: " + file_full_path
        print(v)
    else:
        v = Variables()
        v["fail"] = "Internal error, error code: " + str(p.returncode)
        print(v)

    return

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
