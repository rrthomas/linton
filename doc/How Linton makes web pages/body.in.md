# How Linton makes web pages

Linton delegates the actual work of making web pages to two other tools:

+ A Markdown to HTML converter. You can use whichever one you like; by default, Linton is configured to use [Discount](http://www.pell.portland.or.us/~orc/Code/discount/). If you want to use a different program, edit `markdown-to-html.in.sh` in the your web site’s source directory. The script must produce an HTML fragment (that is, some HTML that can be inserted into a `<body>` element) on standard output, given a filename on the command line.
+ The Nancy macro expander. See its [documentation](https://github.com/rrthomas/nancy) and in particular its Cookbook for full details of how it works.

Now, we will outline how Linton builds web pages, and explain some conventions that it uses.

+ Linton puts each page in its own directory. A directory typically contains all the resources specific to a page, such as images, plus two special files:
    + `body.in.md` is the main contents of the page, written in [Markdown](https://daringfireball.net/projects/markdown/).
    + `index.nancy.html` is a small stub file, usually the same for every page, that simply includes the page template.
+ Most files in the input directory are simply copied to the output. There are two exceptions:
    + Files whose names contain the suffix `.in` are not copied to the final web site (they are only used for *in*put).
    + Files whose names contain the suffix `.nancy`, usually either HTML or Markdown files, are sent to Nancy for macro expansion. The result is written to the output with the `.nancy` suffix removed: for example, `index.nancy.html` expands to a file called `index.html`.

For more information about the page template, see [Template](../Template/index.html).