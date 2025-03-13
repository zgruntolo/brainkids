# BrainKids

## Development

Use the following commands to create, activate, and deactivate the virtual environment.

```shell
python -m venv venv
source venv/Scripts/activate
deactivate
```

Use the following commands to create a single .exe file.

```shell
pyinstaller --noconsole --onefile --add-data "data;data" --add-data "src;src" --icon=data/gui/images/icon.ico --name BrainKids --paths src src/main.py
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

* data/: Contains data content files used by the application.
* src/: Contains the source code of the project.
* core/: Contains core functionality modules.
* gui/: Contains modules related to the graphical user interface.
* tests/: Contains unit tests for the project.
* requirements.txt: Lists the Python dependencies required for the project.

```code
brain_kids/
├── data/
│   ├── gui/
│   │   ├── images/
│   │   │   ├── difficulties.jpg
│   │   │   ├── icon.icns
│   │   │   ├── icon.ico
│   │   │   ├── icon.png
│   │   │   ├── intro.jpg
│   │   │   └── name.jpg
│   ├── lakeriversea/
│   │   ├── files/
│   │   │   ├── chart.json
│   │   │   └── images.json
│   │   ├── images/
│   │   │   ├── Fiume/
│   │   │   │   │   └── ...
│   │   │   │   ├── Lago/
│   │   │   │   │   └── ...
│   │   │   │   ├── Mare/
│   │   │   │   │   └── ...
│   │   ├── livingornot/
│   │   │   ├── files/
│   │   │   │   ├── chart.json
│   │   │   │   └── images.json
│   │   │   ├── images/
│   │   │   │   ├── Non Vivente/
│   │   │   │   │   └── ...
│   │   │   │   ├── Vivente/
│   │   │   │   │   └── ...
│   │   ├── treeparts/
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
│   ├── src/
│   │   ├── core/
│   │   │   ├── common_ui_callback.py
│   │   │   ├── datamanager.py
│   │   │   ├── gamelogic.py
│   │   │   ├── gamestate.py
│   │   │   ├── imagemanager.py
│   │   │   └── scoreboard.py
│   │   ├── gui/
│   │   │   └──renderer.py
│   │   ├── quizzes/
│   │   │   ├── lakeriversea.py
│   │   │   ├── livingornot.py
│   │   │   └── treeparts.py
│   │   └── main.py
├── tests/
│   ├── (test files)
│   └── ...
├── Makefile
├── pyproject.toml
├── README.md
├── requirements_dev.txt
└──  requirements.txt
```
