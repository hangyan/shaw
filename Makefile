OS = Linux

VERSION = 0.0.1

CURDIR = $(shell pwd)
SOURCEDIR = $(CURDIR)

ECHO = echo
RM = rm -rf
MKDIR = mkdir
FLAKE8 = flake8
PIP_INSTALL = sudo pip install

.PHONY: all setup build test help

all: check test

check:
	$(FLAKE8) $(SOURCEDIR) --show-source  --statistics --count

test:
	green

upload:
	python setup.py sdist upload -r pypi



