Python HTML document tree generator and rendering library
=========================================================

A quick-and-dirty HTML generator library.

Example
-------

Running

    from html_generator import *

    print("<!DOCTYPE html>")
    print(
      html(
        head({"lang": "en"},
          title("Hello, ", "world!"),
          style("body { color:red; }\n", type="text/css")),
        body(
          h1("Welcome"),
          p("This is a paragraph."),
          p("This is another."))))

produces

    <!DOCTYPE html>
    <html lang='en'>
      <head>
        <title>Hello, world!</title>
        <style type='text/css'>
          body { color:red; }
        </style>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>This is a paragraph.</p>
        <p>This is another.</p>
      </body>
    </html>

License
-------
Written by Christian Stigen Larsen

Placed in the public domain by the author.

2014-03-05

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

Also, I don't support so-called empty tags, as in `<br/>`.  You're free to
add it, though!

Attributes
----------

To create attributes, for instance `<a href='foo'>Foo</a>`, you can do
either of

    a("Foo", href="foo")

or

    a({"href": "foo"}, "Foo")

