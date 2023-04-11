run:
	python3 main.py

install:
	pip install -r requirements.txt
	python -m spacy download en_core_web_sm

fmt:
	black .
