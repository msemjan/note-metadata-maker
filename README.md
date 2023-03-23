# Note Metadata Maker

Note Metadata Maker is a tool for generating YAML front-matter for your notes written in Python.

## Motivation

I've decided to add the following metadata for my notes:
- Author
- Date
- Description
- Tags
- Keywords

I have a lot of notes, so doing this manually would require a lot of time and effort, so I've created this tool to automate the process.

## I plan to use these technologies

- Python
- `spaCy` library for extracting keywords and generating tags
- GPT-2 for generating descriptions that summarize the note 
- YAML formatter to generate the front-matter
- `langdetect` to detect language used in the notes (some of my notes are written in different languages different than English)

## What I've learned

- How to use a pre-made machine learning model for fast prototyping

## TODO

- [ ] Add the language detection and use the correct model for the language
- [ ] Add command line arguments to select the file with notes instead of hard coding it
- [ ] Update the README:
  - [ ] List of the technologies that were actually used
  - [ ] Simple guide to describe how to use this tool
- [ ] Add license
