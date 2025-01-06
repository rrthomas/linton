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
	make test
	make dist
	twine upload dist/* && \
	gh release create v$$version --title "Release v$$version" dist/*

loc:
	cloc linton tests/*.py

.PHONY: dist build
