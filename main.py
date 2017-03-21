#!/usr/bin/python
#vim: set fileencoding=utf8

import os, argparse

from taskfile import *

parser  = argparse.ArgumentParser(description="KISS task manager")
p = parser.add_mutually_exclusive_group()

p.add_argument("-l", action="store_true", help="list tasks")
p.add_argument("-a", nargs=1, type=str, metavar="<name>", help="add task")
p.add_argument("-d", nargs='+', type=int, metavar="<id>", help="delete task")
p.add_argument("-r", nargs=2, metavar=("<id>", "<name>"), help="rename task")

args = parser.parse_args()

tf = taskfile(os.environ.get("HOME")+"/.config/tasky/tasks")

if args.l:
    tf.show()
elif args.a:
    tf.add(args.a[0])
elif args.d:
    tf.remove(args.d)
elif args.r:
    tf.rename(int(args.r[0]), args.r[1])
else:
    tf.show()

tf.save()
