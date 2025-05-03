Here’s the updated `README.md` tailored for your **uv-based Data Science Project Template**, replacing all Conda references with `uv`, and fully aligned with the updated project structure, CLI, and GitHub Actions CI.

---

# 🧠 Data Science Project Template (uv version)

This template is designed for fast, reproducible, and maintainable personal data science projects using [`uv`](https://github.com/astral-sh/uv) for dependency management.

Inspired by [khuyetran1401's article](https://towardsdatascience.com/how-to-structure-an-ml-project-for-reproducibility-and-maintainability-54d5e53b4c82?sk=c3d05ae5b8ccc95822618d0dacfad8a4), this setup is intended to stay lightweight and clean, while still enforcing quality practices.

> For production-grade orchestration, consider [Kedro](https://docs.kedro.org/en/stable/).

---

## 🚀 Features

- Build project structure instantly with Cookiecutter
- Manage environments and dependencies with [`uv`](https://github.com/astral-sh/uv)
- Pre-commit checks for formatting, linting, typing, notebook quality
- Auto-generate docs using `pdoc`
- Run unit tests via `pytest`
- Logging setup for both scripts and notebooks
- Built-in CLI for full automation

---

## 🧰 Tools Used

| Tool           | Purpose                                                |
|----------------|--------------------------------------------------------|
| [uv](https://github.com/astral-sh/uv) | Fast dependency management & venv |
| [pre-commit](https://pre-commit.com/) | Code quality automation |
| [pytest](https://docs.pytest.org/) | Unit testing framework |
| [mypy](http://mypy-lang.org/) | Static type checking |
| [black](https://black.readthedocs.io/en/stable/) | Code formatting |
| [flake8](http://flake8.pycqa.org/) | Linting |
| [nbQA](https://nbqa.readthedocs.io/) | Notebook linting |
| [pdoc](https://pdoc.dev/) | Documentation generator |
| [click](https://click.palletsprojects.com/) | CLI interface for setup |

---

## 🧱 Template Structure

```bash
.
├── config/                    # Optional config files
├── data/                      # Data folders (not tracked)
│   ├── 01_raw/                # Raw immutable data
│   ├── 02_primary/            # Domain-level cleaned data
│   ├── 03_feature/            # Features for modeling
│   ├── 04_model_input/
│   ├── 05_model_output/
│   └── 06_reporting/
├── docs/                      # Auto-generated documentation
├── models/                    # Saved models
├── notebooks/                 # Jupyter notebooks
│   ├── 00_example_notebook.ipynb
│   └── README.md
├── scripts/                   # CLI and utility scripts
│   └── setup_cli.py
├── src/                       # Core source code
│   ├── logging_utils.py
│   └── main.py
├── tests/                     # Unit tests
│   └── test_main.py
├── .github/workflows/ci.yml  # GitHub Actions CI workflow
├── .gitignore
├── .pre-commit-config.yaml
├── Makefile
├── pyproject.toml
└── README.md
```

---

## ⚙️ Quick Start

### 🧱 1. Generate a Project

```bash
pip install cookiecutter
cookiecutter https://github.com/radema/datascience-personal-templates
```

### 🛠 2. Setup the Project with uv

```bash
uv venv
uv pip install -e .
make setup  # runs pre-commit install
```

Or use the full automation CLI:

```bash
python scripts/setup_cli.py all
```

---

## 🔧 Developer CLI

You can automate common steps using:

```bash
python scripts/setup_cli.py create-env
python scripts/setup_cli.py install
python scripts/setup_cli.py test
python scripts/setup_cli.py docs
```

---

## 🧪 Testing

Run tests:

```bash
make test
```

Or from the CLI:

```bash
python scripts/setup_cli.py test
```

---

## 📓 Notebooks

Located in `notebooks/`, using a numbered convention:

```
01_data_exploration.ipynb
02_feature_engineering.ipynb
03_model_training.ipynb
```

Best practices:
- Keep modular and clean
- Restart + clear outputs before commits
- Auto-checked with `nbQA` in pre-commit

---

## 🧼 Pre-commit Hooks

Includes:
- `black`, `flake8`, `isort`, `mypy`, `interrogate`
- `nbQA` for notebook linting
- Whitespace, large file checks

Run manually with:

```bash
pre-commit run --all-files
```

---

## 📚 Generate Docs

Use:

```bash
make docs
```
Docs will be saved to the `docs/` folder using [`pdoc`](https://pdoc.dev).

---

## 🔁 Continuous Integration

This project includes GitHub Actions CI:
- Installs environment with `uv`
- Runs pre-commit hooks
- Runs `pytest`

You can find the config under `.github/workflows/ci.yml`.

---

## 📖 References

- [khuyentran1401/data-science-template](https://github.com/khuyentran1401/data-science-template/blob/dvc-poetry/README.md)
- [Kedro starters](https://github.com/kedro-org/kedro-starters)
- [uv documentation](https://github.com/astral-sh/uv)

---
=======
Let me know if you want me to write the updated `Makefile`, `.pre-commit-config.yaml`, or help generate badges and shields for the top of the README!