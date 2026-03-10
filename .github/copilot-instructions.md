# Copilot instructions for BrainKids

Purpose
- Help AI coding agents make focused, safe changes in this repository.

Big picture
- Entry point: `brain_kids/src/main.py` — creates a `Renderer` and shows the game selection.
- UI layer: `src/gui/renderer.py` (renderer drives UI and calls into game callbacks).
- Core game logic: `src/core/` contains small, responsibility-focused modules:
  - `datamanager.py`: loads JSON files from `data/*/*/files/*.json` into a dict mapping category -> list of filenames.
  - `imagemanager.py`: given a base image dir and datamanager data, selects and preloads PIL `Image` objects.
  - `gamelogic.py`: orchestrates game flow (difficulty selection, image rotation, scoring) and uses `game_ui_callback` to update UI.
  - `gamestate.py`: singleton state object — tests and changes must account for shared state between runs.
  - `scoreboard.py`: reads/writes leaderboard JSON referenced by each quiz's `DEFAULT_CHART` / `CHART_FILENAME`.
- Quizzes: `src/quizzes/*.py` define quiz factories (e.g., `Animals(renderer)`) that wire `GameLogic` + UI callback and start games.

Data layout and conventions
- Data files live under `data/<quiz>/files/`:
  - `images.json` contains a mapping category -> [filename, ...]
  - `chart.json` contains scoreboard/leaderboard data persisted by `scoreboard`.
- Image folders: `data/<quiz>/images/<Category>/<image_files>` — `ImageManager` composes paths as `base_dir / category / filename`.

Developer workflows
- Virtualenv: `python -m venv venv` then activate. Dependencies: `requirements.txt` and `requirements_dev.txt`.
- Common Make targets (see `Makefile`):
  - `make init` — install dependencies
  - `make test` — run tests (`pytest`)
  - `make lint` / `make format`
- Run app locally for development: execute `brain_kids/src/main.py` with Python (or use the Makefile target if present).
- Packaging: Nuitka command shown in `README.md` for building a single executable — note special handling for compiled runs in `main.py`.

Project-specific patterns and gotchas
- `GameState` is a singleton: tests rely on clearing or reinitializing state between runs.
- `DataManager.load()` expects a path to a JSON file (not a directory). Many quiz modules pass `DATA_FILE` which points to `images.json`.
- `ImageManager.select_images(max_per_category)` uses `random.sample` — ensure category lists are long enough for the requested difficulty.
- `GameLogic` communicates to UI solely via the `game_ui_callback` string-based events (see `core/common_ui_callback.py`): maintain that contract when changing UI messages.
- `preloaded_images` stores PIL `Image` objects; avoid serializing them or storing huge numbers of images in memory.

When editing or adding quizzes
- Follow the pattern in `src/quizzes/*`: define constants (`DIFFICULTY_RANK`, `DATA_FILE`, `IMAGE_DIR`, `DEFAULT_CHART`, `CHART_FILENAME`), create `GameLogic`, set up `ui_callback` with `create_game_ui_callback`, assign `renderer.game_callback`, then call `game_logic.start_game()`.

Tests
- Tests live under `tests/test_src/` and mirror `src/`. Use `pytest -q` or `make test`.
- To write tests mock filesystem reads of `data/*/files/*.json` or use `tests/test_data/` fixtures already in repo.

If unsure
- Open `src/quizzes/animals.py` and `src/core/gamelogic.py` for the canonical wiring example.
- Preserve the `game_ui_callback` event strings and `GameState` semantics.

If this file misses any project-specific conventions you'd like emphasized, tell me which areas to expand.
