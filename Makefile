# Makefile for maintainer tasks

build:
	python -m build

dist:
	git diff --exit-code && \
	rm -rf ./dist && \
	mkdir dist && \
	$(MAKE) build

test:
	tox

release:
	$(MAKE) test && \
	$(MAKE) dist && \
	version=$$(grep version pyproject.toml | grep -o "[0-9.]\+") && \
	twine upload dist/* && \
	gh release create v$$version --title "Release v$$version" dist/* && \
	git pull --tags

loc:
	cloc linton tests/*.py

.PHONY: dist build
