# School Test Suite

## Development

Use the following commands to create, activate, and deactivate the virtual environment.

```shell
python -m venv venv
source venv/Scripts/activate
deactivate
```

Use the following commands to create a single .exe file.

```shell
pyinstaller --noconsole --onefile --add-data "livingornot;livingornot" --add-data "src;src" --add-data "treeparts;treeparts" --icon="src/gui/images/favicon.ico" --name SchoolTestSuite main.py
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
* tests/: Contains unit tests for the project.
* data/: Contains data content files used by the application.
* requirements.txt: Lists the Python dependencies required for the project.

```code
school/
├── schooltestsuite/
│   ├── livingornot/
│   │   ├── (module files)
│   │   ├── data/
│   │   │   ├── files/
│   │   │   │   ├── chart.json
│   │   │   │   └── images.json
│   │   │   ├── images/
│   │   │   │   ├── Non Vivente/
│   │   │   │   │   └── ...
│   │   │   │   ├── Vivente/
│   │   │   │   │   └── ...
│   │   └── livingornot.py
│   ├── src/
│   │   ├── core/
│   │   │   ├── chart.py
│   │   │   ├── common_ui_callback.py
│   │   │   ├── datamanager.py
│   │   │   ├── gamelogic.py
│   │   │   ├── imagemanager.py
│   │   │   └── state.py
│   │   ├── gui/
│   │   │   ├── images/
│   │   │   │   ├── intro.png
│   │   │   │   └── name.png
│   │   │   └──renderer.py
├── tests/
│   ├── (test files)
│   └── ...
├── treeparts/
│   │   ├── (module files)
│   │   ├── data/
│   │   │   ├── files/
│   │   │   │   ├── chart.json
│   │   │   │   └── images.json
│   │   │   ├── images/
│   │   │   │   ├── Fusto/
│   │   │   │   │   └── ...
│   │   │   │   ├── Foglie/
│   │   │   │   │   └── ...
│   │   │   │   ├── Radici/
│   │   │   │   │   └── ...
│   │   └── treeparts.py
│   └── main.py
├── Makefile
├── README.md
├── requirements_dev.txt
├── requirements.txt
└── setup.py
```
