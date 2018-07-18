"""Main Tasky file"""

import os
import argparse
from taskfile import Taskfile

def parse_args():
    """Return the parser for command line arguments"""
    parser = argparse.ArgumentParser(description="KISS task manager")
    parser_grp = parser.add_mutually_exclusive_group()

    parser_grp.add_argument('-l', action='store_true', help='list tasks')
    parser_grp.add_argument('-a', nargs=1, type=str, metavar='<name>', help='add task')
    parser_grp.add_argument('-d', nargs='+', type=int, metavar='<id>', help='delete task(s)')
    parser_grp.add_argument('-r', nargs=2, metavar=('<id>', '<name>'), help='rename task')

    return parser.parse_args()

CONFIG_PATH = os.environ.get('HOME')+'/.config/tasky'
ARGS = parse_args()

if not os.path.exists(CONFIG_PATH):
    os.makedirs(CONFIG_PATH)

TASKFILE = Taskfile(CONFIG_PATH+'/tasks')

if ARGS.l:
    TASKFILE.show()
elif ARGS.a:
    TASKFILE.add(ARGS.a[0])
elif ARGS.d:
    TASKFILE.remove(ARGS.d)
elif ARGS.r:
    TASKFILE.rename(int(ARGS.r[0]), ARGS.r[1])
else:
    TASKFILE.show()

TASKFILE.save()
