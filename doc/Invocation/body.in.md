# Command-line arguments

Linton provides its functionality via subcommands. It also recognizes common flags:

```
$paste{/bin/sh,-c,PYTHONPATH=. python -m linton --help | sed -e 's/usage: -m/linton/'}
```

## `linton publish`

```
$paste{/bin/sh,-c,PYTHONPATH=. python -m linton publish --help | sed -e 's/usage: -m/linton/'}
```

## `linton serve`

```
$paste{/bin/sh,-c,PYTHONPATH=. python -m linton serve --help | sed -e 's/usage: -m/linton/'}
```

## `linton init`

```
$paste{/bin/sh,-c,PYTHONPATH=. python -m linton init --help | sed -e 's/usage: -m/linton/'}
```
