# Installation

To install Linton you’ll need Python and the [Nancy](https://github.com/rrthomas/nancy) utility.

Then run the following command:

```
pip install linton
```

To create a new Linton web site, use:

```
linton init DIRECTORY
```

where `DIRECTORY` is the directory in which to write the new web site’s pages and ancillary files. Linton copies the default Linton site template files and a couple of sample pages into the directory you specify. See [Invocation](Invocation/index.html) for more details.

Then, configure Linton as described in [Configuration](Configuration/index.html).

The input files correspond directly to output files. Web pages are written as Markdown files, whose contents is then templated into the structure given by the `template.in.html` template file, which you can customize as desired. Other resources such as media files, CSS (including Linton’s own `style.css`)
and any web server configuration files, are rendered verbatim. See [How output is generated from input](<How output is generated from input/index.html>) for more details.

The site should now be ready to use. See [Testing](Testing/index.html) for how to test it in dynamic mode without configuring a web server, and see the `linton publish` command in [Invocation](Invocation/index.html) for how to produce the final files that can be uploaded to a server.

Then, see [Customization](Customization/index.html) for details of the various
ways in which Linton can be customized.
