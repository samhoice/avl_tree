#!/usr/bin/env just --justfile

test:
    PYTHONPATH=src pipenv run pytest .
