.PHONY: venv setup compile-deps sync-deps clean

venv:
	python -m venv .venv
	@echo "Virtual environment created. Activate it with:"
	@echo "Windows: .venv\\Scripts\\activate"
	@echo "Unix: source .venv/bin/activate"

setup: venv
	.venv\Scripts\python -m pip install --upgrade pip
	.venv\Scripts\pip install pip-tools

compile-deps:
	.venv\Scripts\python scripts/setup/compile_requirements.py

sync-deps: compile-deps
	.venv\Scripts\pip-sync requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .venv/
