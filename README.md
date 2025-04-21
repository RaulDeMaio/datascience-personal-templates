Here’s the updated `README.md` reflecting all the recent improvements you've applied, including removal of DVC and Hydra, added testing, enriched pre-commit setup with `mypy` and `nbQA`, improved docs and developer UX, and notebook management guidelines.

---

```markdown
# 🧠 Data Science Project Template

This template was built after reading [this excellent article by khuyetran1401](https://towardsdatascience.com/how-to-structure-an-ml-project-for-reproducibility-and-maintainability-54d5e53b4c82?sk=c3d05ae5b8ccc95822618d0dacfad8a4).  
Rather than forking, I’ve rebuilt it myself to understand each component. The goal is **simplicity, reproducibility, and maintainability** for personal and experimental data science projects.

For industrial or enterprise-grade pipelines, tools like [Kedro](https://docs.kedro.org/en/stable/) are still preferable.

---

## 🚀 Features and Roadmap

### ✅ Implemented

- Automatically build repository structure
- Create and build Conda environment
- Enforce static typing and clean code with pre-commit
- Run unit tests with `pytest`
- Auto-lint notebooks using `nbQA`
- Generate HTML documentation with `pdoc`

### 📋 To Do

- Automate some setup steps with CLI
- Add GitHub Action for CI
- Setup centralized logging and error tracking

---

## 🧰 Tools Used

| Tool           | Purpose                                                |
|----------------|--------------------------------------------------------|
| [Conda](https://docs.conda.io/) | Environment management                    |
| [pre-commit](https://pre-commit.com/) | Code quality automation                |
| [pytest](https://docs.pytest.org/) | Unit testing framework                   |
| [mypy](http://mypy-lang.org/) | Static type checking                      |
| [black](https://black.readthedocs.io/en/stable/) | Code formatting                    |
| [flake8](http://flake8.pycqa.org/) | Linting                                |
| [nbQA](https://nbqa.readthedocs.io/) | Code quality checks on Jupyter Notebooks |
| [pdoc](https://pdoc.dev/) | Automatic documentation generator         |

---

## 🧱 Template Structure

```bash
.
├── config/                      # Conda and pipeline configuration
│   └── environment.yml          # Conda environment definition
├── data/                        # Data folders (local, untracked)
│   ├── 01_raw/
│   ├── 02_primary/
│   ├── 03_feature/
│   ├── 04_model_input/
│   ├── 05_model_output/
│   └── 06_reporting/
├── docs/                        # HTML and markdown documentation
├── models/                      # Saved models and config
├── notebooks/                   # Jupyter notebooks (experimental zone)
│   └── README.md                # Notebook structure and usage guide
├── scripts/                     # Scripts folder
│   └── setup_cli.py             # Script to setup CLI
├── src/                         # Source code for data pipeline, modeling, etc.
│   └── main.py
├── tests/                       # Unit tests
│   └── test_main.py
├── .pre-commit-config.yaml      # Hooks for linting, formatting, typing
├── Makefile                     # Automation: setup, lint, test, docs
└── README.md
```

---

## 🛠 How to Use This Template

### 📦 Install Cookiecutter

```bash
pip install cookiecutter
```

### 🧪 Generate New Project

```bash
cookiecutter https://github.com/radema/datascience-personal-templates
```

### ⚙️ Setup Your Environment

```bash
cd {{cookiecutter.repository-name}}
conda env create -f config/environment.yml
conda activate {{cookiecutter.environment_name}}
make setup
```

### 🧪 Run Tests

```bash
make test
```

### 📚 Generate Documentation

```bash
make docs
```

### ⚡ Automate Setup via CLI

You can automate environment creation, setup, testing, and docs generation using the built-in CLI.

Example:

```bash
python scripts/setup_cli.py all
```

Or use individual steps:

```bash
python scripts/setup_cli.py create-env --env-name=my_env
python scripts/setup_cli.py activate --env-name=my_env
python scripts/setup_cli.py test
python scripts/setup_cli.py docs
```

You can also run:

```bash
make cli
```

to open the CLI menu directly.


---

## 📓 Notebook Guidelines

Notebooks are stored in `notebooks/` and follow a numeric prefix convention:

```
01_data_exploration.ipynb
02_feature_engineering.ipynb
03_model_training.ipynb
```

Code quality is enforced in notebooks using `nbQA` integrated with pre-commit (`black`, `flake8`, `mypy`).

---

## 📖 Resources

- [khuyentran1401/data-science-template](https://github.com/khuyentran1401/data-science-template/blob/dvc-poetry/README.md)
- [Kedro starters](https://github.com/kedro-org/kedro-starters)

---

```

Let me know if you want me to write the updated `Makefile`, `.pre-commit-config.yaml`, or help generate badges and shields for the top of the README!