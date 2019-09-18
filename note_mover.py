#!/usr/bin/python
# encoding: utf-8
from __future__ import print_function

import sys
import io
import os
from workflow import Workflow3
from workflow import Variables
from datetime import datetime
import pytz

log = None


def generate_header(file_name):
    author = os.getenv("AUTHOR")
    if author is None:
        author = ""
    header = "---\n" + generate_title(file_name) + generate_author(author) + \
             generate_tag() + generate_date() + generate_draft() + generate_summary() + "---\n"
    return header

def generate_title(file_name):
    title = file_name.split(".")[0]
    title_str = "title: \"" + title + "\"\n"
    return title_str


def generate_author(author):
    author_str = "author: \"" + author + "\"\n"
    return author_str


def generate_tag():
    tag_str = "tags: []\n"
    return tag_str

def generate_draft():
    draft_str = "draft: true\n"
    return draft_str

def generate_date():
    tz = pytz.timezone("Asia/Shanghai")
    date_str = "date: " + datetime.now(tz).isoformat() + "\n"
    return date_str

def generate_summary():
    summary_str = "summary: \n"
    return summary_str

def main(wf):
    success = False
    if len(wf.args):
        file_path = ""
        for item in wf.args:
            file_path = file_path + item + " "
        file_path = file_path.strip(" ")
        if not file_path.endswith(".md"):
            return
        file_name = os.path.basename(file_path)
        header = generate_header(file_name)
        file_name = file_name.replace(" ", "-")
        log.debug("file path: " + file_path)
        with io.open(file_path, "r", encoding='utf-8') as input_file:
            note_content = input_file.read()
            note_content = header + note_content
            hugo_folder = os.getenv("SOURCE_FOLDER")
            if hugo_folder is None or hugo_folder == "":
                v = Variables()
                v["fail"] = "Please specify hugo source folder using \"hugoset\""
                print(v)
                return

            blog_path = hugo_folder + "/content/posts/" + file_name
            log.debug("post path: " + blog_path)
            with io.open(blog_path, 'w') as output_file:
                output_file.write(note_content)
                success = True
            if success:
                print(blog_path, end="")
            else:
                print("Cannot open the target folder", end="")
                return
    if not success:
        log.error("wrong")
        print("No file found", end="")


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
