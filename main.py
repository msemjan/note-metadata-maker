#!/usr/bin/env python3
"""Script for generating front-matter metadata in YAML format for Markdown notes"""
import os
import datetime
import yaml
from transformers import pipeline

TAG_TRASHHOLD=0.85

AUTHOR = os.getenv("AUTHOR") if os.getenv("AUTHOR") else os.getenv("USER")
DATE = datetime.now()

tags = ["education",
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
        "diary"]

with open("notes.txt", "r") as f:
    text = f.read()

summarizer = pipeline(task="summarization")
summary = summarizer(text)

classifier = pipeline("zero-shot-classification")
tag_prob = classifier(
    text,
    candidate_labels=tags,
    multi_class=True,
)

found_tags = []
for tag, prob in zip(tags, tag_prob):
    if prob >= TAG_TRASHHOLD:
        found_tags.append(tag)

metadata = {
    "author": AUTHOR,
    "date": DATE,
    "tags": found_tags,
    "description": summary,
}

print("---")
print(yaml.dump(metadata, default_flow_state=False, indent=2))
print("---")
