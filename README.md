# Pango Syntax Highlighter

This is an incredibly basic tool for Python 3.x for use when creating images for slides with code snippets in.  It takes a given file and using Pygments it converts it into a syntax highlighted Pango compatible output.

## Usage

```
usage: pangosyntaxhighlight.py [-h] [--language LANGUAGE] [--list-languages] [--style STYLE] [--list-styles] inputfile outputfile

Syntax highlight code in Pango format using Pygments

positional arguments:
  inputfile            the input file
  outputfile           the output file

options:
  -h, --help           show this help message and exit
  --language LANGUAGE  the syntax language of the input file (otherwise auto-detected/auto)
  --list-languages     list available languages (lexers)
  --style STYLE        highlighting style, e.g., vs
  --list-styles        list available styles

```

## Examples

To convert `myfile.cpp` to the image `myfile.png`:

```
python3 pangosyntaxhighlight.py myfile.cpp output.txt && pango-view --markup --font=mono -qo myfile.png output.txt
```

Specifying a specific programming language for a generic `.txt` file:

```
python3 pangosyntaxhighlight.py code.txt output.txt --language cpp && pango-view --markup --font=mono -qo code.png output.txt
```

Run with `--list-languages` to get a list of supported languages/lexers by short names (e.g., cpp, python, etc.). Additional short names may also work, see the [available lexers list](https://pygments.org/docs/lexers/) for the complete list. For example, `--list-languages` lists `delphi`, not `pascal`, but the latter will work.

Specifying the vs highlighting style:

```
python3 pangosyntaxhighlight.py myfile.cpp output.txt --style vs && pango-view --markup --font=mono -qo myfile.png output.txt
```

Run with `--list-styles` to get a list of styles supported by your system. [Style previews are available here](https://pygments.org/styles/).


## Requirements

python, pygments, pango
