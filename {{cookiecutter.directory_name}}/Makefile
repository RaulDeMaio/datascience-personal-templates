.ONESHELL:

SHELL = /bin/zsh
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

activate-env:
	@echo "Activating virtual environment ..."
	conda env update --prune -f config/environment.yml

initialize-git:
	@echo "Initializing Git..."
	git init
	git add .
	git commit -m "Setup project"

pre-commit-install:
	@echo "Installing pre commit"
	$(CONDA_ACTIVATE) {{cookiecutter.environment_name}}; pre-commit install

setup: activate-env initialize-git pre-commit-install

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

test:
	pytest tests/

docs:
	pdoc src --html --output-dir docs

