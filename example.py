from html_generator import *

print(
  html(
    head(title("Hello, ", "world!"),
      style("body { color:red; }\n", type="text/html")),
    body(
      h1("Welcome"),
      p("This is a paragraph."),
      p("This is another.")), lang="en"))
