# About

This repository contains several [Jupyter](https://jupyter.org/) notebooks. These notebooks
are the course material for an upcoming [openSAP](https://open.sap.com/) course on [Python 🐍](https://www.python.org/).

## Contributing

In order to ensure that all output is removed from the Jupyter notebooks in the repository a
a specific pre-commit hook is used. This hook is managed using the [pre-commit](https://pre-commit.com/)
framework. To activate the pre-commit hook on your development machine:

1. Install pre-commit by installing the dev dependencies from the [Pipfile](./Pipfile). This can, for example,
be done by executing `pipenv install --dev`.
1. Execute `pre-commit install` to generate the pre-commit hook.

## Acknowledgements

The work on this material has been supported by:

- The [SQSL-Project](https://www.fh-aachen.de/en/hochschule/projekt-sqsl/) of the FH Aachen
- The [Stifterverband](https://www.stifterverband.org/) in the context of a [Senior-Fellowship für Innovationen in der digitalen Hochschullehre](https://www.stifterverband.org/digital-lehrfellows-nrw/2019/drumm)
