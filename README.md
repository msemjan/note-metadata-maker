# Note Metadata Maker (Work in progress)

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

The summarization of the text was done with the [Hugging Face](https://huggingface.co/) transformers library. 

At the end I didn't use Hugging face library for generating tags. It wasn't precise enough to use without fine-tuning the model, and I didn't have time and will to create a training data set with labeled notes. So I've cheated a little bit. My files have a fairly consistent naming convention, e.g. a note about AWS  Lambda functions would be named `AWS_lambda.md`, or a note about creating a Git repository on a flash drive would be named `git_how_to_create_a_repository_on_flash_drive.md`. I always use underscores for separating words, and I try to use descriptive file names. Because of this naming convention I can guess what tags should be assigned to each note, and I've created a simple helper function, which will generate a list of tags based on the name of the file.

## Installation

Run `make install` to install all dependencies.

## TODO

- [ ] Add the language detection and use the correct model for the language
- [ ] Add command line arguments to select the file with notes instead of hard coding it
- [ ] Update the README:
  - [ ] List of the technologies that were actually used
  - [ ] Simple guide to describe how to use this tool
- [ ] Add license
