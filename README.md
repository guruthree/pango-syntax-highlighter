# Pango Syntax Highlighter

This is an incredibly basic tool for Python 3.x for use when creating images for slides with code snippets in.  It takes a given file and using Pygments it converts it into a syntax highlighted Pango compatible output.

Usage example:

```
python3 pangosyntaxhighlight.py cpp myfile.cpp output.txt && pango-view --markup --font=mono -qo image.png output.txt
```
