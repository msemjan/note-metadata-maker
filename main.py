#!/usr/bin/env python3
"""Script for generating front-matter metadata in YAML format for Markdown notes"""
import os
import datetime
import subprocess
import yaml
from transformers import pipeline

TAG_TRASHHOLD = 0.85

AUTHOR = os.getenv("AUTHOR") if os.getenv("AUTHOR") else os.getenv("USER")
DATE = datetime.datetime.now()

tags = [
    "education",
    "programming",
    "science",
    "politics",
    "business",
    "physics",
    "data science",
    "machine learning",
    "philosophy",
    "arts",
    "crafts",
    "survival",
    "recipes",
    "miscellaneous",
    "memes",
    "traveling",
    "diary",
]


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


def parse_file(file, summarizer, classifier):
    """Function for generating metadata from text"""

    with open(file, "r") as f:
        text = f.read()

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

    results = classifier(
        text,
        candidate_labels=tags,
        multi_class=True,
    )

    found_tags = []
    for tag, prob in zip(tags, results["scores"]):
        if prob >= TAG_TRASHHOLD:
            found_tags.append(tag)

    metadata = {
        "author": AUTHOR,
        "date": DATE,
        "tags": found_tags,
        "description": summary[0]["summary_text"],
    }

    return metadate


def to_yaml(metadata):
    return "---\n" + yaml.dump(metadata, indent=2) + "\n---"


if __name__ == "__main__":
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-cnn")
    summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")

    note = "notes.txt"

    metadata = parse_file(note, summarizer, classifier)

    print(to_yaml(metadata))
