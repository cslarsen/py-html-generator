"""A quick-and-dirty HTML generator library.

Written by Christian Stigen Larsen
2014-03-05

Placed in the public domain by the author.

Works fairly well, but the only problem is that attributes need to come
AFTER any subtags, which basically makes this unusable.  E.g.

    html(body("hello, world"), lang="en")
                               ^^^^^^^^^^ should come first, as in
    html(lang="en", body("hello, world"))

I think a solution would be to do

    html(attrs(lang="en"), body("hello, world"))

with some special handling of `attrs', but that doesn't look as natural as
using normal keywords.
"""

import cgi

def escape(s):
  """Escapes special characters for HTML text."""
  return cgi.escape(s).encode('utf-8', 'xmlcharrefreplace')

def escape_attr(s):
  """Escapes special characters for attribute values."""
  return escape(s).replace("'", "\"")

def Tag(name):
  """Returns a named tag class."""
  class _NamedTag():
    def __init__(self, *items, **attrs):
      self.name = name
      self.items = items
      self.attrs = attrs
      self.indent = 0

    def __str__(self):
      s = "  " * self.indent
      if self.name is not None:
        s += "<%s" % self.name
        for k,v in self.attrs.items():
          s += " {}='{}'".format(k, escape_attr(v))
        s += ">"

      # Only contains text?
      text = all(map(lambda x: isinstance(x, "".__class__), self.items))

      if not text: s += "\n"

      # Does text-only tag contain newlines?
      newlines = True
      if text:
        newlines = any(map(lambda t: t.count("\n")>0, self.items))

      for num, item in enumerate(self.items):
        if isinstance(item, "".__class__):
          if newlines:
            s += "\n"
            s += "  "*(self.indent+1)
          s += escape(item.lstrip())
          if num+1 < len(self.items): s += " "
        else:
          item.indent = self.indent + 1
          s += item.__str__()

      # Indent if it's a normal tag or is text with newlines
      if newlines:
        s += "  " * self.indent

      if self.name is not None:
        s += "</%s>" % self.name

      s += "\n"

      return s

  return _NamedTag

html = Tag("html")
head = Tag("head")
title = Tag("title")
style = Tag("style")
h1 = Tag("h1")
p = Tag("p")
body = Tag("body")

if __name__ == "__main__":
  print("<!DOCTYPE html>")
  print(
    html(
      head(title("Hello,", "world!"),
        style("body { color:red; }\n", type="text/css")),
      body(
        h1("Welcome"),
        p("This is a paragraph.", "3 > 2"),
        p("This is another.")), lang="en"))

