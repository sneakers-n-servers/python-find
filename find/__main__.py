#!/usr/bin/env python3
import argparse
from os.path import exists

from find.callbacks import print_color, print0
from find import find


def parse_args(arg_parser):
    args = arg_parser.parse_args()
    arg_dict = vars(args)
    arg_dict['callback'] = print_color
    for predicate in args.predicates:
        if predicate == '-print0':
            arg_dict['callback'] = print0
            break
        if predicate == '-print':
            arg_dict['callback'] = print
            break
        arg_parser.error("unknown predicate '{}'".format(predicate))
    return arg_dict


def path_exists(path: str) -> str:
    if not exists(path):
        raise argparse.ArgumentTypeError("'{}': No such file or directory".format(path))
    return path


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='find',
        description='default path is the current directory; default expression is -print (but with color)',
        epilog='Predicates available are -print and -print0',
        usage='find [-H] [-L] [-P] [path...] [predicates]'
    )
    parser.add_argument(
        'path',
        nargs='*',
        type=path_exists
    )
    parser.add_argument(
        '-P',
        action='store_false',
        dest='follow_links',
        default=False,
        help='Never  follow  symbolic  links.  This is the default behaviour.'
    )
    parser.add_argument(
        '-L',
        action='store_true',
        dest='follow_links',
        help='Follow symbolic links.'
    )
    parser.add_argument(
        '-H',
        action='store_true',
        dest='arg_links',
        default=False,
        help='Do not follow symbolic links, except while processing the command line arguments.'
    )
    parser.add_argument(
        'predicates',
        nargs=argparse.REMAINDER
    )
    return parser


def main():
    arg_parser = create_parser()
    arg_dict = parse_args(arg_parser)
    return find(arg_dict['path'], **arg_dict)


if __name__ == '__main__':
    ret = main()
    exit(ret)