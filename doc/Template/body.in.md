# Template

The layout of the generated HTML pages can be customized by editing `template.in.html` and `style.css`, and the following files at the top level of your site’s source directory:

=`Title.in.txt`=
    The name of the web site.
=`Author.in.txt`=
    The name of the web site's owner.
=`Email.in.txt`=
    The email address of the web site's owner.
=`favicon.ico`=
    The web site icon, which is often shown by browsers in tab or window headings, or in bookmarks.

## The page template

It is beyond the scope of this manual to give a full explanation of the page template, as that requires in-depth knowledge of HTML and CSS (the main languages used in web pages). This section gives a few details of the template’s organization.

The template is built using the [Bootstrap](https://getbootstrap.com) web framework, a widely-used and flexible open-source web framework. See its web site for more details on how to use its features. The template loads the full version of Bootstrap, so all of its functionality is available out of the box.

The functionality of the default template is quite rich, and you are encouraged to remove or alter elements that do not meet your needs; or of course to add more elements. For more complex functionality, such as the left-hand menu and the breadcrumb trail at the top of the window, external scripts are used, which are executable files at the top level of the web site directory; you may wish to study those that are supplied to see how to write similar scripts of your own.

The page has the following principal elements:

+ The page `<title>` is set to the site title followed by the page title (or, for the home page, just the site title).
+ Two `<nav>` elements contain a breadcrumb trail from the top of the site to the current page (at the top of the page) and a list of pages and subdirectories in the same directory as the current page (in the left-hand margin).
+ The `<main>` element contains the page’s main content, derived from the `body.in.md` Markdown file in the page’s directory. Underneath is a short notice saying when the page was last updated.
+ The `<footer>` element contains links to the site licence (assumed to be in the top-level `Licence` directory), and the author’s (or administrator’s) name and email address, both linked to the email address.

The page automatically adjusts its colouring to a light or dark scheme according to the reader’s preferences as set in their web browser.