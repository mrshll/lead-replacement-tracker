# Design
There are three components to this project:
1. **Extract** project inventory data from pdfs (this can be done either with human-in-the-loop automation or fully manually)
2. **Load** data (in csv format) into a database
3. **Display** the data in one or more visualizations

## Extract

After a brief survey of technologies, a few pdf extraction frameworks provide solid extraction of structured output (tables):
- [Poppler](https://poppler.freedesktop.org/)
- [Camelot](https://github.com/camelot-dev/camelot)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

Experimentation with a few pdfs with tabular data showed ~Camelot~ pdfplumber had slightly more consistent results, although it seems also that many of these libraries have the same underlying dependencies.

[Okular](https://okular.kde.org/) is also worth mentioning, as it is a application-based pdf viewer that uses Poppler to allow users to extract text.

## Load

TODO

## Display

TODO
