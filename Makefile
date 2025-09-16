PY ?= python3

.PHONY: run repl test debug clean

run:
	@$(PY) main.py

repl:
	@$(PY) main.py --repl

test:
	@$(PY) -m unittest -v

debug:
	@$(PY) main.py --debug "12.3e-4" "5." --allow-trailing-dot

clean:
	@find . -name "__pycache__" -type d -exec rm -rf {} +
