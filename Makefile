install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
test:
	python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py

lint:
	pylint --disable=R,C *.py nlplogic/*.py

format:
	black *.py nlplogic

all: install lint test format
