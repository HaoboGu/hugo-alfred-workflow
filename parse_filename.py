#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow3


def main(wf):
    log = wf.logger
    if len(wf.args):
        file_name = wf.args[0]
        if not file_name.endswith(".md"):
            file_name += ".md"
        file_name = file_name.replace(" ", "-")

        # In Script filter, use item
        it = wf.add_item('Create a post: ' + file_name, arg='filename', valid=True)
        it.setvar('filename', file_name)

        log.info("Successfully parsed filename")
        wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
