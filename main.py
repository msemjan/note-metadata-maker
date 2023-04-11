#!/usr/bin/env python3
"""Script for generating front-matter metadata in YAML format for Markdown notes"""
import os
import datetime
import subprocess
import yaml
from helpers import get_tags
from transformers import pipeline

SUMMARIZER_MODEL = "facebook/bart-large-cnn"
INPUT_DIR = "./test"

AUTHOR = os.getenv("AUTHOR") if os.getenv("AUTHOR") else os.getenv("USER")
DATE = datetime.datetime.now()

def is_git_repo(path):
    """Returns if the given directory is a git repository"""
    res = subprocess.Popen(
        "git rev-parse --is-inside-work-tree",
        cwd=path,
        stdout=subprocess.PIPE,
        shell=True,
    ).communicate()[0]

    return "true" in res


def get_git_file_timestamp(path):
    """Runs a git command to find the first commit in which the file was
    commited"""
    directory, file = os.path.split(path)

    return subprocess.Popen(
        f"git log --follow --format=%ad --date default {file} | tail -1",
        cwd=directory,
        stdout=subprocess.PIPE,
        shell=True,
    ).communicate()[0]


def get_file_timestamp(path):
    """Retrieve the timestampt of the file. If the file is in a git repository,
    it will get the date of the first commit in which the file was commited
    instead."""

    if is_git_repo(path):
        return get_git_file_timestamp(path)

    return os.path.getctime(path)


def parse_file(file, summarizer):
    #  def parse_file(file, summarizer, classifier):
    """Function for generating metadata from text"""

    with open(file, "r") as f:
        text = f.read()

    if "index" in file:
        title = file.replace(".wiki", "").replace(".md", "").split("_").title()
        summary = f"This is an index for {title}"
    else:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        summary = summary[0]["summary_text"]

    found_tags = get_tags(file)

    metadata = {
        "author": AUTHOR,
        "date": DATE,
        "tags": found_tags,
        "description": summary,
    }

    return metadata


def to_yaml(metadata):
    return "---\n" + yaml.dump(metadata, indent=2) + "\n---"


if __name__ == "__main__":
    summarizer = pipeline(task="summarization", model=SUMMARIZER_MODEL)

    notes = os.listdir(INPUT_DIR)

    print("Files detected:")
    print(notes)

    for note in notes:
        if not os.path.isfile(os.path.join(INPUT_DIR, note)):
            print(f"{note} is not a file")
            continue

        metadata = parse_file(os.path.join(INPUT_DIR, note), summarizer)
        
        print(f"{datetime.datetime.now()} - {note}")
        print(to_yaml(metadata))
