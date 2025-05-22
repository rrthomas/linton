# Command-line arguments

Linton provides its functionality via subcommands. It also recognizes common flags:

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton --help | sed -e 's/usage: -m/linton/')```

## `linton publish`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton publish --help | sed -e 's/usage: -m/linton/')```

Note that `--update` uses Nancy’s `--update` flag, which causes Nancy to find the input files that are referenced by a given output file, and only re-generate or copy the output file if one or more inputs is newer. This does not run any programs, so it will not detect all updates; for example, if an program referenced by a web page prints the current time, or something random. The intended use of `--update` is to speed up updating web sites using long-running programs whose output depends only on regular input files; for example, complex file type conversions.

## `linton serve`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton serve --help | sed -e 's/usage: -m/linton/')```

## `linton init`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton init --help | sed -e 's/usage: -m/linton/')```
