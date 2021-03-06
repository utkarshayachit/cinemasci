# Cinemasci python tools
[![Build Status](https://travis-ci.org/cinemascience/cinemasci.svg?branch=master)](https://travis-ci.org/cinemascience/cinemasci)

A set of python tools for reading, writing and viewing Cinema databases

## tools

### cdb

Tools for reading, writing and manipulating a cinema database

- Current [docs](cinemasci.md)

### cis

Tools for reading, writing and manipulating *composable image sets*

## Unit testing

All code shall be committed with unit testing, using python's `unittest` module. All tests shall be run on code commit, with the following command, which will automatically run all files in the testing directory:

```
    python -m unittest discover testing
```

For each submodule included:

1. There shall be a unit testing file in `testing/` named `test_<modulename>.py`
2. All tests are expected to **pass**.

## Coding standards

This project uses coding standards spelled out in [PEP8](https://www.python.org/dev/peps/pep-0008/)

