from typing import Union, List, Callable
from sys import stderr
from os.path import islink, isfile
from os import scandir


def find(paths: Union[List[str], str] = None, **kwargs) -> int:
    """
    Recurse all directories passed in as paths, defaults to current dir.
    Options to be added to kwargs as needed.
    :param paths: A list of paths to recurse
    :param kwargs: A dictionary of options
    :return: The exit value
    """
    if not paths:
        paths = ['.']
    if isinstance(paths, str):
        paths = [paths]

    follow_links = kwargs.get('follow_links', False)
    arg_links = kwargs.get('arg_links', False)
    callback = kwargs.get('callback', print)

    for path in paths:
        if islink(path) and not arg_links:
            callback(path)
            if follow_links:
                _walk(path, follow_links, callback)
        elif isfile(path):
            callback(path)
        else:
            callback(path)
            _walk(path, follow_links, callback)
    return 0


def _walk(path: str, follow_links: bool, callback: Callable):
    try:
        with scandir(path) as scan:
            for file in scan:
                callback(file.path)
                if file.is_dir(follow_symlinks=follow_links):
                    _walk(file.path, follow_links, callback)
    except OSError as e:
        print(e, file=stderr)
