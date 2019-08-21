#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Set Hugo source folder

"""
from __future__ import print_function

__author__ = "Haobo Gu"
__email__ = "haobogu@outlook.com"
__date__ = "2019.08.16"

import sys
import os

from workflow import Workflow3
from workflow.util import set_config


def main(wf):
    if len(wf.args):
        hugo_folder_path = wf.args[0]
        if os.path.exists(hugo_folder_path):
            set_config("SOURCE_FOLDER", str(hugo_folder_path), exportable=False)
            print("Successfully set source folder !", end="")
        else:
            print("Please specify a valid path !", end="")


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
