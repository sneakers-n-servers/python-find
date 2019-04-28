# find
An implementation of my favorite UNIX command in python3

Packaged is a test symlink, a unittest, and fully functional main method

## Invocation
Running: `python -m find --help`

Yields:
```
usage: find [-H] [-L] [-P] [path...] [predicates]

default path is the current directory; default expression is -print (but with
color)

positional arguments:
  path
  predicates

optional arguments:
  -h, --help  show this help message and exit
  -P          Never follow symbolic links. This is the default behaviour.
  -L          Follow symbolic links.
  -H          Do not follow symbolic links, except while processing the
              command line arguments.

Only expressions availible are -print and -print0
```

## TODO
* Add the exec callback
* Fix the broken pipe error when running the module with a pipe e.g `python -m find | less`
* Add the mindepth and maxdepth predicates (limited by parseargs)
* Add regex and name matching
* Unit testing, ignored due to force creation of acceptable environment
* Examine possible inefficiency in regards to callback and `os.scandir` meaning `os.fstat`
