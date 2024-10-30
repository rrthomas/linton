# Makefile for maintainer tasks

all: README.md

dist: all
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	python -m build

test:
	tox

release:
	make test
	make dist
	twine upload dist/* && \
	git tag v$$(grep version pyproject.toml | grep -o "[0-9.]\+") && \
	git push --tags
