import os
from collections import defaultdict
from stat import S_ISDIR, S_ISLNK, S_ISFIFO, S_ISSOCK
from pathlib import Path

def default_color() -> str:
    return '00'


def _create_default_color_map() -> defaultdict:
    colors = os.getenv('LS_COLORS', '')
    color_map = defaultdict(default_color)
    for color in colors.split(':'):
        if not color:
            continue
        equal_index = color.index('=')
        color_map[color[:equal_index]] = color[equal_index + 1:]
    return color_map


COLOR_MAP = _create_default_color_map()


def _get_color(path) -> str:
    mode = os.lstat(path).st_mode
    if S_ISDIR(mode):
        return COLOR_MAP['di']
    if S_ISLNK(mode):
        return COLOR_MAP['ln']
    if S_ISFIFO(mode):
        return COLOR_MAP['pi']
    if S_ISSOCK(mode):
        return COLOR_MAP['so']
    suffix = ''.join(['*', Path(path).suffix])
    return COLOR_MAP[suffix]


def print_color(path):
    """
    Prints a path in conjuction with LS_COLORS
    :param path: The path to print
    :return: None
    """
    print('\033[{}m{}\033[0m'.format(_get_color(path), path))


def print0(path):
    """
    Prints the path ending with a null byte
    :param path: The path to print
    :return: None
    """
    print(path, end='\x00')
