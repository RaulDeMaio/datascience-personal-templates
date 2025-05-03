.PHONY: setup test docs clean cli

setup:
	uv venv
	uv pip install -r requirements.txt
	uv pip install -e .  # if you want to install your package in editable mode
	pre-commit install

test:
	pytest tests/

docs:
	pdoc src --html --output-dir docs

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

cli:
	python scripts/setup_cli.py
