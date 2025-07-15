# Installation

To install Linton you’ll need Python.

Then run the following command:

```
pip install linton
```

If you have `pipx`, you may prefer:

```
pipx install --include-deps linton
```

To create a new Linton web site, use:

```
linton init DIRECTORY
```

where `DIRECTORY` is the directory in which to write the new web site’s pages and ancillary files. Linton copies the default Linton site template files and a couple of sample pages into the directory you specify. See [Invocation](../Invocation/index.html) for more details.

Then, configure the page template as described in [Template](../Template/index.html).

Write some web pages: see [How Linton makes web pages](<../How Linton makes web pages/index.html>) and [Conventions](../Conventions/index.html) for more information.

The site should now be ready to use. See [Testing](../Testing/index.html) for how to test it in dynamic mode without configuring a web server, and see the `linton publish` command in [Invocation](../Invocation/index.html) for how to produce the final files that can be uploaded to a server.

Then, see [Template](../Template/index.html) for details of the various ways in which Linton can be customized.
