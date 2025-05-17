install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl --force
	
test:
	uv run pytest

lint:
	uv run ruff check

check: 
	test lint

