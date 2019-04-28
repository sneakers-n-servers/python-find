#!/usr/bin/env python3
import argparse
import os

from find.callbacks import print_color, print0
from find import find


def path_exists(path: str) -> str:
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError("'{}': No such file or directory".format(path))
    return path


def parse_args(arg_parser):
    args = arg_parser.parse_args()
    ret = vars(args)
    ret['callback'] = print_color
    for predicate in args.predicates:
        if predicate == '-print0':
            ret['callback'] = print0
            break
        arg_parser.error("unknown predicate '{}'".format(predicate))
    return ret


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Find',
        description='This is my description',
        epilog='Thats how you do'
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
        default=False
    )
    parser.add_argument(
        '-L',
        action='store_true',
        dest='follow_links',
    )
    parser.add_argument(
        '-H',
        action='store_true',
        dest='arg_links',
        default=False
    )
    parser.add_argument(
        'predicates',
        nargs=argparse.REMAINDER
    )
    return parser


def main():
    arg_parser = create_parser()
    arg_dict = parse_args(arg_parser)
    ret = find(arg_dict['path'], **arg_dict)
    exit(ret)


if __name__ == '__main__':
    main()
