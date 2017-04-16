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

all: check test install

check:
	$(FLAKE8) $(SOURCEDIR) --show-source  --statistics --count

test:
	green

install:
	python setup.py sdist install

upload:
	python setup.py sdist upload -r pypi



