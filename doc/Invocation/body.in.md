# Command-line arguments

Linton provides its functionality via subcommands. It also recognizes common flags:

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton --help | sed -e 's/usage: -m/linton/')```

## `linton publish`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton publish --help | sed -e 's/usage: -m/linton/')```

## `linton serve`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton serve --help | sed -e 's/usage: -m/linton/')```

## `linton init`

```
$run(/bin/sh,-c,PYTHONPATH=. python3 -m linton init --help | sed -e 's/usage: -m/linton/')```
