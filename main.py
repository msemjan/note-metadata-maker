#!/usr/bin/env python3
"""Script for generating front-matter metadata in YAML format for Markdown notes"""
import os
import datetime
import yaml
from transformers import pipeline

TAG_TRASHHOLD=0.85

AUTHOR = os.getenv("AUTHOR") if os.getenv("AUTHOR") else os.getenv("USER")
DATE = datetime.datetime.now()

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

summarizer = pipeline(task="summarization", model="facebook/bart-large-cnn")
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-cnn")
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
    "description": summary["summary_text"],
}

print("---")
print(yaml.dump(metadata, indent=2))
print("---")
