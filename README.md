# Living Or Not

## Development

Use the following commands to create, activate, and deactivate the virtual environment.

```shell
python -m venv venv
source venv/bin/activate
deactivate
```

The Makefile contains frequent utility commands.

```shell
# install dependencies
make init

# run linter checks
make lint

# format codebase
make format

# run tests
make test

## Project structure

* src/: Contains the source code of the project.
* core/: Contains core functionality modules.
* gui/: Contains modules related to the graphical user interface.
* config/: Contains configuration files.
* tests/: Contains unit tests for the project.
* data/: Contains data content files used by the application.
* requirements.txt: Lists the Python dependencies required for the project.

```code
nexusnovel/
├── src/
│   ├── core/
│   │   ├── (source files)
│   │   └── ...
│   ├── gui/
│   │   ├── (source files)
│   │   └── ...
│   ├── config/
│   │   ├── config.json
│   │   └── ...
│   └── ...
├── tests/
│   ├── (test files)
│   └── ...
├── data/
│   ├── (data files)
│   └── ...
├── requirements.txt
├── README.md
├── setup.py
└── ...
```
