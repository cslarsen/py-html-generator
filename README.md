Python HTML document tree generator and rendering library
=========================================================

A quick-and-dirty HTML generator library.

License
-------
Written by Christian Stigen Larsen
2014-03-05

Placed in the public domain by the author.


Example
-------

Running

    from html_generator import *

    print("<!DOCTYPE html>")
    print(
      html(
        head(
          title("Hello, ", "world!"),
          style("body { color:red; }\n", type="text/html")),
        body(
          h1("Welcome"),
          p("This is a paragraph."),
          p("This is another.")), lang="en"))

produces

    <!DOCTYPE html>
    <html lang='en'>
      <head>
        <title>Hello,  world!</title>
        <style type='text/html'>
          body { color:red; }
        </style>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>This is a paragraph.</p>
        <p>This is another.</p>
      </body>
    </html>


Adding more tags
----------------

I've only added support for the HTML tags used in the example.
You can add more by doing, e.g.

    table = Tag("table")
    tr = Tag("tr")
    td = Tag("td")

Problems
--------

This is just something I threw together to test how I could create a HTML
document in memory and render it as a string.

I realize there must be dozens such libraries out there, but I don't mind.

Works *fairly* well, but the only problem is that attributes need to come
AFTER any subtags, which basically makes this unusable.  E.g.

    html(body("hello, world"), lang="en")
                               ^^^^^^^^^^ should come first, as in
    html(lang="en", body("hello, world"))

I think a solution would be to do

    html(attrs(lang="en"), body("hello, world"))

with some special handling of `attrs', but that doesn't look as natural as
using normal keywords.

Also, I don't support so-called empty tags, as in `<br/>`.  You're free to
add it, though!
