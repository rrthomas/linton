# Writing web pages for Linton

Linton has some particular conventions for writing web pages that are mostly chosen either to work well with Nancy, to keep Linton itself simple, or to enable Linton web sites to work well both when served from a proper web server, and when run using the test `linton serve` web server.

## Page organization

Each page is stored in its own directory, and named `index.html`. This is done so that all the materials for a page can be stored separately from other pages.

This means that published URLs for your web site never need to include `.html`, as, for example, the page `foo/bar/index.html` will have a URL that ends `foo/bar`.

For details of how the page is structured internally, see [Template](Template).

## Page names including reserved characters

Note that links to Linton pages whose names contain certain characters must be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding), so that characters with special significance to web servers, such as question mark, are not treated as special. (Deliberately using these characters with their special meaning is fine!)

It is also safer to add a trailing slash to links to Linton pages, as otherwise some web servers still seem to misinterpret them. For example, link to a page called “Why?” with the relative URL `Why%3F/`, rather than just `Why%3F`.
